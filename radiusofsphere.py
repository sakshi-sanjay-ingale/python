pi=22/7
r=float(input('radius of sphere'))
sur_area=4*pi*r**2
volume=(4/3)*(pi*r**3)
print("surface area",sur_area)
print("volume",volume)


def areaCube(a):
    return(a*a*a)
def surfaceCube(a):
    return(6*a*a)
 
a=5
print("area:",areaCube(a))
print("surface area",surfaceCube(a)) 