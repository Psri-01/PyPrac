a= [1,2,3,5]
b=[7,8,9]
squared_list=[x**2 for x in a]
print(squared_list)
squared_dict={x:x**2 for x in a if x%2!=0}
print(squared_dict)
parallel_iterators=[(x+y)for(x,y)in zip(a,b)]
nes=[(x,y)for x in a for y in b]
multi=[[10,20,30],[40,50,60],[70,80,90]]
flattened=[x for temp in multi for x in temp]
print(parallel_iterators)
print(nes)
print(flattened)
