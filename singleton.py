class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance


logger1 = Logger()
logger2 = Logger()

assert logger1 is logger2
