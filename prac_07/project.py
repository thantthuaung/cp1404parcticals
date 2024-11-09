class Project:
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percentage = percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, setimate: ${self.cost_estimate:.2f}, completion: {self.percentage}"