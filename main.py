from sensor.logger import logging
from sensor.exception import SensorException
import sys, os

def test_loggerandexcetion():
     try:
          logging.info("Start Logging ")
          result = 3/0
          print(result)
          logging.info("Stop Logging ")
     except Exception as e:
          logging.debug(str(e))
          raise SensorException(e, sys)


if __name__ == "__main__":
     try: 
          test_loggerandexcetion()
     except Exception as e:
          print(e)