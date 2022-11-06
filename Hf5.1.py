if __name__=="__main__":
    szorzotablameret=12
    rendezes='{:>3} {:>6}'+('{:>4}'*(szorzotablameret-1))
    szorzoszamok=list(range(1,szorzotablameret+1))

    print(rendezes.format("", *szorzoszamok))
    print("  :------"+("----"*(szorzotablameret-1)))

    for szam in szorzoszamok:
        output=[str(szam)+":"]
        for szorzo in szorzoszamok:
            output.append(szam*szorzo)
        print(rendezes.format(*output))