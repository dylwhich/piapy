from core import router, plugin

import pynotify

def notify(event):
    pynotify.Notification(event.payload["summary"],
                          event.payload["body"]).show()


def init():
    pynotify.init("piapy")
    notifier = plugin.Plugin()
    notifier.name = "notifier"
    notifier.events = [ "notification" ]
    notifier.handle = notify
    router.register_default(notifier)

init()
