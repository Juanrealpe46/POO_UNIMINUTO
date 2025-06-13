# view.py

def display_menu():
#   """Menu de operacion a realizar"""
    print("\n--- Calculadora de Series de Taylor ---")
    print("1. Calcular e^x")
    print("2. Calcular sen(x)")
    print("3. Calcular cos(x)")
    print("4. Calcular arcsen(x)")
    print("5. Calcular arccos(x)")
    print("6. Calcular senh(x)")
    print("7. Calcular cosh(x)")
    print("8. Salir")
    print("--------------------------------")

def get_input_value(prompt):
#   """Obtiene una entrada flotante del usuario con un mensaje dado."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Entrada invalida. Por favor, ingrese un valor numerico.")

def get_input_n_terms():
#    """Obtiene un entero para el número de términos del usuario."""
    while True:
        try:
            n_terms = int(input("Ingrese el numero de terminos para la serie (ej. 10, 20): "))
            if n_terms <= 0:
                print("El numero de terminos debe ser un entero positivo.")
            else:
                return n_terms
        except ValueError:
            print("Entrada invalida. Por favor, ingrese un numero entero.")

def display_result(function_name, x_value, result):
#    """Muestra el resultado calculado."""
    print(f"\nResultado para {function_name}({x_value}): {result}")

def display_error(message):
#    """Muestra un mensaje de error."""
    print(f"\nError: {message}")

def display_goodbye():
#    """Muestra un mensaje de despedida."""
    print("Gracias por usar la Calculadora de Series de Taylor.")