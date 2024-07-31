import numpy as np

# Create user function =========================
def myadd(x, y):
  return x+y
myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))


# Simple Arithmetic function
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)
newarr = np.subtract(arr1, arr2)
newarr = np.multiply(arr1, arr2)
newarr = np.divide(arr1, arr2)
newarr = np.power(arr1, arr2)
newarr = np.mod(arr1, arr2)
newarr = np.remainder(arr1, arr2)
newarr = np.divmod(arr1, arr2)      # The divmod() function return both the quotient and the the mod.
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])            # 12
newarr = np.sum([arr1, arr2], axis=1)   #[6,6]
newarr = np.cumsum(arr1)                #[1, 3, 6]
x = np.prod([arr1, arr2])
newarr = np.prod([arr1, arr2], axis=1)
newarr = np.cumprod(arr1)
newarr = np.diff(arr1)                  # [1,1]
newarr = np.diff(arr1, n=2)             # [0]   Difference two times



# Rounding Decimals ================================
arr = np.trunc([-3.1666, 3.6667])      # [-3.  3.]
arr = np.fix([-3.1666, 3.6667])         # [-3.  3.]
arr = np.around(3.1666, 2)              # 3.17
arr = np.floor([-3.1666, 3.6667])       # [-4.  3.]
arr = np.ceil([-3.1666, 3.6667])        # [-3.  4.]


arr = np.log2([1,2,3,4,5])              # [0.  1.  1.5849625  2.  2.32192809]
arr = np.log10([1,2,3,4,5])              # [0.  0.30103  0.47712125  0.60205999  0.69897]
arr = np.log([1,2,3,4,5])              # [0. 0.69314718 1.09861229 1.38629436 1.60943791]


# Finding Lowest Common Multiple ==============================
num1 = 4
num2 = 6
x = np.lcm(num1, num2)              # 12

# reduce() method used to find lcm for array element
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)              # 18

# Finding Greatest Common Denominator or HCF(Highest Common Factor ==========================
num1 = 6
num2 = 9
x = np.gcd(num1, num2)              # 3

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)              # 4


# Create Sets in NumPy ======================================
# set arrays should only be 1-D arrays
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
newarr = np.setdiff1d(arr1, arr2, assume_unique=True)




