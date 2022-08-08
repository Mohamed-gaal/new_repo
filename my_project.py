# Lets test the final Version of The project 

import math
def NewFun(df):
    'retunrs maximum deviation * sqrt(2)'
    p= df.iloc[:,3].abs().max()
    p= p * math.sqrt(3)
    return p


