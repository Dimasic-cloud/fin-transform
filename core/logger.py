# creating and initialization logger for logging logs


import logging
import logging.handlers
import os


# creating logger for his further setting
logger = logging.getLogger(__name__)

# checking for folder
parent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'log')
if not os.path.exists(parent_dir):
    os.makedirs(parent_dir, exist_ok=True)

# configure logger for wrighting into file
logger.setLevel(level=logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(
    filename=os.path.join(parent_dir, 'log1.log'),
    maxBytes=1024,
    backupCount=5,
    encoding='utf-8'
)
format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s - %(filename)s - %(lineno)s",
    datefmt="%Y-%m-%d %H.%M.%S"
)

# adding settings to logger
handler.setFormatter(format)
logger.addHandler(handler)

if __name__ == "__main__":
    logger.info("success")