from buildingdir import buildingcodes

def executer():
	flag = 0
	while flag == 0:
		codename = str(raw_input("Enter code (Type ZZ to deactivate): "))
		code = codename.upper()
		if code == "ZZ":
			flag = 1
		else:
			print buildingcodes[code]

def main():
	executer()

if __name__ == "__main__":
	main()