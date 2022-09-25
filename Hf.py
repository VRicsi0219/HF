string_data=input("Adjon meg egy mondatot:")

d={}
for ch in string_data:
    d[ch]=d.get(ch,0)+1
print("Betűk gyakorisága:",d)





