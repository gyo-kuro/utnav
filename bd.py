from sys import argv

from buildingdir import buildingcodes

script, codename = argv

def executer():
	code = codename.upper()
	return buildingcodes[code]

def main():
	print executer()

if __name__ == "__main__":
	main()