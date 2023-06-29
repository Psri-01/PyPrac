string="lollapalooza"
k=[]
for ele in string:
	if ele not in k:
		k.append(ele)
for i in range(0,len(k)):
	print(k[i],end="")
