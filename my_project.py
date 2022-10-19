#Final Version of The project 

import math
def NewFun(df):
    'retunrs maximum deviation * sqrt(2)'
    p= df.iloc[:,3].abs().max()
    p= p * math.sqrt(2)
    return p
def Mapped_test_total(self):
    if len(self.index) >100:
        print('mapped test points are out of bound')
    else:
        print('mapped test points are {}'.format(len(self.index)))
    


    
