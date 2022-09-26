def convert(num, unit):

    if unit == "cm":
        print(float(num)*0.39, "inches")
    elif unit == "inch":
        print(float(num)*2.54, "cm")
    elif unit != "cm" or "inch":
        print("Not correct unit!")

if __name__ == "__main__":
        string = input("Adjon meg egy számot és mértékegységet: ")
        seperatedstring = string.split(" ")
        num = seperatedstring[0]
        unit = seperatedstring[1]
        convert(num,unit)





