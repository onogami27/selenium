import time
from selenium import webdriver
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');



#クロームドライバーをset
driver = webdriver.Chrome()
#更新を最大10秒待つ
driver.implicitly_wait(10)

#サイトのURLを指定
driver.get("http://202.155.1.80/kokoiru/kokoiru.php?user_code=60837")
#場所を指定（IDタグで指定）
#elem_search = driver.find_element_by_id("")
#指定した場所に.send_keysで文字を入力
#elem_search.send_keys("")
#elem_button = driver.find_element_by_id("")
#elem_button.click()
#time.sleep(2)
#driver.get("")
na = driver.find_element_by_class_name("form-control")
na.send_keys("おのがみ")

#x = driver.find_element_by_class_name("btn btn-default")
x= driver.find_element_by_class_name("btn.btn-default")
x.click()
y = driver.find_elements_by_class_name("btn.btn-info")
y[12].click()
print(y[12].text)
