import string
with open('hazi.txt', 'r', encoding="UTF-8") as f:
    lines = f.readlines()
    vowels = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
    for i in range(len(lines)):
        for j in string.punctuation:
            lines[i] = lines[i].replace(j, "")
            lines[i] = lines[i].replace(" ", "")
        for k in vowels:
            lines[i] = lines[i].replace(k, "")
with open("hazi_output.txt", "w", encoding="UTF-8") as hazi_output:
    for i in range(len(lines)):
        if i % 3 == 0 and i != 0 and lines[i] != "\n":
            hazi_output.write(lines[i])