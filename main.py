import os
import time
import pyperclip as pc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import tkinter_window

tkw = tkinter_window.Window()

#CREDENTIALS
username = tkw.username
password = tkw.password

#Language dict
langauge_dict={'java8':'java',
                'java':'java',
                'cpp':'cpp',
                'c':'c',
                'python3':'py',}
time.sleep(0.5)

Code_path = tkw.folder_path
Contest_URL = tkw.contest_url

print(username+'\n'+password+'\n'+Code_path+'\n'+Contest_URL)

#PATH
driver = webdriver.Chrome(r"___ChromeDriver Path___")

#Mazimize current window
driver.maximize_window()

#1st URL
driver.get("https://www.hackerrank.com/auth/login?h_l=body_middle_left_button&h_r=login")

#LOGIN ID, PASSWORD, ENTER
driver.find_element_by_id("input-1").send_keys(username)
driver.find_element_by_id("input-2").send_keys(password)
driver.find_element_by_xpath('//button[@type="submit"]').click()


driver.get(str(Contest_URL))

#CODE URL
length = len(driver.find_elements_by_xpath('//div[@class="pagination-wrap clearfix pagination-wrapper"]/div[@class="pagination"]/ul/li'))
page_no = int(length) - 3
for i in range(1,page_no):
    driver.get(str(Contest_URL) + "/" + str(i))
    time.sleep(2)

    #View Result of 10
    Results = driver.find_elements_by_xpath('//a[@class="view-results"]')
    result_list = []
    for result in Results:
        url = result.get_attribute("href")
        result_list.append(url)
    time.sleep(2)

    #Score
    Scores = driver.find_elements_by_xpath('//div[@rel="tooltip"]/p[@class="small"]')
    score_list = []
    for score in Scores:
        marks = score.text
        score_list.append(marks)
    time.sleep(2)

    #Names
    Names = driver.find_elements_by_xpath('//div[@class="clearfix row-btn submissions_item"]/div[2]/p/a[@class="challenge-slug backbone"]')
    name_list = []
    for name in Names:
        nm = name.text
        name_list.append(nm)
    time.sleep(2)

    #Language3
    Languages = driver.find_elements_by_xpath('//div[@class="clearfix row-btn submissions_item"]/div[4]/p[@class="small"]')
    language_list = []
    for language in Languages:
        lang = language.text
        language_list.append(lang)
    time.sleep(2)

    for j in range(len(result_list)):
        if score_list[j] != "0":
            filename = str(name_list[j]) + "." + str(langauge_dict[language_list[j]])
            print(filename)
            driver.get(result_list[j])
            time.sleep(2)

            text_box = driver.find_element_by_css_selector("span.cm-variable")
            actions = ActionChains(driver)
            actions.move_to_element(text_box)
            actions.click()
            time.sleep(2)

            #COPY ALL
            actions.key_down(Keys.LEFT_CONTROL).send_keys("a").key_up(Keys.LEFT_CONTROL)
            actions.key_down(Keys.LEFT_CONTROL).send_keys("c").key_up(Keys.LEFT_CONTROL)
            actions.perform()
            time.sleep(4)

            code = pc.paste()

            name_with_path = os.path.join(str(Code_path), filename)
            file = open(name_with_path, 'w')
            file.write(str(code))
            file.close()
            time.sleep(2)
        else:
            pass
