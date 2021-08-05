from selenium import webdriver
import chromedriver_binary
import subprocess
import webbrowser
from selenium.webdriver.chrome.options import Options

#ここいるヘルパーを実行する
x = subprocess.Popen(["start","", r"C:\Users\60837\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\DAIWA-KASEI\KokoiruHelper.appref-ms"],shell=True)




option = Options()
#ヘッドレスモードで実行
option.add_argument("--headless")

driver = webdriver.Chrome(options=option)

#更新を最大10秒待つ
driver.implicitly_wait(10)
#ここいるのサイトを表示する
driver.get("http://202.155.1.80/kokoiru/kokoiru.php?user_code=60837")
driver.quit()

