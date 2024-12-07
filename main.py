from loguru import logger
from src.test_data_creator import TestDataCreator


if __name__ == "__main__":
    logger.info("Start")
    tdc = TestDataCreator()
    tdc.create_test_data()
    logger.info("Finished")
