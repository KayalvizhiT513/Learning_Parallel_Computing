from joblib import Parallel, delayed
import numpy as np

def random_square(seed):
    np.random.seed(seed)
    random_num = np.random.randint(0, 10)
    return random_num**2

print("With 8 jobs")
results = Parallel(n_jobs=8, verbose=1)\
          (delayed(random_square)(i) for i in range(1000000))

print("Using all CPUs")
results = Parallel(n_jobs=-1, verbose=1)\
          (delayed(random_square)(i) for i in range(1000000))

print("Using all CPUs but one")
results = Parallel(n_jobs=-2, verbose=1)\
          (delayed(random_square)(i) for i in range(1000000))

print("Backend set to multiprocessing")
results = Parallel(n_jobs=-1, backend="multiprocessing", verbose=1)\
          (delayed(random_square)(i) for i in range(1000000))

