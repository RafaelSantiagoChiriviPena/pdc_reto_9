from math import pi # importacion de la constante pi 3.1416
if __name__ == "__main__":
    try:
        r1 : float = float(input("Ingrese el radio de la esfera (cm): ")) # ingreso del radio de la esfera
        while r1 < 0: # limitante para el valor
            r1 = float(input("No existen distancias negativas, intentelo de nuevo: ")) # reingreso al cumplirse la condicion de error

        r2 : float = float(input("Ingrese el radio de la base del cono (cm): ")) # ingreso del radio de base para el cono
        while r2 < 0: # limitante para el valor
            r2 = float(input("No existen distancias negativas, intentelo de nuevo: ")) # reingreso al cumplirse la condicion de error

        h : float = float(input("Ingrese la altura del cono (cm): ")) # ingreso de la altura del cono
        while h < 0: # limitante para el valor
            h = float(input("No existen distancias negativas, intentelo de nuevo: ")) # reingreso al cumplirse la condicion de error

        volumen_figura1 = (lambda r1, r2, h : ((4/3) * pi * (r1**3)) + (pi * h * (r2**2))/3) (r1, r2, h) # funcion anonima para el volumen de la figura 

        area_figura1 = (lambda r1, r2, h : 4 * pi * (r1**2) + pi * r2 * (r2 + ((r2**2 + h**2)**0.5))) (r1, r2, h) # funcion anonima para el area superficial de la figura
        
        print(f"A partir de los datos ingresados de: \n {r1} cm de radio para la esfera \n {r2} cm de radio para la base del cono \n {h} cm de altura para el cono")
        print(f"El volumen de la figura es {volumen_figura1} cm ^ 3") # impresion de volumen
        print(f"El area superficial de la figura es {area_figura1} cm ^ 2") # impresion de area
        
    except ValueError:
        print("El valor ingresado no es un numero real")