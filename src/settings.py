import os

NUMBER_OF_PERSONS = os.getenv("NUMBER_OF_PERSONS")
PRINT = os.getenv("PRINT", "True").lower() == "true"

DATE_FORMAT = "%Y-%m-%d-%H%M%S"
INDATA_DIRECTORY = "indata"
DEFAULT_NUMBER_OF_PERSONS = 10
