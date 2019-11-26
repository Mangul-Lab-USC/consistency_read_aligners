fileName = input("What is the file name?")
samFile = open(fileName, "r")
information = samFile.readlines()
for line in information:
	line = line[:-1]
	linelist = line.split("\t")
	for i in linelist:
		if "NM" in i:
			print(i)
			break
	print("\n")



