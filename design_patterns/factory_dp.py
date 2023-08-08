from abc import ABC, abstractmethod

# Logger Interface
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

# File Logger
class FileLogger(Logger):
    def log(self, message):
        with open('logfile.txt', 'a') as file:
            file.write(f"{message}\n")

# Console Logger
class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Console Log: {message}")

# Database Logger
class DatabaseLogger(Logger):
    def log(self, message):
        # Implement database logging logic here
        print(f"Database Log: {message}")

# Logger Factory
class LoggerFactory:
    @staticmethod
    def create_logger(logger_type):
        if logger_type == 'file':
            return FileLogger()
        elif logger_type == 'console':
            return ConsoleLogger()
        elif logger_type == 'database':
            return DatabaseLogger()
        else:
            raise ValueError("Invalid logger type. Supported types: 'file', 'console', 'database'")

# Example usage
if __name__ == "__main__":
    # Factory Design Pattern to create different loggers
    logger1 = LoggerFactory.create_logger('file')
    logger2 = LoggerFactory.create_logger('console')
    logger3 = LoggerFactory.create_logger('database')

    # Logging using different loggers
    logger1.log("This message will be logged to a file.")
    logger2.log("This message will be logged to the console.")
    logger3.log("This message will be logged to the database.")
