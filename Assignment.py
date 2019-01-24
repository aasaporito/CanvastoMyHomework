from datetime import datetime, timedelta
class Assignment:
    
    def __init__(self, name="No Name", course="", dueAt= "1/1/2019"):
        self.name = name
        self.course = course
        self.dueAt = datetime.strftime(datetime.strptime(dueAt, "%Y-%m-%dT%H:%M:%S%z") - timedelta(days=1), "%m/%d/%Y")
