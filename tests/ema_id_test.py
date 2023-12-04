import unittest
import logging
from src.ema_id_tool import check_digit_calc
from src.ema_id_tool import main
from src.ema_id_tool import validator
from src.ema_id_tool import ema_id

ids_list = {"NN123ABCDEFGHIT", "FRXYZ1234567892", "ITA1B2C3E4F5G64", "ESZU8WOX834H1DR", "PT73902837ABCZZ", "DE83DUIEN83QGZD", "DE83DUIEN83ZGQM"}
'''
 (EMA-ID, Country code validity, )
'''

logging.basicConfig(level=logging.INFO)


class TestEmaId(unittest.TestCase):

    def test_digit_generation(self):

        for id in ids_list:

            check = id[-1]
            gen_check = check_digit.generate(id)

            logging.info(f"ID: {id}")
            logging.info(f"Check digit: {check}")
            logging.info(f"Generated check digit: {gen_check}")

            self.assertEqual(gen_check, check)

    def test_country_validation(self):
        for id_tuple in ids_country_valid:
            country = id_tuple[0][:2]
            validation_result = validator.is_country_valid(country)

            logging.info(f"ID, country code validity: {id_tuple}")
            logging.info(f"Country code: {country}")
            logging.info(f"Validation result: {validation_result}")

            self.assertEqual(validation_result, id_tuple[1])

