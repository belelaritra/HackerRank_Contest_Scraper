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
Code_path = tkw.folder_path
Contest_URL = tkw.contest_url
Problem = tkw.problem


print('Name: ' + username+'\nPassword: *****' +'\nContest Name: ' + Contest_URL + '\nQuestion Name: '+Problem+'\nFolder Path: '+ Code_path)

#Language dict
langauge_dict={'java8':'java',
                'java':'java',
                'cpp':'cpp',
                'c':'c',
                'python3':'py',}


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

time.sleep(5)

#Dropdown List (UserId)
driver.find_element_by_xpath("//*[@id='content']/div/div/div/div/div[1]/nav/div/div[2]/ul[2]/li[3]/div/div").click()
time.sleep(1)

#Administration
driver.find_element_by_xpath("//*[@id='content']/div/div/div/div/div[1]/nav/div/div[2]/ul[2]/li[3]/div/div[2]/ul/li[7]/a").click()
time.sleep(1)

#Contest Number
contest = driver.find_element_by_partial_link_text(Contest_URL)
contest_url = contest.get_attribute("href")
driver.get(contest_url)
time.sleep(2)

#Challenges
driver.find_element_by_xpath("//*[@id='content']/div/section/header/div/div[3]/ul/li[2]/a").click()
time.sleep(4)

#Question Number
question = driver.find_element_by_partial_link_text(Problem)
question_url = question.get_attribute("href")
driver.get(question_url)
time.sleep(1)

#View Element
try:
    driver.find_element_by_xpath("//*[@id='content']/div/div/section/div/div[2]/div[1]/div/div/aside/div/div[7]/p/a").click()
    
    length = len(driver.find_elements_by_xpath('//div[@class="pagination-wrap clearfix pagination-wrapper"]/div[@class="pagination"]/ul/li'))
    page_no = int(length) - 3
    for i in range(1,page_no):
        driver.get(Problem_URL+ "/" + str(i))
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
                
                #code location
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

                name_with_path = os.path.join(folder_path, filename)
                file = open(name_with_path, 'w')
                file.write(str(code))
                file.close()
                time.sleep(2)
            else:
                pass
except:
    print("You Have No Permission To View Submissions")
