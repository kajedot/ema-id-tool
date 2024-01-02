from iso3166 import countries
from src.ema_id_tool import check_digit_calc
from src.ema_id_tool.exceptions import ValidatorException


def validate_alpha_numeric(string: str) -> bool:
    for char in string:
        if char not in check_digit_calc.list_alpha:
            raise ValidatorException(
                f"provided string {string} is not an alpha-numeric string (does not have an appropriate key in the "
                f"decode matrix)")
    return True


def validate_country(country: str) -> bool:
    if len(country) != 2:
        raise ValidatorException(f"country code {country} length is other than 2. ")

    if country not in countries:
        raise ValidatorException(f"country code {country} is not a valid ISO-3166-1 code. ")

    return True


def validate_provider_id(provider_id: str) -> bool:
    if len(provider_id) != 3:
        raise ValidatorException(f"provider id {provider_id} length is other than 3. ")

    return validate_alpha_numeric(provider_id)


def validate_id_type(id_type: str) -> bool:
    if id_type != 'C':
        raise ValidatorException(f"id_type cannot be other than C (provided {id_type}). ")

    return True


def validate_ema_instance(ema_instance: str) -> bool:
    if len(ema_instance) != 8 and validate_alpha_numeric(ema_instance):
        raise ValidatorException(f"ema_instance {ema_instance} length is other than 8. ")

    return validate_alpha_numeric(ema_instance)
