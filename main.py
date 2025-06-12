import subprocess
import platform
import os

def __detect_os() -> str:
	os_type = platform.system()
	if os_type == "Windows":
		return os_type
	elif os_type == "Linux":
		try:
			with open("/etc/os-release") as f:
				os_info = f.read().lower()
			if "arch" in os_info:
				return "Arch Linux"
			elif ("debian" or "ubuntu" in os_info):
				return "Debian"
		except FileNotFoundError:
				return "Unknown Linux"
		else:
			return "Unknown OS"

def __join(strarr: list, *strings):
    res = list(strarr)
    res.extend(strings)
    return res

def __call_pip_linux_package_manager() -> str:
	os_name = __detect_os()
	if("Arch" in os_name):
		return "sudo pacman -S python-"
	if("Debian" in os_name):
		return "sudo apt install python-"
def __install_lib(libname: str):
	try:
		subprocess.check_call([sys.executable, "-m", "pip", "install", "faker"])
	except Exception:
		try:
			subprocess.check_call(__join(__call_pip_linux_package_manager(), "faker"))
		except Exception as ignore:
			print("Cant install 'Faker' lib")
			sys.exit(1)

import sys

# Check if here isn't Faker library
try:
	from faker import Faker
except Exception as ignore:
	print("Looks like here isn't required 'Faker' library")
	inst = input("Install it automatically(Yes/No)?: ")
	if inst.lower() == "y" or inst.lower() == "yes":
		__install_lib("Faker")
	else:
		print("bye")
		sys.exit(1)
DEFAULT_COL = 50

fake = Faker()

def safeParseInt(s: str):
	i = -1
	try:
		i = int(s)
	except Exception as ignore:
		i = -1
	return i

def main():
	import time
	start_t = time.time()
	col = -1
	if len(sys.argv) >= 2:
		col = safeParseInt(sys.argv[1])
		if col<0:
			col = -col
		elif col == 0:
			return 0
	else:
		col = DEFAULT_COL

	if("-s" in sys.argv):
		for i in range(0, col):
			print(str(i+1) + ": " + fake.name())
	else:
		for i in range(0, col):
			print(fake.name())

	end_t = time.time()
	print("Generated " + str( col) + " accounts in " + str(int((end_t - start_t) * 1000)) + " millis")

if __name__ == '__main__':
	main()
