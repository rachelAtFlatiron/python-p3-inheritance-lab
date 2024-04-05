#!/usr/bin/env python

from user import User

class Student(User):
    
    #we are overriding User's __init__
    #we have to let our init know to include user
    def __init__(self, user_first_name, user_last_name):
        super().__init__(user_first_name=user_first_name, user_last_name=user_last_name)
        #not related to Teacher's self.knowledge
        self.knowledge = []

    def learn(self, topic):
        self.knowledge.append(topic)

#import ipdb; ipdb.set_trace()