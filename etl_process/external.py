# class for exports data and wrighting it to file

import sys
from pathlib import Path

# setting the parent directory
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.logger import logger


class External:
    def __init__(self, url: str, params: dict, api_key: str):
        """
        initialization with simple checking input data
        
        :param self: link to object
        :param url: URL adress to data extraction website
        :param params: dictionary with query parameters
        :param api_key: API key for access data on website
        """
        self._url = self._checking(url)
        self._api_key = self._checking(api_key)
        self._params = self._checking(params)

    def _checking(self, elem):
        """
            checking input data

            :param elem: param for validation
        """
        if elem:
            logger.debug(f"success! {elem} has been correct")
            return elem

        logger.error(f"incorrect data: {elem}")


if __name__ == "__main__":
    ex = External("a", {"a": 1}, "demo")
    logger.info("the object has been created")