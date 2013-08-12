# Copyright (C) 2013 Alexander Bauer, Dylan Whichard, and contributors;
# (GPLv3) see LICENSE.


# Router is the class which routes Events to the appropriate
# Plugins. It maintains a list of known Plugins and the proper
# routings as determined by each Plugin's events names.
class Router:
    
    def __init__(self):
        self.plugins = []
        self.routes = {}
    
    def register(self, plugin):
        """Register a plugin and routing for its events."""
        self.plugins.append(plugin)
        
        # Add the plugin to each known event's routing list.
        for ev_name in plugin.events:
            # If the event name is already known, then append the
            # plugin. Otherwise, create the list.
            if ev_name in self.routes:
                self.routes[ev_name].append(plugin)
            else:
                self.routes[ev_name] = [ plugin ]
    
    def route(self, event):
        """Call handle() on all plugins for a given event type."""
        if event.name in self.routes:
            plugins = self.routes[event.name]
            for plugin in plugins:
                plugin.handle(event)

def register(plugin):
    r.register(plugin)

def route(event):
    r.route(event)

r = Router()
