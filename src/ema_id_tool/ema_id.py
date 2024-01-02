from src.ema_id_tool import check_digit_calc
from src.ema_id_tool import validator
from src.ema_id_tool.exceptions import EmaIDException


class EmaID:
    """
    You can pass the following eMA ID fields as arguments while initializing an object:

            "country_code": two character country code according to ISO-3166-1,

            "provider_id": three alphanumeric characters,

            "id_type": (not mandatory) character 'C' (const),

            "ema_instance": eight alphanumeric characters,

    You can also pass parameters as one joined string in the eMA ID format,
    with or without dashes (ex. 'FR-XYZ-123456789').

    After initialization of an object, all eMA ID fields are validated and check digit is being generated.

    You can get a check digit with the method get_check_digit.

    You can also get id with check digit at the end using methods: get_full_id or get_full_id_with_dashes.
    """

    def __init__(self, **kwargs: str) -> None:

        if 'ema_id' in kwargs:
            attributes = self.id_to_attributes(kwargs['ema_id'])
        else:
            attributes = kwargs
            if 'id_type' not in kwargs:
                self.id_type = 'C'

        self.country_code = attributes['country_code']
        self.provider_id = attributes['provider_id']
        self.id_type = attributes['id_type']
        self.ema_instance = attributes['ema_instance']

        self.id_no_check = f"{self.country_code}{self.provider_id}" \
                          f"{self.id_type}{self.ema_instance}"

        self.__validate_id()

        self.check_digit = check_digit_calc.generate(self.id_no_check)

    def get_check_digit(self):
        """
        returns a one alpha-numeric char which is a check digit. It was calculated based on parameters provided
        while initializing the EmaID object.
        """
        return self.check_digit

    def get_full_id(self):
        """
        returns the eMA ID with a check digit and without dashes, in the following format:
        <Country Code><Provider ID><ID Type><eMA Instance><Check Digit>
        """
        return self.id_no_check + self.check_digit

    def get_full_id_with_dashes(self):
        """
        returns the eMA ID with a check digit and with dashes, in the following format:
        <Country Code>-<Provider ID>-<ID Type><eMA Instance>-<Check Digit>
        """
        return f"{self.country_code}-{self.provider_id}-{self.id_type}{self.ema_instance}-{self.check_digit}"

    @staticmethod
    def id_to_attributes(ema_id: str):
        ema_id = ema_id.replace('-', '')
        if len(ema_id) == 14:
            attributes = {
                "country_code": ema_id[:2],
                "provider_id": ema_id[2:5],
                "id_type": ema_id[5:6],
                "ema_instance": ema_id[6:14]
            }
        else:
            raise EmaIDException(f"Provided Ema-ID length is wrong "
                                 f"(only 14 characters are supported, excluding dashes)")
        return attributes

    def __set_id_type(self, kwargs: dict):
        if 'id_type' in kwargs:
            self.id_type = kwargs['id_type']
        else:
            self.id_type = 'C'

    def __validate_id(self):
        validator.validate_country(self.country_code)
        validator.validate_provider_id(self.provider_id)
        validator.validate_ema_instance(self.ema_instance)
        validator.validate_id_type(self.id_type)
