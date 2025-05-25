#numpy is a python module consisting of multidimensional array objects and a set of routines for processing those arrays
#mathematical and logical operations on the array can be performed
#fourier transforms and routines for shape manupilation
#operation related to linear algebra and random number
import numpy as np

narr =  np.array([(1,2,3,4),(5,6,7,8)],dtype=float)
print(f"the number of dimension in this array: {narr.ndim}")
print(f"the shap or number od element in each dimension: {narr.shape}")
print(f"the total elements in the array {narr.size}")
print(f"the individuall item size{narr.itemsize}")
print(f"the datatype of the array{narr.dtype}")