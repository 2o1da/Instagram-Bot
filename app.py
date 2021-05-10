from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')

# 페이지 이동
driver.get('https://www.instagram.com/')

time.sleep(2)

# 키 입력
# 클래스 이름 중복일 수 있으므로 순서 직접 확인 필요
e = driver.find_elements_by_class_name('_2hvTZ')[0]
e.send_keys("ID")

e = driver.find_elements_by_class_name('_2hvTZ')[1]
e.send_keys("PASWORD123")

e.send_keys(Keys.ENTER)

e = driver.find_elements_by_class_name('댓글칸')[0]
e.click()
e = driver.find_elements_by_class_name('댓글칸')[0]
e.send_keys("댓글내용")

# 클래스 이름이 없는 경우
# '#id_name', .'class_name', 'tag'
e = driver.find_element_by_css_selector('#. ')[0]

# 데이터 수집
e = driver.find_element_by_css_selector('본문')[0].text
print(e)

time.implicitly_wait(5)

e = driver.find_element_by_class_name('이미지')[0].get_attribute('src')
