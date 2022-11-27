numlist = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91]
numtolookfor = 70
def binsrch():
    lowest = 0
    highest = len(numlist)
    numofsteps = 0
    found = True
    while lowest <= highest:
        numofsteps += 1
        mid = (lowest+highest)//2
        if numlist[mid]>70:
            highest = lowest-1

        elif numlist[mid]<70:
            lowest = mid+1
        elif numlist[mid] == 70:
            spot = mid
            break
    else:
        found = False

    if found == True:
        print("Lépések száma:",numofsteps)
        print("Alsó érték:", lowest+1)
        print("Felső érték:", highest)
        print("A k értéke:", spot)

    else:
        print("Nincs találat.")


if __name__  ==  "__main__" :
    binsrch()