import logging


class ErrorLogger:

    def __init__(self):
        self._sensor_err_msg = "SENSOR ERROR : "
        logging.basicConfig(level=logging.INFO, filename="simulator.log", filemode="w",
                            format='%(levelname)s - %(message)s')

    def log_sensor_error(self, sensor_name, timestamp):
        message = self._sensor_err_msg+sensor_name+"\t"+str(timestamp)
        logging.info(message)
