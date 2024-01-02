class ValidatorException(Exception):
    def __init__(self, message):
        super().__init__("Ema-ID validator: " + message)


class EmaIDException(Exception):
    def __init__(self, message):
        super().__init__("EmaID class exception: " + message)
