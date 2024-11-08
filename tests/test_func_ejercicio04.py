import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_ejercicio04():
    import codigo_estudiante as micodigo
    salida = micodigo.ejercicio04()
    assert salida[0] == 2
    assert salida[4] == 10