# Copyright (C) 2013 Alexander Bauer, Dylan Whichard, and contributors;
# (GPLv3) see LICENSE.


# Router is the class which routes Events to the appropriate
# Plugins. It maintains a list of known Plugins and the proper
# routings as determined by each Plugin's events names.
class Router:
    
    def __init__(self):
        self.plugins = []
        self.defaults = []
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
    
    def register_default(self, plugin):
        """Register a plugin that will always be routed to."""
        self.defaults.append(plugin)
    
    
    def route(self, event):
        """Call handle() on all plugins for a given event type."""
        # If the event name has any specific routes, send the event to
        # them, first.
        if event.name in self.routes:
            plugins = self.routes[event.name]
            for plugin in plugins:
                plugin.handle(event)
        
        # If there are any default plugins, send it along to those,
        # too.
        for plugin in self.defaults:
            plugin.handle(event)


def register(plugin):
    r.register(plugin)

def register_default(plugin):
    r.register_default(plugin)

def route(event):
    r.route(event)

r = Router()
