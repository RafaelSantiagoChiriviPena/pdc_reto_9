def raiz_cubica_menor (*args) -> float: # definir la funcion de argumento no definido
    lista : list = [] # establecer lista vacia para convertir los datos de la tupla
    for num in args: # bucle que recorra los datos de la tupla
        lista.append(num) # agregar los datos a la lista
    lista.sort() # ordenar la lista
    return float(lista[0]) ** (1/3) # obtener la raiz cubica del dato inferior dentro de la lista ordenada
if __name__ == "__main__":
    try: 
        a : float = float(input("Ingrese numero a: ")) # ingreso de dato 1
        b : float = float(input("Ingrese numero b: ")) # ingreso de dato 2
        c : float = float(input("Ingrese numero c: ")) # ingreso de dato 3
        d : float = float(input("Ingrese numero d: ")) # ingreso de dato 4
        e : float = float(input("Ingrese numero e: ")) # ingreso de dato 5
        
        print(f"raiz cubica del menor en dos elementos: {raiz_cubica_menor(a,b)}") # funcion de raiz cubica al menor en los datos 1 y 2 
        print(f"raiz cubica del menor en tres elementos: {raiz_cubica_menor(a,b,c)}") # funcion de raiz cubica al menor en los datos 1, 2 y 3
        print(f"raiz cubica del menor en cuatro elementos: {raiz_cubica_menor(a,b,c,d)}") # funcion de raiz cubica al menor en los datos 1, 2, 3 y 4
        print(f"raiz cubica del menor en cinco elementos: {raiz_cubica_menor(a,b,c,d,e)}") # funcion de raiz cubica al menor en los datos 1, 2, 3, 4 y 5
        
    except ValueError:
        print("El valor ingresado no se trata de un numero")