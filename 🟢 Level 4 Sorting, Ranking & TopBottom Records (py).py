# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================



""""

     🟢  Level 4: Sorting, Ranking & Top/Bottom Records
       
"""





#  ===============================================================
#      🔵 61. Sort students by Marks in ascending order.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by='Marks', ascending=True)


#_________________________________________________________________________________________



#  ===============================================================
#      🔵 62. Sort students by Marks in descending order
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by='Marks',  ascending=True)

#________________________________________________________________________________________



#  ===============================================================
#      🔵 63. Sort students by state alphabetically.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by='state',  ascending=True)

#_________________________________________________________________________________________


#  ===============================================================
#      🔵 64. Sort students by city alphabetically.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by='city',  ascending=True)



#_________________________________________________________________________________________


#  ===============================================================
#      🔵 65. Sort students by center_name alphabetically.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by='center_name',  ascending=True)


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 66. Sort by state and then Marks.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by=['state','Marks'])


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 67. Sort by city and Marks in descending order.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by=['city','Marks'] ,  ascending=False)



#_________________________________________________________________________________________


#  ===============================================================
#      🔵 68. Sort by state ascending and Marks descending.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by=['state','Marks'] ,  ascending=[True,False])


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 69. Sort by center_name ascending and Marks descending.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by=['center_name','Marks'] ,  ascending=[True,False])


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 70. Display the top 20 scorers.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by='Marks', ascending = False).head(20)

#_________________________________________________________________________________________


#  ===============================================================
#      🔵 71. Display the bottom 20 scorers.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by='Marks', ascending = False).tail(20)


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 72. Display the top 50 scorers.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by='Marks', ascending = False).head(50)


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 73. Display the bottom 50 scorers.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by='Marks', ascending = False).tail(50)


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 74. Display the highest-scoring student.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by= 'Marks' , ascending = False).head(1)


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 75. Display the lowest-scoring student.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by= 'Marks' , ascending = False).tail(1)


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 76. Display the second-highest scorer.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by= 'Marks' , ascending = False).iloc[1]


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 77. Display the second-lowest scorer.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by= 'Marks' , ascending = True).iloc[1]


#_________________________________________________________________________________________


#  ===========================================================================
#      🔵 78. Display the top 10 scorers with only state, city, and Marks.
#  ===========================================================================


import pandas as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.sort_values(by= 'Marks' , ascending = False)[['state','city','Marks']].head(10)


#_________________________________________________________________________________________


#  ===============================================================
#      🔵 79. Display the top 10 scorers from a selected state.
#  ===============================================================


import pandas as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['state']=='MAHARASHTRA'].sort_values(by= 'Marks' , ascending = False).head(10)



#_________________________________________________________________________________________


#  ===============================================================
#      🔵 80. Display the top 10 scorers from a selected city.
#  ===============================================================


import pandas as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['city']=='RAIPUR'].sort_values(by= 'Marks' , ascending = False).head(10)

