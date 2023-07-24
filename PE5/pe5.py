def multi_table(): # From PE2
	multi_table = [["X"] + [str(i) for i in range(1, 13)]]
	for i in range(1, 13):
		row = [str(i)]
		for j in range(1, 13):
			row.append(str(i * j))
		multi_table.append(row)
	return multi_table