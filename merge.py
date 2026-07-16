items1=input ("Enter key-value pairs for first dictionary(eg.,a 1 b 2):").split()
items2=input ("Enter key-value pairs for secondary dictionary(eg.,b 3 c 4):").split()
dict1={items1[i]:items1[i+1] for i in range (0,len (items1),2)}
dict2={items2[i]:items2[i+1] for i in range (0,len (items2),2)}
merged =dict1.copy()
merged.update(dict2)
print ("Merged dictionary:",merged)

