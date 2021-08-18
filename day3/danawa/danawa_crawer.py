from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

browser = webdriver.Chrome("./webdriver/chromedriver.exe")

#크롬 내부 대기
browser.implicitly_wait(5)

#브라우저 사이즈 설정
browser.set_window_size(1920, 1280)

#페이지 이동
browser.get("http://prod.danawa.com/list/?cate=12215657&15main_12_02")

#webdriverwait 사용, 체크박스 클릭
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#searchMakerRep702'))).click()
time.sleep(2)


#현재 페이지
cur_page = 1
#최대(마지막) 페이지
max_page = 2

#파일 열기
f = open("./result/result.txt", "w", encoding='UTF-8')

while(cur_page <= max_page):   
    #bs4 객체 생성
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    #상품 리스트 가져오기
    prod_list = soup.select("div.main_prodlist.main_prodlist_list > ul > li")

    for product in prod_list:
        if product.select_one("div.prod_rel_content"):
            prod_name = product.select_one("p.prod_name > a").text.strip()
            prod_price = product.select_one("p.price_sect > a > strong").text.strip()
            
            text = f"상품명 : {prod_name}, 가격 : {prod_price}\n"
            f.write(text)

    cur_page += 1
    if cur_page > max_page:
        break

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'div.number_wrap > a:nth-child({cur_page})'))).click()
    time.sleep(2)

#파일 닫기
f.close()

#브라우저 닫기
browser.close()