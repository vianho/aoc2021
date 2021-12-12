import logging

def get_logger(name='__main__', level='INFO'):
    LOGGER = logging.getLogger(name)
    levels = {
        'CRITICAL' : logging.CRITICAL,
        'ERROR' : logging.ERROR,
        'WARNING' : logging.WARNING,
        'INFO' : logging.INFO,
        'DEBUG' : logging.DEBUG
    }

    logging.basicConfig(
        level=levels[level], 
        format='%(asctime)s - %(levelname)s - %(message)s', 
        datefmt='%d-%b-%y %H:%M:%S', 
        handlers=[
            logging.FileHandler('log.log', 'a', 'utf-8'),
            logging.StreamHandler()
        ]
    )
    LOGGER.debug(f'{name=} - {level=} - {levels[level]=}')
    return LOGGER

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def transform_input(input, to_int=False):
    return list(map(int, input.strip().split('\n'))) if to_int else list(input.strip().split('\n'))
