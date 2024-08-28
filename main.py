from concurrent.futures import ProcessPoolExecutor
import asyncio

from handlers import telegram_handler


if __name__ == "__main__":
    # Start the program

    loop = asyncio.new_event_loop()
    tasks = [
        telegram_handler,
    ]
    executor = ProcessPoolExecutor(len(tasks))

    for task in tasks:
        loop.run_in_executor(executor, task)

    loop.run_forever()
