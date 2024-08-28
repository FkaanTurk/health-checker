from typing import List
import requests
import threading


class Healtchecker:
    def __init__(self, urls: List[str]) -> None:
        self.urls = urls
        self.fails = []

    def check_url(self, url: str) -> int:
        succeed = False
        try:
            response = requests.get(url=url)

            if response.status_code != 200:
                self.fails.append(url)
                return

            succeed = True
        except:  # noqa
            self.fails.append(url)
        finally:
            print(f'Checking url -> {url} [{"Ok" if succeed else "Failed"}]')

    def run_all(self,):
        threads: List[threading.Thread] = []

        for url in self.urls:
            task = threading.Thread(target=self.check_url, args=(url,))
            threads.append(task)
            task.start()

        # wait until the all threads are done!
        for thread in threads:
            thread.join()
