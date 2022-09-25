string_data=input("Adjon meg egy mondatot:")

d={}
for ch in string_data:
    d[ch]=d.get(ch,0)+1
print("Betűk gyakorisága:",d)

string_length=len(string_data)
sliced_string=string_data[string_length::-1]
print ("Fordítva:", sliced_string)

split_string=string_data.split( )
print("Listába rendezve szavanként:", split_string)
