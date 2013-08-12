# Copyright (C) 2013 Alexander Bauer, Dylan Whichard, and contributors;
# (GPLv3) see LICENSE.

from core import router, plugin

# Import everything in the plugins/ directory.
import plugins


# Prepare a notification event.
e = plugin.Event()
e.name = "notification"
e.payload = { "data": "Hello, world.", "error": None }

# Send e to the router
router.route(e)
