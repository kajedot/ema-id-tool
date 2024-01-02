import unittest
from src.ema_id_tool import ema_id
from src.ema_id_tool.exceptions import EmaIDException
from src.ema_id_tool.exceptions import ValidatorException


class TestEmaID(unittest.TestCase):

    def setUp(self):
        pass

    def test_init_fields(self):
        eid = ema_id.EmaID(country_code='NL', provider_id='XYZ', id_type='C', ema_instance='3KD88D0N')
        self.assertEqual(eid.get_check_digit(), 'Y')
        self.assertEqual(eid.get_full_id(), 'NLXYZC3KD88D0NY')
        self.assertEqual(eid.get_full_id_with_dashes(), 'NL-XYZ-C3KD88D0N-Y')

    def test_init(self):
        valid_ids = {"NLXYZC3KD88D0NY", "PL123CBCDEFGHIY", "FRXYZC23456789A", "ITA1BCC3E4F5G6F",
                          "ESZU8COX834H1DF", "PT739C2837ABCZM", "DE83DCIEN83QGZV", "DE83DCIEN83ZGQ4"}

        for item in valid_ids:
            eid = ema_id.EmaID(ema_id=item[:14])
            self.assertEqual(eid.get_check_digit(), item[-1])
            self.assertEqual(eid.get_full_id(), item)
            self.assertEqual(eid.get_full_id_with_dashes(), f"{item[:2]}-{item[2:5]}-{item[5:14]}-{item[14:15]}")

    def test_init_dashes(self):
        valid_ids = {"NL-XYZ-C3KD88D0N-Y", "PL-123-CBCDEFGHI-Y", "FR-XYZ-C23456789-A", "IT-A1B-CC3E4F5G6-F",
                          "ES-ZU8-COX834H1D-F", "PT-739-C2837ABCZ-M", "DE-83D-CIEN83QGZ-V", "DE-83D-CIEN83ZGQ-4"}

        for item in valid_ids:
            eid = ema_id.EmaID(ema_id=item[:16])
            self.assertEqual(eid.get_check_digit(), item[-1])
            self.assertEqual(eid.get_full_id(), item.replace('-', ''))
            self.assertEqual(eid.get_full_id_with_dashes(), item)

    def test_id_wrong_country(self):
        with self.assertRaises(ValidatorException):
            ema_id.EmaID(ema_id='NNXYZC3KD88D0N')

        with self.assertRaises(ValidatorException):
            ema_id.EmaID(country_code='NN', provider_id='XYZ', id_type='C', ema_instance='3KD88D0N')

    def test_id_too_short(self):
        with self.assertRaises(EmaIDException):
            ema_id.EmaID(ema_id='NLXYZC3KD0XN')

    def test_id_too_long(self):
        with self.assertRaises(EmaIDException):
            ema_id.EmaID(ema_id='NLXYZC3KD88D0XN')

    def test_wrong_id_type(self):
        with self.assertRaises(ValidatorException):
            ema_id.EmaID(country_code='NL', provider_id='XYZ', id_type='X', ema_instance='3KD88D0N')

        with self.assertRaises(ValidatorException):
            ema_id.EmaID(ema_id='NLXYZX3KD88D0N')

    def test_right_id_type(self):
        emid = ema_id.EmaID(country_code='NL', provider_id='XYZ', id_type='C', ema_instance='3KD88D0N')
        self.assertEqual(emid.id_type, 'C')

    def test_id_to_attributes(self):
        true_res = {
            "country_code": 'NL',
            "provider_id": 'XYZ',
            "id_type": 'C',
            "ema_instance": '3KD88D0N'
        }
        res = ema_id.EmaID.id_to_attributes("NLXYZC3KD88D0N")

        self.assertEqual(res, true_res)
