#!/usr/bin/python
import time
import watchdog.observers
import watchdog.events
import datetime


class WatchdogHandlers(watchdog.events.FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.xlsx'):
            now = datetime.datetime.now().strftime('%H:%M:%S')
            print(f' {now}: running...')


if __name__ == "__main__":
    watchdogHandler = WatchdogHandlers()
    watchdogObserver = watchdog.observers.Observer()
    watchdogObserver.schedule(watchdogHandler, path='..', recursive=False)
    watchdogObserver.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        watchdogObserver.stop()
    watchdogObserver.join()
