import os
import time
import pyperclip as pc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
#Import File
import tkinter_window

#TKINTER
tkw = tkinter_window.Window()

#Variable collected from Tkinter
username = tkw.username
password = tkw.password
Contest = tkw.contest_url
Problem = tkw.problem
Code_path = tkw.folder_path

print('Name: ' + username+'\nPassword: *****' +'\nContest Name: ' + Contest + '\nQuestion Name: '+Problem+'\nFolder Path: '+ Code_path)

#Language Dictionary
langauge_dict={'java8':'java',
                'java':'java',
                'cpp':'cpp',
                'c':'c',
                'python3':'py',}

#Chrome Driver PATH
driver = webdriver.Chrome(r"___ChromeDriver Path___")

#Mazimize current window
driver.maximize_window()

#HackerRank Login page
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
contest = driver.find_element_by_partial_link_text(Contest)
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

try:
#View Submissions
    driver.find_element_by_xpath("//*[@id='content']/div/div/section/div/div[2]/div[1]/div/div/aside/div/div[7]/p/a").click()
#Current Page URL   
    Problem_URL = driver.current_url
#Number Of Pages + 1
    page_no = len(driver.find_elements_by_xpath("//a[@class='backbone']"))
#Loop for Each Page
    for i in range(1,page_no):
        #New Page Url
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
#Paste 
                code = pc.paste()
#File Open (Write Mode) --> Choosed Path, File Name=Id.language
                name_with_path = os.path.join(Code_path, filename)
                file = open(name_with_path, 'w')
                file.write(str(code))
                file.close()
                time.sleep(2)
            else:
                pass
except:
    print("You Have No Permission To View Submissions")

driver.close()
