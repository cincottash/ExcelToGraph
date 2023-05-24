import pandas as pd
import matplotlib.pyplot as plt
from setup import *

def main():

	excelFileName = setup()
	try:
		df = pd.read_excel(excelFileName + '.xlsx')

	except FileNotFoundError:
		print(f'Error: File {excelFileName}.xlsx not found')
		exit(0)

	print()

	xValues = []
	yValues = []

	for index, row in df.iterrows():
		print(row[df.columns[0]], row[df.columns[1]])
		xValues.append(row[df.columns[0]])
		yValues.append(row[df.columns[1]])

	plt.scatter(xValues, yValues)
	plt.xlabel(df.columns[0], fontsize=12)
	plt.ylabel(df.columns[1], fontsize=12)
	#plt.show()
	plt.savefig(f'{excelFileName}.png')
	



if __name__ == '__main__':
	main()