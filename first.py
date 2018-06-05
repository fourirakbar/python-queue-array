#!/usr/bin/python

Class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False

    
