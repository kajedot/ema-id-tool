import unittest
from src.ema_id_tool import main

ids_list = {"NN123ABCDEFGHIT", "FRXYZ1234567892", "ITA1B2C3E4F5G64", "ESZU8WOX834H1DR", "PT73902837ABCZZ", "DE83DUIEN83QGZD", "DE83DUIEN83ZGQM"}


class TestCheckSum(unittest.TestCase):

    def test_digit_generation(self):

        for id in ids_list:
            without_check = id[:-1]
            check = id[-1]
            gen_check = main.gen_check_digit()
            self.assertEqual(gen_check, check)