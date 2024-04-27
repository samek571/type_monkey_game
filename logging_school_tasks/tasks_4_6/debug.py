import logging
import threading
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [Thread-%(threadName)s] %(levelname)s %(name)s - %(message)s',
    handlers=[
        RotatingFileHandler('events.log', maxBytes=5000000, backupCount=5),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
