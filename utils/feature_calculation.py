import numpy as np

def sin_trans(x):
    return np.sin((x-1)*(2.*np.pi/12))

def cos_trans(x):
    return np.cos((x-1)*(2.*np.pi/12))