import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_items(driver):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    driver.get(link)
    driver.implicitly_wait(10)
    button = driver.find_element(By.CSS_SELECTOR, 'form#add_to_basket_form.add-to-basket')
    assert button == driver.find_element(By.CSS_SELECTOR, 'form#add_to_basket_form.add-to-basket')
