# ValidIpaddress

Overview
This repository is about validating given ip address and classifying the valid address based on its class. If address is not valid  it returns valueerror message.

Contents of this repository:
1.valid_ipaddress.py
2.valid_ipaddress_test.py

Basic Usage
1. valid_ipaddres.py
This file contains python code to validate the given Ip address and classifies based on the different classes of Ipaddress.
import ipaddress( this module is for inspecting and manipulating ipaddress)
To test the functionality of this file. Run the script "python validate_ipaddress.py"
Example: After running "python validate_ipaddress.py" 
Input address here:192.168.1.20
expected output: classC

2.valid_ipaddress_test.py
This file has the unittest for valid_ipaddress.py file
import unittest (this module helps to run and create unittests)
It has two tests
1.test_valid_ipaddress
2.test_invalid_ipaddress
Script to run the test is 
python -m unittest valid_ipaddress_test.py

Example: After running python -m unittest valid_ipaddress_test.py
Input address here:192.168.1.20
Expected:
Ran 2 tests in 0.054s 
Ok 

