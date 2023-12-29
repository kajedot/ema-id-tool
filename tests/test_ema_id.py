import unittest
from src.ema_id_tool import ema_id


class TestEmaID(unittest.TestCase):

    def setUp(self):
        self.fields_init_id = ema_id.EmaID(country_code='NL', provider_id='XYZ', id_type='C', ema_instance='3KD88D0N')

    def test_get_check_digit(self):
        self.assertEqual(self.fields_init_id.get_check_digit(), 'Y')

    def test_get_full_id(self):
        self.assertEqual(self.fields_init_id.get_full_id(), 'NLXYZC3KD88D0NY')

    def test_get_full_id_with_dashes(self):
        self.assertEqual(self.fields_init_id.get_full_id_with_dashes(), 'NL-XYZ-C3KD88D0N-Y')
