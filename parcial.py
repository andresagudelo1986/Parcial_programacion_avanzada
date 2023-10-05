import random
import time
import statistics
import sys

class MenuPrincipal:

    """
    Docstring: este programa me genera lista, analiza algunos datos stadisticos y ordena los datos aplicando varios metodos.
    """

    #metodo constructor
    def __init__(self):
        self.lista = None
    #metodo magico
    def __str__(self):
        return "Ingeniería en Automatización"
    
    #metodo estático
    @staticmethod
    def mostrar_menu_principal():
        print("MENU PRINCIPAL")
        print("1. Generar una lista aleatoria")
        print("2. Ingresar lista manualmente")
        print("3. Usar lista previamente cargada")
        print("4. Crear lista desde rango")
        print("5. Ayuda")
        print("6. Salir")

    def ejecutar(self):
        while True:
            try:
                print(f"\n{self}\n")
                self.mostrar_menu_principal()
                opcion_principal = self.obtener_opcion("Seleccione una opción: ")

                if opcion_principal == 1:
                    self.lista = ListaNumerosAleatorios()
                    print("Lista aleatoria generada.")

                elif opcion_principal == 2:
                    self.lista = ListaNumerosManual()
                    print("Lista ingresada manualmente.")

                elif opcion_principal == 3:
                    self.lista = ListaNumerosCargada()
                    print("Lista cargada.")

                elif opcion_principal == 4:
                    self.lista = ListaNumerosRango()
                    print("Lista creada desde rango.")

                elif opcion_principal == 5:
                    self.mostrar_ayuda()

                elif opcion_principal == 6:
                    print("Saliendo del programa.")
                    break

                else:
                    print("Opción no válida. Inténtelo de nuevo.")

                while self.lista:
                    while True:  # Bucle para mostrar el submenú hasta que se seleccione 'o'
                        self.mostrar_submenu()
                        opcion_submenu = self.obtener_opcion("Seleccione una opción del submenu: ")

                        if opcion_submenu == 'a':
                            self.lista.imprimir_lista()

                        elif opcion_submenu == 'b':
                            self.medir_tiempo_ejecucion(self.lista.ordenar_burbuja, "Ordenamiento Burbuja")
                            self.lista.imprimir_lista()

                        elif opcion_submenu == 'c':
                            self.medir_tiempo_ejecucion(self.lista.ordenar_rapido, "Ordenamiento Rápido")
                            self.lista.imprimir_lista()

                        elif opcion_submenu == 'd':
                            # Ordenar con el método burbuja y medir el tiempo
                            self.medir_tiempo_ejecucion(self.lista.ordenar_burbuja, "Ordenamiento Burbuja")

                            # Ordenar con el método rápido y medir el tiempo
                            self.medir_tiempo_ejecucion(self.lista.ordenar_rapido, "Ordenamiento Rápido")

                            # Ordenar con el método sorted y medir el tiempo
                            self.medir_tiempo_ejecucion(self.lista.ordenar_sorted, "Ordenamiento Sorted")

                        elif opcion_submenu == 'e':
                            numero_buscar = self.obtener_opcion("Ingrese el número a buscar: ")
                            self.lista.busqueda_lineal(numero_buscar)

                        elif opcion_submenu == 'f':
                            numero_buscar = self.obtener_opcion("Ingrese el número a buscar: ")
                            self.lista.busqueda_binaria(numero_buscar)

                        elif opcion_submenu == 'g':
                            self.lista.sumar_elementos()

                        elif opcion_submenu == 'h':
                            self.lista.calcular_promedio()

                        elif opcion_submenu == 'i':
                            self.lista.calcular_mediana()

                        elif opcion_submenu == 'j':
                            self.lista.calcular_varianza()

                        elif opcion_submenu == 'k':
                            self.lista.encontrar_minimo()

                        elif opcion_submenu == 'l':
                            self.lista.encontrar_maximo()

                        elif opcion_submenu == 'm':
                            self.lista.mostrar_longitud()

                        elif opcion_submenu == 'n':
                            self.comparar_con_otra_lista()

                        elif opcion_submenu == 'o':
                            self.lista = None
                            break  # Salir del submenú y volver al menú principal

                        else:
                            print("Opción no válida. Inténtelo de nuevo.")

            except Exception as e:
                print(f"Error: {e}")

    @staticmethod
    def mostrar_ayuda():
        print("Ayuda:")
        print("- La búsqueda lineal recorre la lista de principio a fin hasta encontrar el elemento previamente seleccionado.")
        print("- La búsqueda binaria requiere que la lista esté ordenada y encuentra el elemento dividiendo la lista en mitades.")
        print("- El ordenamiento por burbuja compara pares de elementos adyacentes y los intercambia si están en orden incorrecto.")
        print("- El ordenamiento rápido utiliza un elemento pivote para dividir la lista y ordenarla de manera más eficiente.")

    def comparar_con_otra_lista(self):
        otra_lista = ListaNumerosManual()  # Ingresar una nueva lista manualmente
        if self.lista == otra_lista:
            print("Las listas son iguales.")
        else:
            print("Las listas son diferentes.")

    @staticmethod
    def obtener_opcion(mensaje):
        while True:
            try:
                opcion = input(mensaje)
                if opcion.isdigit():
                    return int(opcion)
                elif opcion.isalpha() and len(opcion) == 1:
                    return opcion.lower()
                else:
                    print("Opción no válida. Inténtelo de nuevo.")
            except ValueError:
                print("Opción no válida. Inténtelo de nuevo.")

    @staticmethod
    def mostrar_submenu():
        print("\nSUBMENU")
        print("a. Imprimir lista")
        print("b. Ordenar con burbuja")
        print("c. Ordenar con rápido")
        print("d. Ordenar con sorted()")
        print("e. Buscar elemento con búsqueda lineal")
        print("f. Buscar elemento con búsqueda binaria")
        print("g. Sumar elementos de la lista")
        print("h. Calcular promedio")
        print("i. Calcular mediana")
        print("j. Calcular varianza")
        print("k. Encontrar el número mínimo")
        print("l. Encontrar el máximo")
        print("m. Mostrar longitud de la lista")
        print("n. Comparar con otra lista")
        print("o. Volver al menú principal")

    def medir_tiempo_ejecucion(self, funcion, nombre):
        inicio = time.time()
        funcion()
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print(f"Tiempo de ejecución para {nombre}: {tiempo_ejecucion:.8f} segundos")


