import logging

logging.basicConfig(
    filename="library.log",
    level=logging.DEBUG,
    filemode="w",
    format="%(asctime)s - %(name)s -  %(levelname)s - %(message)s"
)

logger = logging.getLogger("Two sum")

def sum(a, b):
    logger.info("info, ikkta soni yigindisi uchun logger ishladi")
    logger.debug(f"{a}")
    logger.debug(f"{b}")
    logger.info(f"Ikki sonning yigi\'ndisi: {a+b}")
    return a + b

sum(34, 54)