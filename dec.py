import logging

logging.basicConfig(filename='app.log',level=logging.INFO)
logger = logging.getLogger(__name__)

def check_type(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not (type(arg) == int or type(arg) == float):
                logging.error("One of the args is not a number")
                raise TypeError("one of the args are not a number")
        return func(*args, **kwargs)
    return wrapper
    

@check_type
def add(num1,num2):
    logging.info("Executing add function with arguments: %s, %s", num1, num2)
    return num1 + num2

@check_type
def sub(num1,num2):
    logging.info("Executing sub function with arguments: %s, %s", num1, num2)
    return num1 - num2

@check_type
def multi(num1,num2):
    logging.info("Executing multi function with arguments: %s, %s", num1, num2)
    return num1 * num2
    

if __name__ == '__main__':
    print(add(1, 'b'))