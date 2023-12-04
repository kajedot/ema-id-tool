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

        self.id_str = attributes_to_id(attributes_dictionary)

    def validate_id(self):
        valid = True
        if not self.validate_country(self.country_code):
            valid = False
        if not self.validate_provider_id(self.provider_id)
            valid = False
        if not self.validate_id_type(self.id_type)
            valid = False
        if not self.validate_ema_instance(self.ema_instance)
            valid = False
        if not self.validate_check_digit(self.check_dg):
            valid = False

        if not valid:
            logging.ERROR(f"Ema-ID validator: Ema-ID {self.id_str} is invalid")
            return False
        else:
            logging.INFO(f"Ema-ID validator: Ema-ID {self.id_str} has been validated and is correct")
            return True

    @staticmethod
    def validate_country(country: str) -> bool:
        if len(country) != 2:
            logging.ERROR(f"Ema-ID validator: country code {country} length is other than 2. ")
            return False
        try:
            countries.get(country)
        except KeyError:
            logging.ERROR(f"Ema-ID validator: country code {country} is not a valid ISO-3166-1 code")
            return False
        else:
            return True

    @staticmethod
    def validate_provider_id(provider_id: str) -> bool:
        if len(provider_id) != 3:
            logging.ERROR(f"Ema-ID validator: provider id {provider_id} length is other than 2. ")
            return False
        elif not check_alpha_numeric(provider_id):
            return False
        else:
            return True

    @staticmethod
    def validate_id_type(id_type: str) -> bool:
        if id_type != 'C'
            logging.ERROR(f"Ema-ID validator: only id type C is allowed, provided {provider_id}. ")
            return False
        else:
            return True

    @staticmethod
    def validate_ema_instance(ema_instance: str) -> bool:
        if len(ema_instance) != 8:
            logging.ERROR(f"Ema-ID validator: ema_instance {ema_instance} length is other than 8. ")
            return False
        elif not check_alpha_numeric(ema_instance):
            return False
        else:
            return True

    @staticmethod
    def validate_check_digit(id: str, digit: str)
        if len(digit) != 1:
            logging.ERROR(f"Ema-ID validator: check digit {digit} length is other than 1. ")
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

    @staticmethod
    def check_alpha_numeric(string: str) -> bool:
        for char in string:
            try:
                check_digit_calc.list_alpha[char]
            except KeyError:
                logging.ERROR(f"Ema-ID validator: provided string {str} is not an alpha-numeric string "
                              f"(does not have an appropriate key in the decode matrix)")
                return False
        return True

