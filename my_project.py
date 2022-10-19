#Final Version of The project 

import math
def NewFun(df):
    'retunrs maximum deviation * sqrt(2)'
    p= df.iloc[:,3].abs().max()
    p= p * math.sqrt(2)
    return p

def Mapped_points_total(self):
    'take the mapped test points and dataframe and returns the dimensions'
    if len(self.index) >100:
        print('Review your test points')
    else: 
        print('Your test points total is {}'.format(len(self.index)))
    
