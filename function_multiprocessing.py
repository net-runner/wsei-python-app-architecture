#Napisz program, który oblicza wartości funkcji 𝑓(𝑥) = 𝑐𝑜𝑠(𝑥) + 𝑙𝑛(𝑥 + 1)^2 dla
#dużego zestawu wartości 𝑥 (np. od 1 do 1e6 z krokiem 0.01). Podziel zakres 𝑥 na
#fragmenty i wykorzystaj moduł multiprocessing, aby równolegle obliczyć wartości
#funkcji dla każdego fragmentu

import numpy as np
import multiprocessing as mp
from math import cos, log

def compute_chunk(x_values):
    return [cos(x) + log(x + 1) for x in x_values]

def parallel_compute(start, stop, step, num_workers=mp.cpu_count()):
    x_values = np.arange(start, stop, step)
    chunk_size = len(x_values) // num_workers
    chunks = [x_values[i * chunk_size:(i + 1) * chunk_size] for i in range(num_workers)]
    
    with mp.Pool(num_workers) as pool:
        results = pool.map(compute_chunk, chunks)
    
    return np.concatenate(results)

if __name__ == "__main__":
    start, stop, step = 1, 1e6, 0.01
    results = parallel_compute(start, stop, step)
    print("Obliczenia zakończone. Przykładowe wyniki:", results[:10])
