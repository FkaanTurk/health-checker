import time
from checker import Healtchecker
from messenger import Messenger
import config


def healthchecker_job_handler():
    messenger = Messenger()
    hc = Healtchecker(urls=config.URLS_TO_CHECK)
    hc.run_all()

    if len(hc.fails) > 0:
        fail_list = "\n".join(hc.fails)
        message = f"Some url(s) has failed!\n\nDetails: \n{fail_list}"
        messenger.send_message(message=message)


def healtchecker_start():
    while True:
        healthchecker_job_handler()

        # Wait for the interval
        print(f'Sleeping for {config.CHECK_INTERVAL} seconds...')
        time.sleep(config.CHECK_INTERVAL)
