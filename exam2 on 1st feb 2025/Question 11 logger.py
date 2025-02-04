class Logger:
    def log(self, message, type="info"):
        if type == "error":
            print(f"ERROR: {message}")
        elif type == "warning":
            print(f"WARNING: {message}")
        elif type == "info":
            print(f"INFO: {message}")
        else:
            print(f"Unknown type: {message}")
# Create a Logger object
logger = Logger()
# Log different types of messages
logger.log("info message.")  # Default to info
logger.log("error message.", "error")
logger.log("warning message.", "warning")
