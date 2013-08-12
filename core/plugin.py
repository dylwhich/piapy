# Copyright (C) 2013 Alexander Bauer, Dylan Whichard, and contributors;
# (GPLv3) see LICENSE.


# Event is the class which Plugins should know how to process, and
# extend if need be.
class Event:

    def __init__(self, name = None, payload = None):
        self.name = name
        self.payload = payload


# Plugin is a generic class which all plugins to piapy should either use
# or extend.
class Plugin:
    
    def __init__(self, name = None, events = []):
        self.name = name
        self.events = events
    
    def handle(self, event):
        pass
