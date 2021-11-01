import ipaddress
from ipaddress import IPv4Address,IPv4Network
address_id=input("Input address here:")
classA= IPv4Network(("10.0.0.0","255.0.0.0"))
classB= IPv4Network(("172.16.0.0","255.240.0.0"))
classC= IPv4Network(("192.168.0.0","255.255.0.0"))

def check_valid_ip_address(address_id:str)->str:
    try:
        valid_ip=ipaddress.ip_address(address_id)
        if valid_ip in classA:
            print("classA")
            return "classA"
        if valid_ip in classB:
            print("classB")
            return "classB"
        if valid_ip in classC:
            print("classC")
            return "classC"
    except ValueError:
        print("Given Ip address {} is not valid".format(address_id))
        return "Given Ip address {} is not valid".format(address_id)
check_valid_ip_address(address_id)
