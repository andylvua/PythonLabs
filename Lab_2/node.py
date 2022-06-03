class Node:
    def __init__(self, model: str, device_type: str, manufacture_year: int, measurement_limit: int) -> None:
        """
        Called when an instance of the class is created.
        It initializes all the variables in Node class and sets them to the given values.

        :param self: Refer to the instance of the class
        :param model: str: Set the model attribute of the instance
        :param device_type: str: Set the device_type attribute of the instance
        :param manufacture_year: int: Set the manufacture_year of the device
        :param measurement_limit: int: Set the measurement limit for this device
        :return: The object that was created
        """
        self.model = model
        self.device_type = device_type
        self.manufacture_year = manufacture_year
        self.measurement_limit = measurement_limit
        self.next = None

    def __str__(self) -> str:
        """
        Called when an instance of the class is printed.
        It returns a string representation of the object.

        :param self: Refer to the object itself
        :return: A string containing the information about object
        """
        return f"Device type: {self.device_type} \n" \
               f"Model: {self.model} \n" \
               f"Date of manufacture: {self.manufacture_year} \n" \
               f"Measurement limit: {self.measurement_limit} \n"
