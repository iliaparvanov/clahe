import numpy as np

array = np.arange(20).reshape(4, 5)
print(array)

mask = array == 5
array = np.where(mask, -1, array)
print(mask)