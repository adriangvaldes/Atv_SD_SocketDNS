import pickle
import numpy as np

array = [1, 2, 0, 9, 3, 7, 8, 5]
splitArray = np.array_split(array, 2)
arraySerialized = pickle.dumps(splitArray[0])
msg = arraySerialized

print (msg)

msg2 = pickle.loads(msg)
print (msg2)