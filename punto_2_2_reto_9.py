def prom_multiplicativo (*args) -> float: # definir la funcion de argumento no definido
    multiplicacion : int = 1 # establecer la constante para la multiplacion de datos en 1
    for num in args: # bucle que recorra los datos de la tupla
        multiplicacion*= num # multiplicacion de los datos
    return multiplicacion ** len(args) # promedio multiplicativo de la forma ( datos multiplicados ^ numero de datos)
if __name__ == "__main__":
    try: 
        a : float = float(input("Ingrese numero a: ")) # ingreso de dato 1
        b : float = float(input("Ingrese numero b: ")) # ingreso de dato 2
        c : float = float(input("Ingrese numero c: ")) # ingreso de dato 3
        d : float = float(input("Ingrese numero d: ")) # ingreso de dato 4
        e : float = float(input("Ingrese numero e: ")) # ingreso de dato 5
        
        print(f"promedio multiplicativo de dos datos: {prom_multiplicativo(a,b)}") # funcion de promedio multiplicativo a los datos 1 y 2 
        print(f"promedio multiplicativo de tres datos: {prom_multiplicativo(a,b,c)}") # funcion de promedio multiplicativo a los datos 1, 2 y 3
        print(f"promedio multiplicativo de cuatro datos: {prom_multiplicativo(a,b,c,d)}") # funcion de promedio multiplicativo a los datos 1, 2, 3 y 4
        print(f"promedio multiplicativo de cinco datos: {prom_multiplicativo(a,b,c,d,e)}") # funcion de promedio multiplicativo a los datos 1, 2, 3, 4 y 5
        
    except ValueError:
        print("El valor ingresado no se trata de un numero")