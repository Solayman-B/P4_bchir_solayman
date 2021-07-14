from operator import itemgetter

list_of_futures_matchs = [([1, "A"], [2, "B"]), ([3, "C"], [4, "D"]), ([5, "E"], [6, "F"]), ([7, "G"], [8, "H"])]

list_of_played_matchs = [([10, 0], [7, 0]), ([3, 0], [8, 0]), ([2, 0], [1, 0]), ([2, 0], [5, 0]),([2, "B"], [1, "A"])]


def oulah():
	u = -1
	for match_id in list_of_futures_matchs:
		u +=1
		f1 = match_id[0][0]
		f2 = match_id[1][0]
		for match_id2 in list_of_played_matchs:
			p = match_id2[0][0], match_id2[1][0]
			if (f1,f2) == p or (f2, f1) == p:
				w = list_of_futures_matchs.pop(u)
				list_of_futures_matchs.append(w)
				print(w)
				print(w in list_of_played_matchs)
				print(list_of_played_matchs)
				x = list_of_futures_matchs.pop(u)
				w[0][0], x[0][0], w[0][1], x[0][1] = x[0][0], w[0][0], x[0][1], w[0][1]
				list_of_futures_matchs.insert(u, w)
				list_of_futures_matchs.insert(u, x)
				print(list_of_futures_matchs, "futures matchs")
				oulah()

w = list_of_futures_matchs.pop(0)
list_of_futures_matchs.append(w)
print(w)
print(w in list_of_played_matchs)
print(list_of_played_matchs)