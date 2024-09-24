import json
import getpass
from napalm import get_network_driver
from napalm.base.exceptions import ConnectAuthError
from napalm.base.exceptions import ConnectTimeoutError

username = input("username:")

password = getpass.getpass("password:")
optional_args = {"secret":"xxxx"}

range1 = range(1,4)
range2= range(10,15)
IP = list(range1)+list(range2)
driver = get_network_driver("ios")
for n in IP:
    ip_address = "10.10.10." + str(n)
    try:
        device = driver(ip_address, username=username, password=password, optional_args=optional_args)
        device.open()
        output = device.get_facts()
        device.close()
        output_2 = json.dumps(output, indent=4)
        output_3 = json.loads(output_2)
        print (f"Model:{output_3['model']}, ip_address: {ip_address}, hostname: {output_3['hostname']}, os_version: {output_3['os_version'].split(',')[1]}" + "\n")
    except ConnectAuthError as authentication:
        print(f"Authentication error {ip_address}, {authentication}")
        continue
    except ConnectTimeoutError as Timeout:
        print(f"Timeout to device {ip_address}, {Timeout}")
        continue
    except Exception as unknown_error:
        print(f"Error {ip_address}, {unknown_error}")
        continue
    
    