## find best goog buy low sell high

fin = file('goog.csv')
goog = []
days = tuple()

for i in fin:
	nug = i.split(',')
	goog.append(nug)



def goog_money(lis):
	n = 1
	del lis[0]
	lis.reverse()
	sell = 0 
	for day in lis:
		buy = float(day[3])
		for i in xrange(30):
			try:
				top = float(lis[i+n][2])
			except IndexError:
				break
			dif = top - buy
			if dif > sell:
				sell = dif
				days = day,lis[i+n]
		n = n+1
	print sell
	print days



goog_money(goog)