class ListaNumeros:
    def __init__(self):
        self.lista = []

    def __str__(self):
        return f"Lista: {self.lista}"

    #Metodo magico
    def __eq__(self, other):
        return self.lista == other.lista

    def imprimir_lista(self):
        if len(self.lista) > 20:
            print(f"La lista generada es: {self.lista[:10]}")  # Muestra solo los primeros 10 elementos
        else:
            print(f"La lista generada es: {self.lista}")

    def sumar_elementos(self):
        suma = sum(self.lista)
        print(f"La suma de los elementos es: {suma}")

    def calcular_promedio(self):
        promedio = int(sum(self.lista) / len(self.lista))
        print(f"El promedio de la lista es: {promedio}")

    def calcular_mediana(self):
        mediana = int(statistics.median(self.lista))
        print(f"La mediana de la lista es: {mediana}")

    def calcular_varianza(self):
        varianza = statistics.variance(self.lista)
        print(f"La varianza de la lista es: {varianza}")

    def encontrar_minimo(self):
        minimo = min(self.lista)
        print(f"El valor mínimo de la lista es: {minimo}")

    def encontrar_maximo(self):
        maximo = max(self.lista)
        print(f"El valor máximo de la lista es: {maximo}")

    def mostrar_longitud(self):
        print(f"La longitud de la lista es: {len(self.lista)}")

    def ordenar_burbuja(self):
        n = len(self.lista)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.lista[j] > self.lista[j + 1]:
                    self.lista[j], self.lista[j + 1] = self.lista[j + 1], self.lista[j]

    def ordenar_rapido(self):
        self.lista = self.quicksort(self.lista)

    def ordenar_sorted(self):
        self.lista = sorted(self.lista)

    def quicksort(self, lista):
        if len(lista) <= 1:
            return lista

        pivote = lista[len(lista) // 2]
        izquierda = [x for x in lista if x < pivote]
        medio = [x for x in lista if x == pivote]
        derecha = [x for x in lista if x > pivote]

        return self.quicksort(izquierda) + medio + self.quicksort(derecha)

    def busqueda_lineal(self, numero):
        for i, elem in enumerate(self.lista):
            if elem == numero:
                print(f"El número {numero} se encuentra en la posición {i}.")
                return
        print(f"El número {numero} no se encuentra en la lista.")

    def busqueda_binaria(self, numero):
        self.lista.sort()  # Asegurar que la lista esté ordenada
        izquierda, derecha = 0, len(self.lista) - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            valor_medio = self.lista[medio]

            if valor_medio == numero:
                print(f"El número {numero} se encuentra en la posición {medio}.")
                return
            elif valor_medio < numero:
                izquierda = medio + 1
            else:
                derecha = medio - 1

        print(f"El número {numero} no se encuentra en la lista.")

    def cargar_lista(self, nueva_lista):
        self.lista = nueva_lista


class ListaNumerosAleatorios(ListaNumeros):
    def __init__(self):
        super().__init__()
        self.generar_lista_aleatoria()

    def generar_lista_aleatoria(self):
        longitud = MenuPrincipal.obtener_opcion("Ingrese la longitud de la lista aleatoria: ")
        numeros_aleatorios = random.sample(range(1, 1000), longitud)
        self.lista = numeros_aleatorios


class ListaNumerosManual(ListaNumeros):
    def __init__(self):
        super().__init__()
        self.ingresar_lista_manualmente()

    def ingresar_lista_manualmente(self):
        elementos = input("Ingrese los elementos de la lista separados por espacios: ")
        self.lista = [int(x) for x in elementos.split()]


class ListaNumerosCargada(ListaNumeros):
    def __init__(self):
        super().__init__()
        self.cargar_lista()

    def cargar_lista(self):
        # Puedes modificar esta función para cargar la lista desde un archivo o base de datos
        self.lista = [597, 900, 165, 458, 351, 726, 638, 175, 409, 32, 77, 161, 821, 979, 560, 257, 322, 46, 753, 856]


class ListaNumerosRango(ListaNumeros):
    def __init__(self):
        super().__init__()
        self.crear_lista_desde_rango()

    def crear_lista_desde_rango(self):
        while True:
            try:
                inicio = MenuPrincipal.obtener_opcion("Ingrese el inicio del rango: ")
                fin = MenuPrincipal.obtener_opcion("Ingrese el fin del rango: ")
                longitud = MenuPrincipal.obtener_opcion("Ingrese la longitud de la lista: ")

                if fin - inicio + 1 < longitud:
                    raise ValueError("Error: La longitud de la lista es mayor que el rango especificado.")

                self.lista = random.sample(range(inicio, fin + 1), longitud)
                break
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    programa = MenuPrincipal()
    programa.ejecutar()
