from iso3166 import countries
import logging
from src.ema_id_tool import check_digit_calc


def check_alpha_numeric(string: str) -> bool:
    for char in string:
        if char not in check_digit_calc.list_alpha:
            Exception(f"Ema-ID validator: provided string {string} is not an alpha-numeric string "
                          f"(does not have an appropriate key in the decode matrix)")
            return False
    return True


def validate_country(country: str) -> bool:
    if len(country) != 2:
        Exception(f"Ema-ID validator: country code {country} length is other than 2. ")
        return False
    try:
        countries.get(country)
    except KeyError:
        Exception(f"Ema-ID validator: country code {country} is not a valid ISO-3166-1 code. ")
        return False
    else:
        return True


def validate_provider_id(provider_id: str) -> bool:
    if len(provider_id) != 3:
        Exception(f"Ema-ID validator: provider id {provider_id} length is other than 2. ")
        return False
    else:
        if check_alpha_numeric(provider_id):
            return False
        else:
            return True


def validate_id_type(id_type: str) -> bool:
    if id_type != 'C':
        Exception(f"Ema-ID validator: id_type cannot be other than C (provided {id_type}). ")
        return False
    else:
        return True


def validate_ema_instance(ema_instance: str) -> bool:
    if len(ema_instance) != 8:
        Exception(f"Ema-ID validator: ema_instance {ema_instance} length is other than 8. ")
        return False
    elif not check_alpha_numeric(ema_instance):
        return False
    else:
        return True


def validate_check_digit(id: str, digit: str):
    if len(digit) != 1:
        Exception(f"Ema-ID validator: check digit {digit} length is other than 1. ")
        return False

    generated_digit = check_digit_calc.generate(id)
    if generated_digit == digit:
        return True
    else:
        return False
