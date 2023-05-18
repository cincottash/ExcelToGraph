import sys 

def setup():

	try:
		excelFileName = sys.argv[1]
		return excelFileName
	except IndexError:
		print(f'Error: Provide an Excel file to load')
		exit(0)

	