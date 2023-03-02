import os
import logging
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "./logs"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

logger = logging.getLogger("QRBooking")