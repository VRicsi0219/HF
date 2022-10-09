if __name__=="__main__":
    while True:
        a=(float(input("Enter 'a' value:")))
        b=(float(input("Enter 'b' value:")))
        try:
            print(a/b)
        except ZeroDivisionError:
            print("Division by zero not allowed.")
        finally:
            print("Out of try except blocks.")

