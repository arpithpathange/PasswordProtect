import logging

class logbase:

    logger = None

    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] - %(message)s',
            filename='filename.txt')  # pass explicit filename here
        self.logger = logging.getLogger()

    def logwarning(self,msg):
        self.logger.warning(msg)

    def logerror(self,msg):
        self.logger.error(msg)

    def loginfo(self,msg):
        self.logger.info(msg)



