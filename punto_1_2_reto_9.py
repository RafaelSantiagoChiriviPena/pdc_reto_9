from math import pi # importacion de la constante pi 3.1416
if __name__ == "__main__":
    try:
        r : float = float(input("Ingrese el radio de los circulos (cm): ")) # ingreso del radio para los circulas 
        while r < 0: # limitante para el valor
            r = float(input("No existen distancias negativas, intentelo de nuevo: ")) # reingreso al cumplirse la condicion de error

        a : float = float(input("Ingrese la altura del rectangulo (cm): ")) # ingreso de la altura del rectangulo
        while a < 0: # limitante para el valor
            a = float(input("No existen distancias negativas, intentelo de nuevo: ")) # reingreso al cumplirse la condicion de error

        b : float = float(input("Ingrese la base del rectangulo (cm): ")) # ingreso del ancho del rectangulo
        while b < 0: # limitante para el valor 
            b = float(input("No existen distancias negativas, intentelo de nuevo: ")) # reingreso al cumplirse la condicion de error

        area_figura2 = (lambda r, a, b : 2*(pi * (r**2)) + (b * a)) (r, a, b)  # funcion anonima para el area de la figura

        perimetro_figura2 = (lambda r, a, b : 2 * (2 * pi * r) + (2 * b + 2 * a)) (r, a, b) # funcion anonima para el perimetro de la figura
        
        print(f"A partir de los datos ingresados de: \n {r} cm de radio para los circulos \n {a} cm de largo para la atura del rectangulo \n {b} cm de ancho para la base")
        print(f"El volumen de la figura es {area_figura2} cm ^ 2") # impresion de area
        print(f"El area superficial de la figura es {perimetro_figura2} cm") # impresion de perimetro
        
    except ValueError:
        print("El valor ingresado no se trata de un numero real")