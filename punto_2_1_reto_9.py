def promedio (*args) -> float: # definir la funcion de argumento no definido
    sumatoria : int = 0 # establecer la constante para la sumatoria de datos en 0
    for num in args: # bucle que recorra los datos de la tupla
        sumatoria += num # sumatoria de los datos
    return sumatoria / len(args) # obtener el promedio de la forma (sumatoria de los datos / numero de datos)

if __name__ == "__main__":
    try: 
        a : float = float(input("Ingrese numero a: ")) # ingreso de dato 1
        b : float = float(input("Ingrese numero b: ")) # ingreso de dato 2
        c : float = float(input("Ingrese numero c: ")) # ingreso de dato 3
        d : float = float(input("Ingrese numero d: ")) # ingreso de dato 4
        e : float = float(input("Ingrese numero e: ")) # ingreso de dato 5
        
        print(f"promedio de dos datos: {promedio(a,b)}") # funcion de promedio a los datos 1 y 2 
        print(f"promedio de tres datos: {promedio(a,b,c)}") # funcion de promedio a los datos 1, 2 y 3 
        print(f"promedio de cuatro datos: {promedio(a,b,c,d)}") # funcion de promedio a los datos 1, 2, 3 y 4  
        print(f"promedio de cinco datos: {promedio(a,b,c,d,e)}") # funcion de promedio a los datos 1, 2, 3, 4 y 5
        
    except ValueError:
        print("El valor ingresado no se trata de un numero")