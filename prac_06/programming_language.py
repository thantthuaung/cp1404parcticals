"""
programming_language.py
Estimate: 20 minutes
Actual:   24 minutes
"""


class ProgrammingLanguage:
    def __init__(self, language_name, typing, reflection, year):
        self.language_name = language_name
        self.typing = typing
        self.reflection = reflection
        self.year = year
    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False