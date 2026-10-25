# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================



"""

   🟢 Level 5: Aggregations & Descriptive Statistics
      
"""


#  ===============================================================
#      🔵 81. Find the maximum Marks.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

print(max(df['Marks']))



#_________________________________________________________________________________________


#  ===============================================================
#      🔵 82. Find the minimum Marks.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

print(min(df['Marks']))


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 83. Find the average Marks.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

print(df['Marks'].mean())                   # step change

#_________________________________________________________________________________________


#  ===============================================================
#      🔵 84. Find the median Marks.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

print(df['Marks'].median())                   # marks ki middel value nikalega 
#_________________________________________________________________________________________


#  ===============================================================
#      🔵 85. Find the standard deviation of Marks.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

print(df['Marks'].std()) 

#_________________________________________________________________________________________


#  ===============================================================
#      🔵 86. Find the variance of Marks.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

print(df['Marks'].var()) 

#_________________________________________________________________________________________


#  ===============================================================
#      🔵 87. Find the total Marks scored by all students.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

print(df['Marks'].sum()) 


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 88. Find the range between maximum and minimum Marks.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

print(df['Marks'].max() - df['Marks'].min())

#_________________________________________________________________________________________


#  ===============================================================
#      🔵 89. Find the 25th percentile of Marks.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

???????????????????????????


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 90. Find the 50th percentile of Marks.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

??????????????????????????


#__________________________________________________________________________________


#  ===============================================================
#      🔵 91. Find the 75th percentile of Marks.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

?????????????????????????????


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 92. Find the 90th percentile of Marks.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

???????????????


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 93. Find the 95th percentile of Marks.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

???????????????????????


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 94. Find the number of students.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

print(len(df))


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 95. Count the number of non-null Marks values.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

print(df['Marks'].count())


#_________________________________________________________________________________________


#  ===============================================
#    🔵 96. Count students scoring above 600.
#  ===============================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 97. Count students scoring below 300.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#_________________________________________________________________________________________


#  ===============================================================
#      🔵 98. Count students scoring between 500 and 600.
#  ===============================================================


import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#_________________________________________________________________________________________


#  ===============================================================
#      🔵 99. Count students scoring exactly 720.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#_________________________________________________________________________________________


#  ===============================================================
#      🔵 100. Count students scoring exactly 0.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

