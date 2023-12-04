import logging

from iso3166 import countries
from src.ema_id_tool import check_digit_calc


class EmaID:
    '''
    attributes_dictionary = {
            "country_code": ema_id[:2],
            "provider_id": ema_id[2:5],
            "id_type": ema_id[5:6],
            "ema_instance": ema_id[6:14],
            "check_digit": ema_id[14:15]
        }
    '''
    def __init__(self, attributes_dictionary):

        self.country_code = attributes_dictionary['country_code']
        self.provider_id = attributes_dictionary['provider_id']
        self.id_type = attributes_dictionary['id_type']
        self.ema_instance = attributes_dictionary['ema_instance']
        self.check_dg = attributes_dictionary['check_digit']

    def validate_id(self):
        if not self.validate_country(self.country_code):
            logging.ERROR(f"Ema-ID validator: country code {self.country_code} is wrong for ID {self.whole_id}")
            return False
        if not self.validate_check_digit(self.check_dg):
            logging.ERROR(f"Ema-ID validator: check digit {self.check_dg} is wrong for ID {self.whole_id}")
            return False

    @staticmethod
    def validate_country(country: str) -> bool:
        if len(country) != 2:
            return False

        try:
            countries.get(country)
        except KeyError:
            return False
        else:
            return True

    @staticmethod
    def validate_provider_id(provider_id: str) -> bool:
        if len(provider_id) != 3:
            return False
        elif:

        else:
            return True

    @staticmethod
    def validate_id_type(id_type: str) -> bool:
        if id_type != 'C'
            return False
        else:
            return True

    @staticmethod
    def validate_ema_instance(ema_instance: str) -> bool:
        if len(ema_instance) != 8:
            return False
        else:
            return True

    @staticmethod
    def validate_check_digit(id: str, digit: str)
        if len(digit) != 1:
            return False

        generated_digit = check_digit_calc.generate(id)
        if generated_digit == digit:
            return True
        else:
            return False

    @staticmethod
    def id_to_attributes(ema_id: str):
        attributes = {
            "country_code": ema_id[:2],
            "provider_id": ema_id[2:5],
            "id_type": ema_id[5:6],
            "ema_instance": ema_id[6:14],
            "check_digit": ema_id[14:15]
        }
        return attributes

    @staticmethod
    def attributes_to_id(attributes: dict) -> str:
        return f"{attributes['country_code']}{attributes['provider_id']}" \
               f"{attributes['id_type']}{attributes['ema_instance']}{attributes['check_digit']}"

