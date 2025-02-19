def addition(a, b):
    """Retourne la somme de a et b."""
    return a + b

def soustraction(a, b):
    """Retourne la différence entre a et b."""
    return a - b

def multiplication(a, b):
    """Retourne le produit de a et b."""
    return a * b

def division(a, b):
    """Retourne le quotient de a et b. Lève une exception si b est zéro."""
    if b == 0:
        raise ValueError("La division par zéro n'est pas autorisée.")
    return a / b