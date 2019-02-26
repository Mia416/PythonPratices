import logging

def get_logger(configname, filename):    
    logging.basicConfig(filename=filename, filemode='a',level=logging.DEBUG,format='%(levelname)s  %(asctime)s  %(message)s')    
    return logging
    #logging.warning('is when this event was logged.')
    #logging.debug('This message should go to the log file')
    #logging.info('So should this')
    #logging.warning('And this, too')