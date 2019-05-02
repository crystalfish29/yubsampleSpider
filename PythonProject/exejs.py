from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By 
#如果你可以不用定位器，就不要用，毕竟这样可以少导入一个模块。但是，定位器是一种
#十分方便的工具，可以用在不同的应用中，并且具有很好的灵活性。

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('/usr/local/bin/chromedriver',
                          chrome_options=chrome_options)
wait = WebDriverWait(driver, timeout=10)
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
try:
    wait.until(expected.visibility_of_element_located((By.ID, "loadedButton"))).click()
finally:
    print(driver.find_element_by_id('content').text)
   # print(driver.page_source)
    driver.quit()
