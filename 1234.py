s = input("Söz daxil edin: ")
d={'hərflər':0,'rəqəmlər':0}
a='0123456789'
b = "abcdefghijklmnopqrstuvwxyz"
for i in s:
    if i in a:
        d['rəqəmlər']+=1
    else:
        d['hərflər']+=1
print(d)        

