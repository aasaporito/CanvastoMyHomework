# Import the Canvas class
from canvasapi import Canvas
from Assignment import Assignment
import json

with open('config.json') as config_file:
    config = json.load(config_file)

#SequenceMatcher(None, "AP Computer Science A", "AP Comp Sci" ).ratio())

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
		assignments.append(Assignment(assignment.name, course.name, assignment.due_at))



