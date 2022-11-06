if __name__ == "__main__":
    string = input("Írj egy stringet: ")
    revstr = string[::-1]
    tobbjegy = ["cs", "dz", "dzs", "gy", "ly", "ny", "sz", "ty", "zs"]
    for betu in tobbjegy:
        revstr = revstr.replace(betu[::-1], betu)
    if revstr == string:
        print("A string egy palindróm.")
    else:
        print("A string nem palindróm.")