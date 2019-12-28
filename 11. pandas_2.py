import pandas as pd
import numpy as np
import timeit as ti

sports = pd.Series([110.0, 125.4, 73.5, 3., 67.97])

sum = 0
for s in sports :
    sum += s
print(sum)

# Same thing using Vectorization 
# A method of computation, which leverages simultaneous processing
# capabilities of modern computers.
#
# It works with most of the functions in numpy and pandas library.
#
print(np.sum(sports))

################################
# Test Vectorization performance
################################
mysetup = '''
import pandas as pd
import numpy as np
'''

def method1(sports):
    sum = 0
    for s in sports :
        sum += s
    return(sum)

def method2(sports):
    return(np.sum(sports))

numbers = pd.Series(np.random.randint(0,10000,10000))

t1 = ti.repeat(setup = mysetup, stmt = '''
from __main__ import method1
from __main__ import numbers
method1(numbers)
''', repeat = 3, number = 500)

print('Method 1 Time : {}'.format(min(t1)))

t2 = ti.repeat(setup = mysetup, stmt = '''
from __main__ import method2
from __main__ import numbers
method2(numbers)
''', repeat = 3, number = 500)

print('Method 2 Time : {}'.format(min(t2)))
