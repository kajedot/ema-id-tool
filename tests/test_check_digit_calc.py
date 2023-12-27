import unittest

from src.ema_id_tool import check_digit_calc


class TestCheckDigitCalc(unittest.TestCase):

    valid_ids_list = {"FRXYZ1234567892", "ITA1B2C3E4F5G64", "ESZU8WOX834H1DR", "PT73902837ABCZZ",
                      "DE83DUIEN83QGZD", "DE83DUIEN83ZGQM"}

    def test_check_digit_calc(self):

        for eid in self.valid_ids_list:
            original_check = eid[-1]
            generated_check = check_digit_calc.generate(eid)
            print(generated_check)

            self.assertEqual(original_check, generated_check)
