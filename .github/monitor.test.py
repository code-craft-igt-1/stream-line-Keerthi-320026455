import unittest
from vital_signs import *


class MonitorTest(unittest.TestCase):
    monitor = vital_signs()
    def test_temperature_ok(self):
        self.assertTrue(self.monitor.is_temperature_ok(100))
        self.assertFalse(self.monitor.is_temperature_ok(90))

    def test_pulse_rate_ok(self):
        self.assertTrue(self.monitor.is_pulse_rate_ok(70))
        self.assertFalse(self.monitor.is_pulse_rate_ok(101))

    def test_spo2_ok(self):
        self.assertTrue(self.monitor.is_spo2_ok(85))
        self.assertFalse(self.monitor.is_spo2_ok(92))


if __name__ == '__main__':
    unittest.main()
