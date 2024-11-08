import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_ejercicio01():
    import codigo_estudiante as micodigo
    salida = micodigo.ejercicio01()
    assert salida == True