import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_ejercicio03():
    import codigo_estudiante as micodigo
    salida = micodigo.ejercicio03()
    assert salida == 200