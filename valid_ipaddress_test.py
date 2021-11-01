import unittest
from validate_ipaddress import *
class validate_ipaddress_test(unittest.TestCase):
    def test_valid_ipaddress(self):
        self.assertEqual(check_valid_ip_address("10.0.0.0"),'classA')
        self.assertEqual(check_valid_ip_address("10.0.0.1"),'classA')
        self.assertEqual(check_valid_ip_address("192.168.1.20"),'classC')
        self.assertEqual(check_valid_ip_address("192.168.1.9"),'classC')
        self.assertEqual(check_valid_ip_address("192.168.1.10"),'classC')
        self.assertEqual(check_valid_ip_address("172.31.0.0"),'classB')


    def test_invalid_ipaddress(self):
        self.assertEqual(check_valid_ip_address("10.0.0.300"),'Given Ip address 10.0.0.300 is not valid')
        self.assertEqual(check_valid_ip_address("10.260.10.3000"),'Given Ip address 10.260.10.3000 is not valid')


if __name__=='__main__':
    unittest.main()