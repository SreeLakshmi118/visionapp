from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = 'C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# Visit the login page and enter credentials
driver.get("http://127.0.0.1:8000/")
driver.maximize_window()
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("admin")
driver.find_element(By.ID, "submit").click()

# Check if login was successful
expected_url = "http://127.0.0.1:8000/admin/"
current_url = driver.current_url
if expected_url == current_url:
    print("Admin_reads Test Case Passed")
else:
    print("Login Test Case Failed")
presc_link = driver.find_element(By.XPATH, '//*[@id="jazzy-sidebar"]/div/nav/ul/li[8]/a/p')
presc_link.click()
# Wait for a few seconds before clicking the book button
time.sleep(2)
# driver.get("http://127.0.0.1:8000/")
# driver.maximize_window()
# driver.find_element(By.ID, "username").send_keys("admin")
# driver.find_element(By.ID, "password").send_keys("admin")
# driver.find_element(By.ID, "submit").click()

# # Check if login was successful
# expected_url = "http://127.0.0.1:8000/admin/"
# current_url = driver.current_url
# if expected_url == current_url:
#     print("Admin_quiz_question Test Case Passed")
# else:
#     print("Login Test Case Failed")
# presc_link = driver.find_element(By.XPATH, '//*[@id="jazzy-sidebar"]/div/nav/ul/li[6]/a')
# presc_link.click()
# # Wait for a few seconds before clicking the book button
# time.sleep(2)

# # Visit the audiobook page and check if it was loaded
# driver.find_element(By.ID, "book").click()
# expected_url = "http://127.0.0.1:8000/admin/visionapp/quizquestion/"
# current_url = driver.current_url
# if expected_url == current_url:
#     print("quiz_questions_added  Test Case Passed")
# else:
#     print("quiz_questions_added Test Case Failed")

# Close the browser
driver.quit()

# # driver.find_element(By.ID, "quiz").click()
# # expected_url = "http://127.0.0.1:8000/quiz"
# # current_url = driver.current_url
# # if expected_url == current_url:
# #     print("quiz Test Case Passed")
# # else:
# #     print("quiz Test Case Failed")

# # # # Close the browser
# driver.quit()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select

# PATH = 'C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver.exe'
# driver = webdriver.Chrome(PATH)

# # Visit the login page and enter credentials
# driver.get("http://127.0.0.1:8000/")



# # Login
# username = driver.find_element(By.ID, 'username')
# password = driver.find_element(By.ID, 'password')
# username.send_keys('admin')
# password.send_keys('admin')
# login_button = driver.find_element(By.ID, 'btn')
# login_button.click()

# if driver.current_url == 'http://127.0.0.1:8000/admin/visionapp/':
#     print(' Admin Login successful')
# else:
#     print(' Admin Login failed')

# # Navigate to the desired page
# presc_link = driver.find_element(
#     By.XPATH, '//*[@id="jazzy-sidebar"]/div/nav/ul/li[6]/a')
# presc_link.click()


# driver.quit()


