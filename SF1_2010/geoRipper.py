import os, sys

f = open('/Users/chogan/Desktop/md2010.sf1/geoFile.csv', 'r')
o = open('/Users/chogan/Desktop/md2010.sf1/minifile.csv','w')
o.write("ISHISBLOCK, logrecno, geoid\n")
rowNum = 0

for row in f.readlines():
	if row.split(',')[21] != " ":
		firstRow = "1"
	else:
		firstRow = "0"

	o.write(firstRow + ", " + row.split(',')[6] + ", " + row.split(',')[9] + row.split(',')[10] + row.split(',')[19] + row.split(',')[20] + row.split(',')[21] + "\n")

f.close()
o.close()