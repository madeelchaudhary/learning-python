
from datetime import datetime
from utils.helpers import sum, diff


def log(message):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(
        f"Log: {message} at {date} and sum is {sum(1, 2)} and diff is {diff(1, 2)}")
