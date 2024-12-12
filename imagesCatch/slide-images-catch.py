'''
Author: Sandy
Date: 2024-12-05 13:58:37
LastEditors: Please set LastEditors
LastEditTime: 2024-12-11 20:54:20
Description: 
'''
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import random
import requests
# 创建选项对象
edge_options = Options()
# 设置选项，例如无头模式
#edge_options.add_argument('--headless')
edge_options.add_argument(r'--user-data-dir=C:\Users\sandy\AppData\Local\Microsoft\Edge\User Data')
edge_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 使用webdriver_manager自动管理EdgeDriver
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=edge_options)
# 访问登录页面
driver.get("https://www.zhihu.com/signin"   )  

# 等待密码登录按钮出现并点击
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='root']/div/main/div/div/div/div/div[2]/div/div/div/div/form/div/div[2]"))
    )
    # 使用 ActionChains 模拟鼠标点击
    actions = ActionChains(driver)
    actions.move_to_element(login_button).click().perform()
except Exception as e:
    print("无法找到密码登录按钮:", e)

# 等待用户名输入框出现
try:
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    # 使用 ActionChains 模拟键盘输入
    actions = ActionChains(driver)
    actions.move_to_element(username_input).click().perform()
    actions.send_keys("admin").perform()
except Exception as e:
    print("无法找到用户名输入框:", e)
time.sleep(random.uniform(2, 4))  # 随机等待时间

# 等待密码输入框出现
try:
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    # 使用 ActionChains 模拟键盘输入
    actions = ActionChains(driver)
    actions.move_to_element(password_input).click().perform()
    actions.send_keys("123456").perform()
except Exception as e:
    print("无法找到密码输入框:", e)
time.sleep(random.uniform(2, 4))  # 随机等待时间

# 等待登录按钮出现并点击
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    # 使用 ActionChains 模拟鼠标点击
    actions = ActionChains(driver)
    actions.move_to_element(login_button).click().perform()
except Exception as e:
    print("无法找到登录按钮:", e)

# 等待一段时间，以便登录完成
time.sleep(random.uniform(2, 4))  # 随机等待时间
for i in range(100):
    bigImage = driver.find_element(By.CLASS_NAME, "yidun_bg-img")
    image_url = bigImage.get_attribute('src')
    response = requests.get(image_url)
    if response.status_code == 200:
        # 指定保存图片的路径和文件名
        directory = r'D:\SlideMatchByYolo\imagesCatch\images'  # 替换为你的目录路径
        filename = 'pic'+str(i)+'.jpg'    # 替换为你想要的文件名
        filepath = os.path.join(directory, filename)
        # 将图片内容写入指定路径的文件
        with open(filepath, 'wb') as f:
            f.write(response.content)
            print(f"图片已保存到: {filepath}")
        #刷新验证码图片
        freshButton=WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[12]"))
        ) 
        actions = ActionChains(driver)
        actions.move_to_element(freshButton).click().perform()   
        time.sleep(2)
    else:
        print("图片下载失败，状态码：", response.status_code)
        continue