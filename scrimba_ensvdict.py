keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'
keys = keys.split()
values = values.split()
print(keys,values)
en_sv_dict = dict(zip(keys,values))
print(en_sv_dict)
new_dict = {key:value for key,value in zip(keys,values)}
print(new_dict)
en,sv = list(en_sv_dict.keys()),list(en_sv_dict.values())
print(en,sv)
en1,sv1 = zip(*en_sv_dict.items())
print(en1,sv1)
