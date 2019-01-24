# Import the Canvas class
from canvasapi import Canvas
from Assignment import Assignment
import json
from splinter import Browser
import time
from datetime import datetime, timedelta
import pytz
from lxml import html

with open('config.json') as config_file:
    config = json.load(config_file)

# SequenceMatcher(None, "AP Computer Science A", "AP Comp Sci" ).ratio())

assignments = []
# Canvas API URL
API_URL = config["apiUrl"]
# Canvas API key
API_KEY = config["apiKey"]

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

courses = canvas.get_user(1425).get_courses()

for course in courses:
    for assignment in course.get_assignments():
        date = datetime.strptime(
            assignment.due_at, "%Y-%m-%dT%H:%M:%S%z") - timedelta(days=1)
        utc = pytz.UTC

        now = utc.localize(datetime.now())
        if date >= now:
            assignments.append(Assignment(
                assignment.name, course.name, date, assignment.description))

username = config["username"]
password = config["password"]
b = Browser(driver_name="chrome", headless=False)
b.driver.set_window_size(1400, 900)
b.visit("https://myhomeworkapp.com/login")

# Login
b.fill("username", username)
b.fill("password", password)
b.find_by_value("Sign in").click()

# Get Classes
page = b.html
page = ' '.join(page.split('\n'))
tree = html.fromstring(page)

classes = tree.xpath("//*[@id='main-content']/div[1]/div/ul/li/a/text()")[:7]


for a in assignments:
    b.visit("https://myhomeworkapp.com/home")
    time.sleep(2)
    # if(b.is_text_present("Mark all of your late homework as complete?")):
    #   print("got here")
    #   b.find_by_text("Close").click()

    b.find_by_xpath("//*[@id='main-content']/div[2]/div/a").click()
    b.fill("title", a.name)
    b.fill("due_date", a.dueAt)
    b.fill("additional_info", a.description)

    b.find_by_value("Save").click()
    time.sleep(4)
    print("Added: " + a.name)
