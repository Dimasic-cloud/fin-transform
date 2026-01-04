import logging
import logging.handlers
import os

logger = logging.getLogger(__name__)

folder_name = 'log'
if not os.path.exists(folder_name):
    os.makedirs(folder_name, exist_ok=True)

logger.setLevel(level=logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(
    filename=os.path.join(folder_name, 'log1.log'),
    maxBytes=1024,
    backupCount=5,
    encoding='utf-8'
)
format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s - %(filename)s - %(lineno)s",
    datefmt="%Y-%m-%d %H.%M.%S"
)

handler.setFormatter(format)
logger.addHandler(handler)