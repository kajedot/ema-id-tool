import logging

from iso3166 import countries
from src.ema_id_tool import check_digit_calc
from src.ema_id_tool import validator


class EmaID:
    """
    You can pass the following eMA ID fields as arguments while initializing an object:
            "country_code": two character country code according to ISO-3166-1,

            "provider_id": three alphanumeric characters,

            "id_type": (not mandatory) character 'C' (const),

            "ema_instance": eight alphanumeric characters,

    You can also pass parameters as one joined string in the eMA ID format,
    with or without dashes (ex. 'FR-XYZ-123456789-2').
    In the end of the string, you can include 15th character (check digit), but don't have to.

    After initialization of an object, all eMA ID fields are validated.
    If check_digit was not provided, it will be generated.
    """

    def __init__(self, **kwargs: str) -> None:

        if 'ema_id' in kwargs:
            attributes = self.id_to_attributes(kwargs['ema_id'])
        else:
            attributes = kwargs

        self.country_code = attributes['country_code']
        self.provider_id = attributes['provider_id']

        if 'id_type' in attributes:
            if validator.validate_id_type(attributes['id_type']):
                self.id_type = attributes['id_type']
        else:
            self.id_type = 'C'

        self.ema_instance = attributes['ema_instance']

        self.id_no_check = f"{self.country_code}{self.provider_id}" \
                          f"{self.id_type}{self.ema_instance}"

        if not self.__validate_id():
            Exception(f"Ema-ID validator: Ema-ID {self.id_no_check} (without check digit) is invalid")

        self.check_dg = check_digit_calc.generate(self.id_no_check)

    def get_check_digit(self):
        return self.check_dg

    def get_full_id(self):
        """
        returns eMA ID with a check digit and without dashes, in the following format:
        <Country Code><Provider ID><ID Type><eMA Instance><Check Digit>
        """
        return self.id_no_check + self.check_dg

    def get_full_id_with_dashes(self):
        """
        returns eMA ID with a check digit and with dashes, in the following format:
        <Country Code>-<Provider ID>-<ID Type><eMA Instance>-<Check Digit>
        """
        return f"{self.country_code}-{self.provider_id}-{self.id_type}{self.ema_instance}-{self.check_dg}"

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
            Exception(f"Ema-ID validator: Provided Ema-ID length is wrong (only 14 characters are supported)")

        return attributes

    def __set_id_type(self, kwargs: dict):
        if 'id_type' in kwargs:
            self.id_type = kwargs['id_type']
        else:
            self.id_type = 'C'

    def __validate_id(self):
        valid = True
        if not validator.validate_country(self.country_code):
            valid = False
        if not validator.validate_provider_id(self.provider_id):
            valid = False
        if not validator.validate_ema_instance(self.ema_instance):
            valid = False

        if not valid:
            return False
        else:
            return True

    def __attributes_to_id(self) -> str:
        return f"{self.country_code}{self.provider_id}" \
               f"{self.id_type}{self.ema_instance}{self.check_dg}"
