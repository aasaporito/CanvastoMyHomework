from splinter import Browser
import time
import json

with open('config.json') as config_file:
    config = json.load(config_file)

username = config["username"]
password = config["password"]
b = Browser(driver_name="chrome", headless=False)
b.driver.set_window_size(1400, 900)
b.visit("https://myhomeworkapp.com/login")

#Login
b.fill("username", username)
b.fill("password", password)
b.find_by_value("Sign in").click()


i = 0
while i < 3:
	b.visit("https://myhomeworkapp.com/home")
	b.find_by_xpath("//*[@id='main-content']/div[2]/div/a[2]/span").click()
	b.fill("title", "Title Here")
	b.fill("due_date", "1/25/2019")
	
	b.find_by_value("Save").click()
	time.sleep(4)
	i += 1