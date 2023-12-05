import logging

from iso3166 import countries
from src.ema_id_tool import check_digit_calc


class EmaID:
    """
    You can pass the following eMA ID fields as arguments while initializing an object:
            "country_code": two character country code according to ISO-3166-1,

            "provider_id": three alphanumeric characters,

            "id_type": character 'C',

            "ema_instance": eight alphanumeric characters,

            "check_digit" (not mandatory): one alphanumeric character

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
        self.id_type = attributes['id_type']
        self.ema_instance = attributes['ema_instance']

        self.id_no_check = f"{self.country_code}{self.provider_id}" \
                          f"{self.id_type}{self.ema_instance}"

        if not self.validate_id():
            Exception(f"Ema-ID validator: Ema-ID {self.id_no_check} (without check digit) is invalid")

        self.check_dg = self.check_check_digit(attributes)

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

    def check_ema_id(self, kwargs: dict):
        if 'ema_id' in kwargs:
            return self.id_to_attributes(kwargs['ema_id'])
        else:
            return False

    def check_check_digit(self, kwargs: dict) -> str:
        if 'check_digit' not in kwargs:
            return check_digit_calc.generate(self.id_no_check)
        else:
            self.validate_check_digit(self.id_no_check, kwargs['check_digit'])

        return kwargs['check_digit']

    def validate_id(self):
        valid = True
        if not self.validate_country(self.country_code):
            valid = False
        if not self.validate_provider_id(self.provider_id):
            valid = False
        if not self.validate_id_type(self.id_type):
            valid = False
        if not self.validate_ema_instance(self.ema_instance):
            valid = False

        if not valid:
            return False
        else:
            return True

    def validate_provider_id(self, provider_id: str) -> bool:
        if len(provider_id) != 3:
            logging.error(f"Ema-ID validator: provider id {provider_id} length is other than 2. ")
            return False
        else:
            if self.check_alpha_numeric(provider_id):
                return False
            else:
                return True

    def validate_ema_instance(self, ema_instance: str) -> bool:
        if len(ema_instance) != 8:
            logging.error(f"Ema-ID validator: ema_instance {ema_instance} length is other than 8. ")
            return False
        elif not self.check_alpha_numeric(ema_instance):
            return False
        else:
            return True

    def validate_id_type(self, id_type: str) -> bool:
        if self.check_alpha_numeric(id_type): # C or not C?
            return False
        else:
            return True

    @staticmethod
    def validate_country(country: str) -> bool:
        if len(country) != 2:
            logging.error(f"Ema-ID validator: country code {country} length is other than 2. ")
            return False
        try:
            countries.get(country)
        except KeyError:
            logging.error(f"Ema-ID validator: country code {country} is not a valid ISO-3166-1 code. ")
            return False
        else:
            return True

    @staticmethod
    def validate_check_digit(id: str, digit: str):
        if len(digit) != 1:
            logging.error(f"Ema-ID validator: check digit {digit} length is other than 1. ")
            return False

        generated_digit = check_digit_calc.generate(id)
        if generated_digit == digit:
            return True
        else:
            return False

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
        elif len(ema_id) == 15:
            attributes = {
                "country_code": ema_id[:2],
                "provider_id": ema_id[2:5],
                "id_type": ema_id[5:6],
                "ema_instance": ema_id[6:14],
                "check_digit": ema_id[14:15]
            }
        else:
            Exception(f"Ema-ID validator: wrong ema-id length")

        return attributes

    def attributes_to_id(self) -> str:
        return f"{self.country_code}{self.provider_id}" \
               f"{self.id_type}{self.ema_instance}{self.check_dg}"

    @staticmethod
    def check_alpha_numeric(string: str) -> bool:
        for char in string:
            if char not in check_digit_calc.list_alpha:
                logging.error(f"Ema-ID validator: provided string {string} is not an alpha-numeric string "
                              f"(does not have an appropriate key in the decode matrix)")
                return False
        return True

