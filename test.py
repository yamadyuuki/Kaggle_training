import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(6, 4), index=pd.date_range(
    '20170101', periods=6), columns=['A', 'B', 'C', 'D'])
print(df)
