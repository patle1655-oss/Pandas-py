# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================



"""

   🟢   Level 3: Filtering with Boolean Conditions

"""



#  ===============================================================
#      🔵 41. Display students who scored more than 650 marks.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['Marks']> 650, ] 



#__________________________________________________________________________________________________



#  ============================================================
#    🔵 42. Display students who scored less than 200 marks.
#  ============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['Marks']< 200 ,]


#____________________________________________________________________________________________



#  ===================================================================
#    🔵 43. Display students who scored between 500 and 600 marks
#  ===================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[(df['Marks']>= 500 )  &  (df['Marks']<= 600 ), ]

#___________________________________________________________________________________________



#  ==========================================================
#    🔵 44. Display students who scored exactly 720 marks.
#  ==========================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['Marks']== 720 ]



#________________________________________________________________________________________



#  ================================================
#     🔵 45. Display students who scored 0 marks
#  ================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['Marks']== 0]


#_______________________________________________________________________________________



#  ========================================================================
#   🔵 46. Display students whose Marks are greater than or equal to 600.
#  ========================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['Marks']>= 600 ]

#_______________________________________________________________________________________



#  ======================================================================
#    🔵 47. Display students whose Marks are less than or equal to 300
#  ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['Marks'] <= 300 ]


#__________________________________________________________________________________________



#  ===============================================================
#     🔵 48. Display students whose Marks are not equal to 0
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['Marks']!= 0]


#______________________________________________________________________________________________________



#  ======================================================
#     🔵 49. Display students from a particular state.
#  ======================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['state']  == 'CHHATTISGARH' ]


#__________________________________________________________________________________________


#  ===================================================
#   🔵 50. Display students from a particular city.
#  ===================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['city'] == 'RAIPUR']

#___________________________________________________________________________________________


#  ==================================================================
#    🔵 51. Display students from a particular examination centre
#  ==================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['center_name'] == 'GARDEN HIGH SCHOOL' ]


#_________________________________________________________________________________________


#  ===================================================================
#     🔵 52. Display students not belonging to a particular state.
#  ===================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['state'] != 'CHHATTISGARH']

#___________________________________________________________________________________



#  ===============================================================
#     🔵 53. Display students whose Marks are 600, 610, or 620 
#  ===============================================================

import pandas as pd

import numpy as np                   # | sabhi condition true hogi

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[(df['Marks'] == 600) | (df['Marks'] == 610) | (df['Marks'] == 620)]


#________________________________________________________________________________________________



#  ==================================================================
#    🔵 54. Display students whose city starts with the letter A.
#  ==================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['city'].str.startswith('A')]

# ___________________________________________________________________________________________


#  ==============================================================
#    🔵 55. Display students whose city ends with the letter A
#  ==============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.loc[df['city'].str.endswith('A')]

#________________________________________________________________________________________


#  ===============================================================
#   🔵 56. Display students whose city contains the word 'pur'.
#  ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

/////////////////////


#_________________________________________________________________________________________________



#  ======================================================================
#   🔵 57. Display students whose center_name contains 'Public School'
#  ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

///////////////////////////

#_____________________________________________________________________________________________



#  ======================================================================
#   🔵 58. Display students whose center_name contains the word 'School'
#  ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

/////////////


#_____________________________________________________________________________________





#  ======================================================================
#   🔵 59. Display students whose state starts with a specific letter
#  ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#_________________________________________________________________________________________



#  ===========================================================================
#   🔵 60. Display students whose state name contains a specific substring.
#  ===========================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')
