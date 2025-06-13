# model.py

def factorial(n):
    """
    Calcula el factorial de un entero no negativo n.
    Implementado manualmente según los requisitos del proyecto (sin math.factorial).
    """
    if n < 0:
        return None  # El factorial no está definido para números negativos
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def power(base, exp):
    """
    Calcula la base elevada a la potencia de exp.
    Implementado manualmente según los requisitos del proyecto (sin operador **).
    Maneja exponentes positivos, negativos y cero.
    """
    if exp == 0:
        return 1.0
    if exp < 0:
        base = 1.0 / base
        exp = -exp
    result = 1.0
    for _ in range(exp):
        result *= base
    return result

def calculate_e_x(x, n_terms=10):
    """
    Calcula e^x usando su expansión en serie de Maclaurin.
    e^x = sum (x^n / n!) para n desde 0 hasta infinito
   
    :param x: El valor en el que se debe evaluar e^x.
    :param n_terms: El número de términos a usar en la serie para la aproximación.
    """
    e_x_approx = 0.0
    for n in range(n_terms):
        term = power(x, n) / factorial(n)
        e_x_approx += term
    return e_x_approx

def calculate_sen_x(x, n_terms=10):
    """
    Calcula sen(x) usando su expansión en serie de Maclaurin.
    sen x = sum ((-1)^n * x^(2n+1) / (2n+1)!) para n desde 0 hasta infinito
   
    :param x: El valor en el que se debe evaluar sen(x).
    :param n_terms: El número de términos a usar en la serie para la aproximación.
    """
    sin_x_approx = 0.0
    sign = 1
    for n in range(n_terms):
        numerator = sign * power(x, (2 * n + 1))
        denominator = factorial(2 * n + 1)
        term = numerator / denominator
        sin_x_approx += term
        sign *= -1  # Alternar el signo
    return sin_x_approx

def calculate_cos_x(x, n_terms=10):
    """
    Calcula cos(x) usando su expansión en serie de Maclaurin.
    cos x = sum ((-1)^n * x^(2n) / (2n)!) para n desde 0 hasta infinito
   
    :param x: El valor en el que se debe evaluar cos(x).
    :param n_terms: El número de términos a usar en la serie para la aproximación.
    """
    cos_x_approx = 0.0
    sign = 1
    for n in range(n_terms):
        numerator = sign * power(x, (2 * n))
        denominator = factorial(2 * n)
        term = numerator / denominator
        cos_x_approx += term
        sign *= -1  # Alternar el signo
    return cos_x_approx

# Nota: arcsen(x) y arccos(x) son más complejos ya que sus series requieren
# manejo de constantes y términos de serie potencialmente más complejos.
# Además, arccos(x) depende de arcsen(x). Implementar esto sin
# ninguna función matemática incorporada (especialmente para pi o raíces cuadradas, si es necesario)
# será significativamente más desafiante y podría requerir métodos iterativos
# para la aproximación de pi si la precisión es crítica.
# Por simplicidad en este código inicial, proporcionaré la estructura, pero
# una implementación manual completa de arcsen sin ninguna función matemática es
# una tarea sustancial.
# Por ahora, implementaré arcsen(x) y arccos(x) basándome en la serie,
# asumiendo que se define manualmente una constante para pi si es necesario, o que
# el proyecto permite una constante predefinida para pi si no es calculable.

PI = 3.141592653589793 # Una aproximación común de PI

def calculate_arcsen_x(x, n_terms=10):
    """
    Calcula arcsen(x) usando su expansión en serie de Maclaurin.
    arcsen x = sum ( (2n)! / (4^n * (n!)^2 * (2n+1)) * x^(2n+1) ) para |x| < 1
   
    :param x: El valor en el que se debe evaluar arcsen(x).
              Nota: Esta serie converge para |x| < 1.
    :param n_terms: El número de términos a usar en la serie para la aproximación.
    """
    if x >= 1 or x <= -1:
        # La serie converge para |x| < 1
        return "Error: x debe estar entre -1 y 1 para la serie de arcsen(x)."

    arcsen_x_approx = 0.0
    for n in range(n_terms):
        numerator = factorial(2 * n)
        denominator = power(4, n) * power(factorial(n), 2) * (2 * n + 1)
        term = (numerator / denominator) * power(x, (2 * n + 1))
        arcsen_x_approx += term
    return arcsen_x_approx

def calculate_arccos_x(x, n_terms=10):
    """
    Calcula arccos(x) usando la relación arccos(x) = PI/2 - arcsen(x).
   
    :param x: El valor en el que se debe evaluar arccos(x).
              Nota: El componente arcsen(x) converge para |x| < 1.
    :param n_terms: El número de términos a usar en la serie de arcsen para la aproximación.
    """
    arcsen_val = calculate_arcsen_x(x, n_terms)
    if isinstance(arcsen_val, str) and "Error" in arcsen_val:
        return arcsen_val # Pasar el mensaje de error de arcsen

    return (PI / 2.0) - arcsen_val

def calculate_senh_x(x, n_terms=10):
    """
    Calcula senh(x) usando su expansión en serie de Maclaurin.
    senh x = sum (x^(2n+1) / (2n+1)!) para n desde 0 hasta infinito
   
    :param x: El valor en el que se debe evaluar senh(x).
    :param n_terms: El número de términos a usar en la serie para la aproximación.
    """
    senh_x_approx = 0.0
    for n in range(n_terms):
        numerator = power(x, (2 * n + 1))
        denominator = factorial(2 * n + 1)
        term = numerator / denominator
        senh_x_approx += term
    return senh_x_approx

def calculate_cosh_x(x, n_terms=10):
    """
    Calcula cosh(x) usando su expansión en serie de Maclaurin.
    cosh x = sum (x^(2n) / (2n)!) para n desde 0 hasta infinito
   
    :param x: El valor en el que se debe evaluar cosh(x).
    :param n_terms: El número de términos a usar en la serie para la aproximación.
    """
    cosh_x_approx = 0.0
    for n in range(n_terms):
        numerator = power(x, (2 * n))
        denominator = factorial(2 * n)
        term = numerator / denominator
        cosh_x_approx += term
    return cosh_x_approx