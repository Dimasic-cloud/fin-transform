# class for exports data and wrighting it to file

import sys
from pathlib import Path
import os

# setting the parent directory
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.logger import logger
import requests
from dotenv import load_dotenv


# extract env
load_dotenv()


class External:
    def __init__(self, url: str, params: dict):
        """
        initialization with simple checking input data
        """
        self._url = url
        logger.debug("added: %s", self._url)
        self._params = params
        logger.debug(f"added: {self._params}")

    def extract(self):
        """
        extracting data from website
        """
        resp = requests.get(self._url, params=self._params)
        logger.debug(f"respons status: {resp.status_code}")
        data = resp.json()

        # open context for writing to file
        with open('data/raw.json', "a", encoding="UTF-8") as file:
            n = file.write(data)
            logger.debug(f"success! writing data is: {n}")


if __name__ == "__main__":
    params = os.getenv("PARAMS")
    ex = External('https://www.alphavantage.co/query', params)
    logger.debug("created object")
    ex.extract()
    logger.debug("writing data")