"""
File: score_input_script.py
Description: This Python script automates the process of inputting scores into an online education system. It reads course scores from an Excel file, opens a web page for score input, and enters scores for each student based on their student ID.

Author: [Your Name]
Date: [Date]

Prerequisites:
- Python libraries: pandas, selenium
- Chrome WebDriver installed (chromedriver.exe)
- An Excel file named 'Scores.xlsx' with sheets containing course codes and student scores.

"""

# Import necessary libraries
import pandas as pd
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Part 1: Read data from the Excel file
Scores = pd.read_excel('c:/Scores.xlsx', None)
CourseCodes = list(Scores.keys())

# Part 2: Check if the Excel sheets correspond to course codes
print("Your Excel file contains the following sheets which are expected to be course codes: ", CourseCodes)
Ans1 = input("Enter 1 if correct, or 2 to exit:")
if Ans1 not in ['1', ""]:
    print('Please review your Excel file following the control instructions and make corrections.')
    quit()

# Part 3: Open a web page for score input
print('Next, a Google Chrome page will open, guiding you to the login page of the educational system. After entering your username and password, navigate to the score input section and enter the course code for the scores you want to input. Then click the "Submit Scores" button.')
Ans2 = input('Press 1 to continue: ')
if Ans2 not in ['1']:
    quit()

# Part 4: Define functions and automate score input
def ScoreInput(CourseCode):
    ScorestoInput = Scores[str(CourseCode)]
    NumberOfStudentsInTheList = len(driver.find_element_by_xpath('-----------------------'))
    for i in range(1, NumberOfStudentsInTheList + 1):
        StudentIDXpath = '----------' % i
        StudentId = driver.find_element_by_xpath(StudentIDXpath).text
        print(StudentId)
        for j in range(ScorestoInput.shape[0]):
            if int(Scores.iat[j, 0]) == int(StudentId):
                print(Scores.iat[j, 0])
                StudentScoreXpath = '--------------------' % i
                driver.find_element_by_xpath(StudentScoreXpath).send_keys(str(Scores.iat[j, 2]))
        time.sleep(1)

def Openweb():
    driver = webdriver.Chrome(executable_path=r'C:------------------/chromedriver.exe')
    driver.get("-------------------/loginPage.jsp")

def FindCourseCode():
    CourseCode = driver.find_element_by_xpath('-----------').text
    return CourseCode

Openweb()
CourseCode = FindCourseCode()
ScoreInput(CourseCode)
