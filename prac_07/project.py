import datetime
class Project:
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, percentage=0):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percentage = percentage

    def __lt__(self, other):
        return self.priority < other.priority


    def update_percentage(self, new_percentage):
        self.percentage = new_percentage

    def update_priority(self, new_priority):
        self.priority = new_priority


    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, setimate: ${self.cost_estimate:.2f}, completion: {self.percentage}%"

