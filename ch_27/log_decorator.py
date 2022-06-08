import logging

def log(func):
    """Log the function."""
    def wrapper(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # add logging formatter and file handler.
        logging_formatter(logger, name)

        logger.info(f'Running function: {name}')
        logger.info(f'{args} {kwargs}')
        result = func(*args, **kwargs)
        logger.info(f'Result: {result}')
        return result
    return wrapper

def logging_formatter(logger, name):
    """Format logger and add file handler"""

    fh = logging.FileHandler(f"{name}.log")
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

@log
def treble(a):
    return  a * 3

if __name__ == '__main__':
    treble(5)