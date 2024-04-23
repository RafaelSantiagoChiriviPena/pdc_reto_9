import time # importacion de la funcion tiempo para medir la aplicacion de funciones 

def fibo (n : int) -> int: # definir la funcion
    n1 : int = 0 # establecer constante menor 0
    n2 : int = 1 # establecer constante mayor 1
    for i in range (1, n+1, 1): # bucle que recorra el numero de sumas a realizar
        sumafibo = n1 + n2 # establecer resultado de suma
        n1 = n2  # escalar valores hacia su siguiente mayor
        n2 = sumafibo # escalar valores hacia su siguiente mayor
    return (sumafibo) # valor dentro de la secuencia de fibonacci en el numero de sumas ingresado

def fibo_recursiva (n : int) -> int: # definir la funcion
    if n <= 1: # caso base de 1 suma
        return 1
    else: 
        return fibo_recursiva(n-1) + fibo_recursiva(n-2) # funcion recursiva de suma de terminos, descomposicion de los terminos a aplicacion de la funcion en 1 y 0 para suma de solo unos
if __name__ == "__main__":
    try:
        n : int = int(input("Ingrese el numero de sumas que desea realizar: ")) # ingreso del numero de sumas
        start_time = time.time() # aplicacion de la funcion de tiempo para medir cuanto tarda en aplicar la funcion de iteracion de fibonacci
        print(f"La suma numero {n} de fibonacci es {fibo(n)}") # impresion del valor en la serie de fibonacci hasta la suma ingresada
        end_time = time.time() # finalizacion de la medida de tiempo

        timer = end_time - start_time # calculo de tiempo
        print(f"Tiempo de calculo: {timer} seg") # impresion de cuanto tardo la funcion de iteracion en calcular

        start_time = time.time() # aplicacion de la funcion de tiempo para medir cuanto tarda en aplicar la funcion de recursion de fibonacci
        print(f"La suma numero {n} de fibonacci es {fibo_recursiva(n)}") # impresion del valor en la serie de fibonacci hasta la suma ingresada
        end_time = time.time() # finalizacion de la medida de tiempo

        timer = end_time - start_time # calculo de tiempo
        print(f"Tiempo de calculo: {timer} seg") # impresion de cuanto tardo la funcion de iteracion en calcular
    except ValueError:
        print("El valor ingresado no se trata de un numero entero")
# A partir de la suma 32, los resultados dejan de salir de manera instantanea con una diferencia de tiempo de 0.46 casi 0.5s
# A partir de la suma 34, los resultados se imprimen con una diferencia de tiempo de 1.15s, siendo la primera en superar el segundo