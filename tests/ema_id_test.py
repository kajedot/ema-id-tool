import unittest
import logging

from src.ema_id_tool import ema_id

'''
 (EMA-ID, Country code validity, )
'''

logging.basicConfig(level=logging.INFO)


class TestEmaId(unittest.TestCase):
    valid_ids_list = {"FRXYZ1234567892", "ITA1B2C3E4F5G64", "ESZU8WOX834H1DR", "PT73902837ABCZZ",
                "DE83DUIEN83QGZD", "DE83DUIEN83ZGQM"}



'''
def test_digit_generation(self):

    for test in self.digit_generation_data:

        valid_check = test[1]['valid_check_digit']
        my_ema_id = ema_id.EmaID(**test[0])
        generated_check = my_ema_id.get_check_digit()

        logging.info(f"Data: {test[0]}")
        logging.info(f"Check digit: {valid_check}")
        logging.info(f"Generated check digit: {generated_check}")

        self.assertEqual(generated_check, valid_check)



digit_generation_data = [
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
            'ema_id': "DE83DCIEN83QGZV"
        },
        {
            'valid_check_digit': 'V',
        },
    ],
]

wrong_check_digit_data = [
        {
            "country_code": 'DE',
            "provider_id": '83D',
            "id_type": 'C',
            "ema_instance": 'IEN83QG',
            "check_digit": 'X'
        },
        {
            'ema_id': "DE83DCIEN83QGZV"
        }
] '''
