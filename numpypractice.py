import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr.shape)

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = arr.reshape(3,4)
print(new_arr)

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = arr.reshape(2,3,2)
print(new_arr)

import numpy as np
arr = np.array([1,2,3,4,5])
for x in arr:
    print(x)

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)

import numpy as np
arr =np.array([[1,2,3],[4,5,6],[7,8,9]])
for x in arr:
    print(x)

import numpy as np
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)

import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)