def potencia_recursiva (x : int, n : int) -> int : # definir la funcion 

    if n == 0: # caso base de exponente 0
        return 1
    else: 
        return x * potencia_recursiva (x, n - 1) # funcion recursiva de multiplicacion de x por si mismo, restando 1 al exponente hasta que sea 0 (x^n * x^n-1 * x^n-2 ... 1)

if __name__ == "__main__":
    try:
        x : int = int(input("ingrese la base para la potencia: ")) # ingreso para la base de la potencia
        n : int = int(input("ingrese el exponente para la potencia: ")) # ingreso del exponente

        potencia = potencia_recursiva (x, n) # funcion recursiva de potencia sobre los datos ingresados

        print(f"la base {x} elevada al exponente {n} = {potencia}") #impresion de potencia
        
    except ValueError:
        print("El valor ingresado no se trata de un numero entero")