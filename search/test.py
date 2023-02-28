import numpy as np
# listOfBoolValues = np.array([[True, False, False, True, False, False, False, True, True, True, False],
# [True, False, False, True, False, False, False, True, True, True, False]])
# # Get indices of True values in a list
# # indices = np.where(listOfBoolValues)[0].tolist()
# indices = np.argwhere(np.any(listOfBoolValues == True, axis=1))
# arr = np.array([[11, 12, 13],
#                 [14, 15, 16],
#                 [17, 15, 11],
#                 [12, 14, 15]])

arr = [[True, False, False],
                [False, True, False],
                [False, True, False],
                [False, False, True]]
result = np.where(arr == True)
print('Tuple of arrays returned : ', list(zip(result[0], result[1])))