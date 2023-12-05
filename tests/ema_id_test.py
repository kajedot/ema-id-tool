import unittest
import logging
from src.ema_id_tool import check_digit_calc
from src.ema_id_tool import main
from src.ema_id_tool import validator
from src.ema_id_tool import ema_id

'''
 (EMA-ID, Country code validity, )
'''

logging.basicConfig(level=logging.INFO)


class TestEmaId(unittest.TestCase):
    ids_list = {"NN123ABCDEFGHIT", "FRXYZ1234567892", "ITA1B2C3E4F5G64", "ESZU8WOX834H1DR", "PT73902837ABCZZ",
                "DE83DUIEN83QGZD", "DE83DUIEN83ZGQX"} # TODO CHECK DIGIT VALID

    test_data = [
        [
            {
                "country_code": 'DE',
                "provider_id": '83D',
                "id_type": 'U',
                "ema_instance": 'IEN83QGZ',
            },
            {
                'valid_check_digit': 'D',
            },
        ],
        [
            {
                "country_code": 'DE',
                "provider_id": '83D',
                "id_type": 'C',
                "ema_instance": 'IEN83QGZ',
            },
            {
                'valid_check_digit': 'V',
            },
        ],
        [
            {
                'ema_id': "DE83DUIEN83QGZD"
            },
            {
                'valid_check_digit': 'D',
            },
        ],
    ]

    def test_digit_generation(self):

        for test in self.test_data:

            valid_check = test[1]['valid_check_digit']
            my_ema_id = ema_id.EmaID(**test[0])
            generated_check = my_ema_id.get_check_digit()

            logging.info(f"Data: {test[0]}")
            logging.info(f"Check digit: {valid_check}")
            logging.info(f"Generated check digit: {generated_check}")

            self.assertEqual(generated_check, valid_check)

    def test_country_validation(self):
        for id_tuple in ids_country_valid:
            country = id_tuple[0][:2]
            validation_result = validator.is_country_valid(country)

            logging.info(f"ID, country code validity: {id_tuple}")
            logging.info(f"Country code: {country}")
            logging.info(f"Validation result: {validation_result}")

            self.assertEqual(validation_result, id_tuple[1])

    def test_validate_all_dict(self):
        for obj in self.test_data:
            id = ema_id.EmaID(**obj)
            print(id.get_check_digit())

    def test_validate_all_str(self):
        for obj in self.ids_list:
            id = ema_id.EmaID(ema_id=obj)
            print(id.get_check_digit())
