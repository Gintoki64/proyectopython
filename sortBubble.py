
lista=[9,8,7,6,5,4,3]
m= len(lista)
for x in range(m-1):
	for y in range(0, m-x-1):
		if lista[y] > lista[y+1]:
			lista[y], lista[y+1] = lista[y+1], lista[y]
print(lista)




