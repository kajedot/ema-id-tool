import unittest

from src.ema_id_tool import check_digit_calc


class TestCheckDigitCalc(unittest.TestCase):

    def test_join_digits_matrices(self):
        cases_nr = 2
        true_in = [['AA', 'BB'], ['cc', 'dd']]
        true_out = [['A', 'A', 'B', 'B'], ['c', 'c', 'd', 'd']]

        for n in range(0, cases_nr):
            self.assertEqual(true_out[n],
                             check_digit_calc._join_digits_matrices(true_in[n]))

    def test_digit_to_matrix(self):
        cases_nr = 14
        true_in = ['I', 'T', 'A', '1', 'B', '2', 'C', '3', 'E', '4', 'F', '5', 'G', '6']
        true_out = [(1, 0, 0, 0), (1, 1, 0, 2), (0, 1, 0, 1), (0, 0, 0, 1), (0, 1, 0, 2), (0, 0, 0, 2), (0, 1, 1, 0),
                    (0, 0, 1, 0), (0, 1, 1, 2), (0, 0, 1, 1), (0, 1, 2, 0), (0, 0, 1, 2), (0, 1, 2, 1), (0, 0, 2, 0)]

        for n in range(0, cases_nr):
            self.assertEqual(true_out[n],
                             check_digit_calc._digit_to_matrix(true_in[n]))

    def test_digits_to_matrices(self):
        true_in = 'ITA1B2C3E4F5G6'
        true_out = [(1, 0, 0, 0), (1, 1, 0, 2), (0, 1, 0, 1), (0, 0, 0, 1), (0, 1, 0, 2), (0, 0, 0, 2), (0, 1, 1, 0),
                    (0, 0, 1, 0), (0, 1, 1, 2), (0, 0, 1, 1), (0, 1, 2, 0), (0, 0, 1, 2), (0, 1, 2, 1), (0, 0, 2, 0)]
        self.assertEqual(true_out,
                         check_digit_calc._digits_to_matrices(true_in))

    def test_check_equation(self):
        true_in = [(1, 0, 0, 0), (1, 1, 0, 2), (0, 1, 0, 1), (0, 0, 0, 1), (0, 1, 0, 2), (0, 0, 0, 2), (0, 1, 1, 0),
                    (0, 0, 1, 0), (0, 1, 1, 2), (0, 0, 1, 1), (0, 1, 2, 0), (0, 0, 1, 2), (0, 1, 2, 1), (0, 0, 2, 0)]
        true_out = [0, 0, 1, 2]
        self.assertEqual(true_out,
                         check_digit_calc._check_equation(true_in))

    def test_reverse_digit(self):
        cases_nr = 5
        true_in = [[0, 0, 1, 2], [1, 1, 0, 0], [1, 1, 2, 1], [0, 1, 1, 2], [0, 0, 1, 0]]
        true_out = [20, 3, 43, 22, 32]

        for n in range(0, cases_nr):
            self.assertEqual(true_out[n],
                             check_digit_calc._reverse_digit(true_in[n]))

    def test_decode_reverse(self):
        cases_nr = 5
        true_in = [20, 3, 43, 22, 32]
        true_out = ['4', 'R', 'Z', 'D', '2']

        for n in range(0, cases_nr):
            self.assertEqual(true_out[n],
                             check_digit_calc._decode_reverse(true_in[n]))

    def test_generate(self):
        valid_ids_list = {"FRXYZ1234567892", "ITA1B2C3E4F5G64", "ESZU8WOX834H1DR", "PT73902837ABCZZ",
                          "DE83DUIEN83QGZD", "DE83DUIEN83ZGQM"}
        for eid in valid_ids_list:
            original_check = eid[-1]
            generated_check = check_digit_calc.generate(eid)

            self.assertEqual(original_check, generated_check)
