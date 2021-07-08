





z=0
list = [["Delafontaine", "Jean", "01/06/1991", "h", 4, 25, 1], ["Sarkozy", "Nicolas", "01/07/1991", "h", 6, 32, 2], ["Mouse", "Mickey", "01/08/1991", "h", 0, 21, 3], ["Éléphant", "Babar", "01/09/1991", "h", 0, 14, 4], ["Bond", "James", "01/10/1991", "h", 0, 85, 5], ["Neige", "Anna", "01/11/1991", "f", 0, 66, 6], ["Baba", "Ali", "01/12/1991", "h", 0, 47, 7], ["Ourson", "Winnie", "01/01/1991", "h", 0, 48, 8]]

for i in list:
	a = list[z].pop(4)
	list[z].insert(4,1 + a)
	z +=1
print(list)