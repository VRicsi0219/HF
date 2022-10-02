def is_triangle_valid(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

side_a = float(input("Adja meg az a oldal hosszát:"))
side_b = float(input("Adja meg a b oldal hosszát:"))
side_c = float(input("Adja meg a c oldal hosszát:"))

if is_triangle_valid(side_a, side_b, side_c):
    print("A", side_a, side_b, side_c, "oldalú háromszög szerkeszthető.")
else:
    print("A", side_a, side_b, side_c, "oldalú háromszög nem szerkeszthető.")
