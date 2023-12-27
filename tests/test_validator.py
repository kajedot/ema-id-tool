import unittest
import string
from src.ema_id_tool import validator
from src.ema_id_tool.exceptions import ValidatorException


class TestValidator(unittest.TestCase):

    def test_check_alpha_numeric(self):
        true_positives = string.ascii_uppercase + string.digits
        true_negatives = string.ascii_lowercase + string.punctuation

        for letter in true_positives:
            self.assertTrue(validator.validate_alpha_numeric(letter))

        for digit in true_negatives:
            with self.assertRaises(ValidatorException):
                validator.validate_alpha_numeric(digit)

    def test_validate_country(self):
        true_positives = ['PL', 'NL', 'GB', 'BE', 'DE', 'FR']
        true_negatives_length = ['POL', 'NLD', '', ' ', 'AJDBNsd', 'F']
        true_negatives_rand = ['5r', '22', 'XX', '%!']
        true_negatives = true_negatives_length + true_negatives_rand

        for country in true_positives:
            self.assertTrue(validator.validate_country(country))

        for country in true_negatives:
            with self.assertRaises(ValidatorException):
                validator.validate_country(country)

    def test_validate_provider_id(self):
        true_positives = ['CAR', 'BAR', 'BOW', 'COW', '111', 'GO4']
        true_negatives = ['.', '$$', 'D', '^^', 'DFSF', 'Q', '']

        for item in true_positives:
            self.assertTrue(validator.validate_provider_id(item))

        for item in true_negatives:
            with self.assertRaises(ValidatorException):
                validator.validate_provider_id(item)

    def test_validate_id_type(self):
        true_positives = ['C']
        true_negatives = ['X', 'c', 'CC', '67']

        for item in true_positives:
            self.assertTrue(validator.validate_id_type(item))

        for item in true_negatives:
            with self.assertRaises(ValidatorException):
                validator.validate_provider_id(item)

    def test_validate_ema_instance(self):
        true_positives = ['AAAA1234', 'QWERTYUI', '12345678']
        true_negatives = ['!@#$%^&*', '1', 'JHFJD9982', '']

        for item in true_positives:
            self.assertTrue(validator.validate_ema_instance(item))

        for item in true_negatives:
            with self.assertRaises(ValidatorException):
                validator.validate_ema_instance(item)
