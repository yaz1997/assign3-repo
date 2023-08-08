class ConfigurationManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls, *args, **kwargs)
            # Load configuration settings from file (e.g., config.txt)
            cls._instance.load_configuration()
        return cls._instance

    def load_configuration(self):
        # Implement logic to read configuration settings from a file
        # For demonstration purposes, let's use a dummy configuration dictionary
        self.configuration = {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3",
        }

    def get_configuration(self):
        return self.configuration

# Example usage
if __name__ == "__main__":
    # Accessing the configuration manager instance
    config_manager1 = ConfigurationManager()
    config_manager2 = ConfigurationManager()

    # The same instance is returned for both calls
    print(config_manager1 is config_manager2)  # Output: True

    # Accessing configuration settings
    configuration = config_manager1.get_configuration()
    print(configuration)
