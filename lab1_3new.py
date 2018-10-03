from scipy import linalg
import math
from numpy.linalg import inv
import numpy as np
from scipy.optimize import minimize as min


f = lambda x: np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
X = np.arange(1, 15, 0.1)
res = min(f, 2, method='BFGS')