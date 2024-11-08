import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_ejercicio08():
    import codigo_estudiante as micodigo
    salida = micodigo.ejercicio08()
    assert salida[0] == 8
    assert salida[2] == 5
    assert salida[4] == 10