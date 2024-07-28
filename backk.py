import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
action = ActionChains(browser)
Episode = sys.argv[1]


browser.get((f'https://www.youtube.com/watch?v=-fo9DYX0_1w&list=PLtNk7av9R5XIaMFcf1AGGZ6t5Qt1NN1Ey&index={Episode}'))
browser.maximize_window()

btn = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[35]/div[2]/div[1]/button")))
btn.click()
btn.click()