from core import router, plugin

import time, json

def log(event):
    timestamp = time.strftime("%c")
    print timestamp, event.name, json.dumps(event.payload, sort_keys=True, separators=(',',':'))


def init():
    logger = plugin.Plugin()
    logger.name = "logger"
    logger.events = [ "notification" ]
    logger.handle = log
    router.register(logger)

init()
