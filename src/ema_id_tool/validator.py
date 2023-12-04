from iso3166 import countries


def is_id_valid(ema_id: str) -> bool:
    country_code = ema_id[:2]
    if not is_country_valid(country_code):
        return False



