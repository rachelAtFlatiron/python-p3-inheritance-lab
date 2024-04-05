#!/usr/bin/env python

import ipdb 
from user import User

import random

#default data the README is asking for
teacher_knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):
    #setting default for knowledge param equal to data above
    def __init__(self, user_first_name, user_last_name, knowledge=teacher_knowledge):

        super().__init__(user_first_name=user_first_name, user_last_name=user_last_name)
        
        #not related to Student's self.knowledge
        #setting current instance of teacher's knowledge equal to param
        self.knowledge = knowledge

    def teach(self):
        #randomint(first index, length of array)
        rand_index = random.randint(0, len(self.knowledge) - 1)
        return self.knowledge[rand_index]

#ipdb.set_trace()