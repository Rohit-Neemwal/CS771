import numpy as np
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
import time
import matplotlib.pyplot as plt
# You are allowed to import any submodules of sklearn as well e.g. sklearn.svm etc
# You are not allowed to use other libraries such as scipy, keras, tensorflow etc

# SUBMIT YOUR CODE AS A SINGLE PYTHON (.PY) FILE INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILE MUST BE submit.py
# DO NOT INCLUDE OTHER PACKAGES LIKE SCIPY, KERAS ETC IN YOUR CODE
# THE USE OF ANY MACHINE LEARNING LIBRARIES OTHER THAN SKLEARN WILL RESULT IN A STRAIGHT ZERO

# DO NOT CHANGE THE NAME OF THE METHODS my_fit, my_predict etc BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here
# For example, functions to calculate next coordinate or step length


################################
# Non Editable Region Starting #
################################
def my_fit( Z_train ):
################################
#  Non Editable Region Ending  #
################################

 __train__ = [[] for _ in range(120)]

 for curr in np.copy(Z_train) :
  p = int(np.array(curr[64:68]).T @ np.array([8,4,2,1]))
  q = int(np.array(curr[68:72]).T @ np.array([8,4,2,1]))
	
  if(p>q):
   __train__[int(p*(p-1)/2) + q].append(curr)
  else:
   curr[72] = 1-curr[72]
   __train__[int(q*(q-1)/2) + p].append(curr)

	# make distribution elements a  numpy array
 for i in range (120):
  __train__[i] = np.array(__train__[i])

 model = [LinearSVC(C = 0.3,tol = 0.216,penalty = 'l1',loss='hinge',dual = False) for _ in range(120)]

 for current in range(120):
  if(len(__train__[current])==0):print("empty list")
  else:
    X_train = __train__[current][:,0:64]
    Y_train = __train__[current][:,-1]
    model[current].fit(X_train,Y_train)
	
 return model					# Return the trained model


################################
# Non Editable Region Starting #
################################
def my_predict( X_tst, model ):

################################
#  Non Editable Region Ending  #
################################
 pred = []
 for curr in X_tst:
  p = int(np.array(curr[64:68]).T @ np.array([8,4,2,1]))
  q = int(np.array(curr[68:72]).T @ np.array([8,4,2,1]))

  if(p>q): pred.append(model[int(p*(p-1)/2) + q].predict([curr[0:64]])[0])
  else: pred.append(1-model[int(q*(q-1)/2) + p].predict([curr[0:64]])[0])
 return pred




Z_train= np.loadtxt("F:\CS771\CS771_A1\dummy\secret_train.dat")
X_tst = np.loadtxt("F:\CS771\CS771_A1\dummy\secret_test.dat")
t = time.time()
model = my_fit(Z_train)
print(time.time() -t)
pred = my_predict(X_tst, model)

print(np.average(X_tst[:,-1]==pred))

