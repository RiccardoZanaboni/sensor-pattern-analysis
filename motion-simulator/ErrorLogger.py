import logging


class ErrorLogger:
    """
    It uses the python module logging to trace the errors of the sensors during the simulation,
    and it saves them in the 'simulator.log' file.

    """

    def __init__(self):
        self._sensor_err_msg = "SENSOR ERROR : "
        logging.basicConfig(level=logging.INFO, filename="simulator.log", filemode="w",
                            format='%(levelname)s - %(message)s')

    def log_sensor_error(self, room_name, timestamp):
        """
        It logs the errors of the sensors during the simulation.

        :param room_name: the name of the room in which the sensor fails
        :param timestamp: the time of the sensor failure
        :return:
        
        """
        message = self._sensor_err_msg+room_name+"\t"+str(timestamp)
        logging.info(message)
