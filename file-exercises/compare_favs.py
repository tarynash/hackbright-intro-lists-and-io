f1 = open('taryn_fav_foods.txt')
f2 = open('patrick_fav_foods.txt')

taryn_favs = f1.readlines()
patrick_favs = f2.readlines()

f1.close()
f2.close()

#def compare_favs(fav1, fav2):
#	if fav1 == fav2:
#		return "Our favorite foods are the same!"
#	else:
#		return "our favorite foods are different!"

#print compare_favs(taryn_favs,patrick_favs)

def compare_favs2(fav1, fav2):
	for fav in fav1:
		if fav in fav2:
			print "We both love %s" %fav.strip('/n')

compare_favs2(taryn_favs,patrick_favs)


