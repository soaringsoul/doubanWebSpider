# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import json
import pandas as pd



def get_bookinfo(bookinfo):
    # 获取作者信息
    author_result = bookinfo.find('script', {'type': 'application/ld+json'})
    author_info = json.loads(list(author_result)[0])
    bookName = author_info.get('name')
    try:
        bookAuthor = author_info['author'][0]['name']
    except:
        bookAuthor = ''
    bookIsbn = author_info.get("isbn")
    bookUrl = author_info.get("url")

    # 获取评价人数
    voteNum = bookinfo.find('span', {'property': 'v:votes'})
    voteNum = voteNum.text.strip()
    # 获取豆瓣评分
    voteAvg = bookinfo.find('strong', {'property': 'v:average'})
    voteAvg = voteAvg.text.strip()

    return [bookName, bookAuthor, bookIsbn, voteAvg, voteNum, bookUrl]


def get_pagesource_by_bookname(bookname="人类简史"):
    driver = webdriver.Firefox(executable_path=r"./tools/geckodriver.exe")  # Firefox浏览器

    # driver.set_window_size(width=960, height=1080, windowHandle="current")

    url = "https://book.douban.com/"
    print("  \b\b当前搜索的书名：【%s】" % bookname)
    driver.get(url)
    search_box = driver.find_element_by_id("inp-query")
    search_box.send_keys(bookname)
    print('  \b\b输入关键词：%s' % bookname)
    # 定位搜索按钮
    button = driver.find_element_by_class_name("inp-btn")
    # 点击搜索按钮
    print("  \b\b点击搜索按钮，开始搜书！")
    button.click()
    print('  \b\b成功搜索，将自动点击搜索结果列表中的第一本书！')
    pageSource = driver.page_source
    bookurl_pat = r"[a-zA-z]+://book.douban.com/subject/[0-9]{1,10}"
    bookurls = re.findall(bookurl_pat, pageSource)
    driver.get(bookurls[0])
    content = driver.page_source.encode('utf-8')
    driver.quit()
    return content


def get_single_bookinfo(bookname="人类简史"):
    html_content = get_pagesource_by_bookname(bookname)
    bookinfo = BeautifulSoup(html_content, 'lxml')
    bookinfo_lst = get_bookinfo(bookinfo)
    return bookinfo_lst


def bookname_clean(bookname):
    pat = r'.txt|epub|.mobi|.azw3|.pdf'
    bookname = re.sub(pat, '', bookname)
    return bookname


if __name__ == "__main__":
    excel_filepath = input("请输入包含书名的excel文件路径：\n")
    colname = input("指定excel文件中的书名所在的列名，默认为【书名】") or "书名"
    if len(colname.strip()) == 0:
        colname = "书名"
    df = pd.read_excel(excel_filepath.strip())
    print("您选择的excel文件共有【%s】本书需要爬取豆瓣信息:" % df.shape[0])

    for name in df[colname]:
        print(name)

    print("*"*50)
    print("现在开始从豆瓣采集书籍信息了！")
    db_bookinfo_colname = ["豆瓣书名", "作者", "ISBN", "豆瓣评分", "评分人数", "豆瓣链接"]
    new_row_lst = []
    for index, row in df.iterrows():
        bookname = bookname_clean(row['书名'])

        # bookinfo = [bookName, bookAuthor, bookIsbn, voteAvg, voteNum, bookUrl]
        try:
            bookinfo = get_single_bookinfo(bookname)
            print("  \b\b获取到的图书信息：%s" % bookinfo)
        except Exception as e:
            print("\b\b未获取到此书的信息，错误详情:%s" % e)
            bookinfo = ['' for i in range(6)]
        i = 0
        for col in db_bookinfo_colname:
            row[col] = bookinfo[i]
            i += 1
        new_row_lst.append(row)
        print("*" * 30)
    new_df = pd.DataFrame(new_row_lst)
    new_df.to_excel("采集完成的豆瓣图书信息.xlsx", index=False)
