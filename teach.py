from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# id元素定位
def test(url,name,key,clk):
        dt = webdriver.Chrome()
        dt.maximize_window()
        dt.get(url)
        test = dt.find_element_by_id(name)
        test.send_keys(key)
        #键盘事件
        test.send_keys(clk)
test('https://www.runoob.com','s','python',Keys.ENTER)
