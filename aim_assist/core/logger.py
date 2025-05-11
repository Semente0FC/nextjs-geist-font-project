from loguru import logger
import sys

def setup_logger(log_file: str = "aim_assist.log"):
    logger.remove()
    logger.add(sys.stdout, colorize=True, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <level>{message}</level>")
    logger.add(log_file, rotation="10 MB", retention="10 days", compression="zip", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")
    return logger
