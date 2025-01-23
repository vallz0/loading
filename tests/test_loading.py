from loading import Loading
import time

def test_loading():
    loader = Loading()
    start = time.time()
    loader.show(2)  # Testa o carregamento por 2 segundos
    end = time.time()
    assert round(end - start) == 2
