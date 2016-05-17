import re
from xlrd import open_workbook
source = open('worldnewsdat_scored.txt', 'r')
wb = open_workbook('Offensive Labeling.xlsx')
out = open('worldnewsdat_scored_ffa.txt', 'w')
n = 1
for s in wb.sheets():
	for line in source:
		out.write(line)
		if 'ID:' in line:
			# print n
			score = s.cell(n,1).value
			out.write('\n')
			out.write('Offensive Score:' + str(score) + '\n')
			n += 1
source.close
# wb.close
out.close