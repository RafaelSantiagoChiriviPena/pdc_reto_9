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