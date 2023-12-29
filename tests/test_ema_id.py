import unittest
from src.ema_id_tool import ema_id


class TestEmaID(unittest.TestCase):

    def setUp(self):
        pass

    def test_fields_init(self):
        eid = ema_id.EmaID(country_code='NL', provider_id='XYZ', id_type='C', ema_instance='3KD88D0N')
        self.assertEqual(eid.get_check_digit(), 'Y')
        self.assertEqual(eid.get_full_id(), 'NLXYZC3KD88D0NY')
        self.assertEqual(eid.get_full_id_with_dashes(), 'NL-XYZ-C3KD88D0N-Y')

    def test_full_id_init(self):
        eid = ema_id.EmaID(ema_id='NLXYZC3KD88D0N')
        self.assertEqual(eid.get_check_digit(), 'Y')
        self.assertEqual(eid.get_full_id(), 'NLXYZC3KD88D0NY')
        self.assertEqual(eid.get_full_id_with_dashes(), 'NL-XYZ-C3KD88D0N-Y')
