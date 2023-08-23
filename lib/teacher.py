#!/usr/bin/env python

import random

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Teacher(User):
    all_knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]

    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        if knowledge is None:
            knowledge = Teacher.all_knowledge
        self._knowledge = knowledge

    def get_knowledge(self):
        return self._knowledge

    def set_knowledge(self, knowledge):
        if isinstance(knowledge, list):
            self._knowledge = knowledge

    knowledge = property(get_knowledge, set_knowledge)

    def teach(self):
        if self._knowledge:
            return random.choice(self._knowledge)  # Return a random item from knowledge
        else:
            return None

teacher = Teacher('John', 'Doe')
knowledge = teacher.get_knowledge()
print(knowledge)
taught = teacher.teach()
print(taught)
