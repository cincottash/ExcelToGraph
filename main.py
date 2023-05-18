import pandas as pd
import matplotlib.pyplot as plt

def main():
	#If sheet_name argument is none, all sheets are read.
	df = pd.read_excel('sample.xlsx')

	xColName = df.columns[0]
	yColName = df.columns[1]

	xValues = []
	yValues = []

	for index, row in df.iterrows():
		print(row[xColName], row[yColName])
		xValues.append(row[xColName])
		yValues.append(row[yColName])

	plt.scatter(xValues, yValues)
	plt.xlabel(xColName, fontsize=12)
	plt.ylabel(yColName, fontsize=12)
	plt.show()
	



if __name__ == '__main__':
	main()