# controller.py (o main.py)
import model
import view

def run_calculator():
#    """Función principal para ejecutar la Calculadora de Series de Taylor."""
    while True:
        view.display_menu()
        choice = input("Ingrese su opción (1-8): ")

        if choice == '8':
            view.display_goodbye()
            break

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            x_value = view.get_input_value("Ingrese el valor de x: ")
            n_terms = view.get_input_n_terms()

            result = None
            function_name = ""

            if choice == '1':
                function_name = "e^x"
                result = model.calculate_e_x(x_value, n_terms)
            elif choice == '2':
                function_name = "sen(x)"
                result = model.calculate_sen_x(x_value, n_terms)
            elif choice == '3':
                function_name = "cos(x)"
                result = model.calculate_cos_x(x_value, n_terms)
            elif choice == '4':
                function_name = "arcsen(x)"
                result = model.calculate_arcsen_x(x_value, n_terms)
            elif choice == '5':
                function_name = "arccos(x)"
                result = model.calculate_arccos_x(x_value, n_terms)
            elif choice == '6':
                function_name = "senh(x)"
                result = model.calculate_senh_x(x_value, n_terms)
            elif choice == '7':
                function_name = "cosh(x)"
                result = model.calculate_cosh_x(x_value, n_terms)

            if isinstance(result, str) and "Error" in result:
                view.display_error(result)
            else:
                view.display_result(function_name, x_value, result)
        else:
            view.display_error("Opción inválida. Por favor, ingrese un número entre 1 y 8.")

if __name__ == "__main__":
    run_calculator()