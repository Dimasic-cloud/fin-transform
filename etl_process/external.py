# class for exports data and wrighting it to file

from core.logger import logger

class External:
    # initialization with simple checking input data
    def __init__(self, url: str, params: dict, api_key: str):
        if url:
            self.url = url
            logger.info("added url data: %s", self.url)
        else:
            logger.debug("the transmitted data was empty")

        if api_key:
            self.api_key = api_key
            logger.info("added api_key data: %s", self.api_key)
        else:
            logger.debug("the transmitted data was empty")

        if params:
            self.params = params
            logger.info("added list params: %s", self.params)
        else:
            logger.debug("the transmitted data was empty")

if __name__ == "__main__":
    ex = External("a", {"a": 1}, "demo")
    logger.info("the object has been created")