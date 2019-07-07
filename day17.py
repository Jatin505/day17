Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: C:/python/Python37-32/day17/1.py =================
inputData:
 [[ 2.1 -1.9  5.5]
 [-1.5  2.4  3.5]
 [ 0.5 -7.9  5.6]
 [ 5.9  2.3 -5.8]]

Binarized data:
 [[1. 0. 1.]
 [0. 1. 1.]
 [0. 0. 1.]
 [1. 1. 0.]]
>>> 
================= RESTART: C:/python/Python37-32/day17/2.py =================
inputData:
 [[ 2.1 -1.9  5.5]
 [-1.5  2.4  3.5]
 [ 0.5 -7.9  5.6]
 [ 5.9  2.3 -5.8]]
mean= [ 1.75  -1.275  2.2  ]
std deviation= [2.71431391 4.20022321 4.69414529]
Traceback (most recent call last):
  File "C:/python/Python37-32/day17/2.py", line 9, in <module>
    data_scaled=preprocessing.scalar(input_data)
AttributeError: module 'sklearn.preprocessing' has no attribute 'scalar'
>>> 
================= RESTART: C:/python/Python37-32/day17/2.py =================
inputData:
 [[ 2.1 -1.9  5.5]
 [-1.5  2.4  3.5]
 [ 0.5 -7.9  5.6]
 [ 5.9  2.3 -5.8]]
mean= [ 1.75  -1.275  2.2  ]
std deviation= [2.71431391 4.20022321 4.69414529]
data_scaled:
 [[ 0.12894603 -0.14880162  0.70300338]
 [-1.19735598  0.8749535   0.27694073]
 [-0.46052153 -1.57729713  0.72430651]
 [ 1.52893149  0.85114524 -1.70425062]]
mean= [1.11022302e-16 0.00000000e+00 0.00000000e+00]
std deviation= [1. 1. 1.]
>>> 
================= RESTART: C:/python/Python37-32/day17/3.py =================
24 24

================= RESTART: C:/python/Python37-32/day17/4.py =================
Traceback (most recent call last):
  File "C:/python/Python37-32/day17/4.py", line 7, in <module>
    [174,15,0]
TypeError: list indices must be integers or slices, not tuple
>>> 
================= RESTART: C:/python/Python37-32/day17/4.py =================
Traceback (most recent call last):
  File "C:/python/Python37-32/day17/4.py", line 10, in <module>
    clf=xlf.fit(X,Y)
NameError: name 'xlf' is not defined
>>> 
================= RESTART: C:/python/Python37-32/day17/4.py =================
Traceback (most recent call last):
  File "C:/python/Python37-32/day17/4.py", line 11, in <module>
    prediction=clf.pedict([[120,10,1]])
AttributeError: 'DecisionTreeClassifier' object has no attribute 'pedict'
>>> 
================= RESTART: C:/python/Python37-32/day17/4.py =================
Traceback (most recent call last):
  File "C:/python/Python37-32/day17/4.py", line 12, in <module>
    priny(prediction)
NameError: name 'priny' is not defined
>>> 
================= RESTART: C:/python/Python37-32/day17/4.py =================
['woman']
>>> 
