# pdc_reto_9
### Soy Rafael Santiago Chirivi Peña y pertenezco al grupo de "Fenomenoides", adelante se muestra nuestro logo 

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>

### A continuacion, se muestran las soluciones propuestas a los distintos puntos de este reto

## 1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

### 1.1
<div align='center'>
<figure> <a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/FKBsrHTV/IMG-20240322-WA0066.jpg" alt="IMG-20240322-WA0066"/></a><br/><br/>
<figcaption><b></b></figcaption></figure>
</div>
+ Una función matemática para calcular el volumen y el área superficial.

+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.

```python
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
```

### 1.2
<div align='center'>
<figure> <a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/FsLF9vSj/IMG-20240322-WA0067.jpg" alt="IMG-20240322-WA0067"/></a><br/><br/>
<figcaption><b></b></figcaption></figure>
</div>
+ Una función matemática para calcular el área y el perimetro.

+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.

```python
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
```

### 1.3 Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python
if __name__ == "__main__":
    try:
        gallinas : int = int(input("Por favor, ingrese el numero de gallinas: ")) # ingreso del numero de gallinas
        while gallinas < 0: # limitante para el valor
            gallinas = int(input("No existen cantidades negativas, por favor intentelo de nuevo: ")) # reingreso al cumplirse la condicion de error

        gallos : int = int(input("Por favor, ingrese el numero de gallos: ")) # ingreso del numero de gallos
        while gallos < 0: # limitante para el valor
            gallos = int(input("No existen cantidades negativas, por favor intentelo de nuevo: ")) # reingreso al cumplirse la condicion de error

        pollitos : int = int(input("Por favor, ingrese el numero de pollitos: ")) # ingreso del numero de pollitos 
        while pollitos < 0: # limitante para el valor
            pollitos = int(input("No existen cantidades negativas, por favor intentelo de nuevo: ")) # reingreso al cumplirse la condicion de error

        kilos_aves = (lambda gallinas, gallos, pollitos : (gallinas * 6) + (gallos * 7) + pollitos) (gallinas, gallos, pollitos) # funcion anonima de los kilos de carne (gallinas 6kg) (gallos 7kg) (pollitos 1kg)
        
        print(f"Tomando en cuenta las cantidades ingresadas de {gallinas} gallinas, {gallos} gallos y {pollitos} pollitos")
        print(f"Los kilos de carne de ave resultantes son de {kilos_aves} kg") # impresion de kilos de carne
        
    except ValueError:
        print("El valor ingresado no es un numero entero")    
```

## 2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
# Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
+ 2.1 El promedio
+ 2.2 El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
+ 2.3 La raíz cúbica del menor número
### 2.1

```python
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
```

### 2.2

```python
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
```

### 2.3

```python
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
```

## 3. Escriba una función recursiva para calcular la operación de la potencia.
   
```python
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
```
 
## 4. Utilice la siguiente plantilla de code para contar el tiempo:
   
```python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```
Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. 

```python
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
```
## 5. Crear cuenta en stackoverflow y adjuntar imagen en el repo
[![imagen-2024-04-22-214502859.png](https://i.postimg.cc/9fQhhpxs/imagen-2024-04-22-214502859.png)](https://postimg.cc/VJpT9jPF)
## 6. Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.
El enlace a mi perfil de linkedin se encuentra [aqui](http://www.linkedin.com/in/Rafael-Santiago-Chirivi-Pena)
