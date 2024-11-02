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
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.language_name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"
