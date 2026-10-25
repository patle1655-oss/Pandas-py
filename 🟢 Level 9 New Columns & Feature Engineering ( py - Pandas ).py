# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================


"""

    🟢 Level 9: New Columns & Feature Engineering
    
"""


import pandas as pd  

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#  =====================================================================
#   🔵 161. Create a column Pass_Fail where students scoring at least 
#          300 are Pass, otherwise Fail.
#  =====================================================================

df['Pass_Fail'] = 'Fail'

df.loc[df['Marks'] >= 300, 'Pass_Fail'] = 'Pass'
 
print(df[['Marks', 'Pass_Fail']].head(20))

#____________________________________________________________________________________



#  ================================================================
#    🔵 162. Create a Grade column with A/B/C/D based on Marks.
#  ================================================================

df['Grade'] = 'D'

df.loc[df['Marks'] >= 300, 'Grade'] = 'C'
df.loc[df['Marks'] >= 450, 'Grade'] = 'B'
df.loc[df['Marks'] >= 600, 'Grade'] = 'A'

print(df[['Marks', 'Grade']].head(20))


#_____________________________________________________________________________________________



#  ============================================================================
#    🔵 163. Create score bands such as 0–100, 101–200, 201–300, and so on.
#  ============================================================================




#________________________________________________________________________________________



#  ========================================================
#    🔵 164. Create a Score_Band column using pd.cut().
#  ========================================================


#________________________________________________________________________________________



#  ========================================================
#    🔵 165. Count students in each Score_Band.
#  ========================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#___________________________________________________________________________________________



#  ============================================================
#    🔵 166. Create a High_Medium_Low column based on Marks.
#  ============================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#_____________________________________________________________________________________



#  ====================================================================
#    🔵 167. Create a Scholarship_Eligible column based on a chosen 
#           Marks threshold.
#  ====================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#______________________________________________________________________________________



#  =============================================================================
#   🔵 168. Create a Performance_Category column with at least four categories.
#  =============================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#________________________________________________________________________________________



#  =============================================================================
#🔵 169. Calculate the numeric percentage equivalent assuming Marks are out of 720.
#  =============================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#_____________________________________________________________________________________________



#  =============================================================================
#   🔵 170. Create a column indicating whether a student scored 600 or more.
#  =============================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#___________________________________________________________________________________________


#  =============================================================================
#   🔵 171. Create a column indicating whether a student scored 650 or more.
#  =============================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#________________________________________________________________________________________


#  =============================================================================
#   🔵 172. Create a column indicating whether a student scored 700 or more.
#  =============================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#____________________________________________________________________________________________



#  =============================================================================
#   🔵 173. Create a column indicating whether a student scored exactly 720.
#  =============================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')




#_______________________________________________________________________________________



#  =============================================================================
#    🔵 174. Create a column indicating whether a student scored below 200.
#  =============================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#_____________________________________________________________________________________________



#  =============================================================================
#     🔵 175. Create a column containing the length of each city name.
#  =============================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#__________________________________________________________________________________________



#  =============================================================================
#     🔵 176. Create a column containing the length of each centre name
#  =============================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#_________________________________________________________________________________________


#  =============================================================================
#     🔵 177. Create a column containing the first letter of each city
#  =============================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#____________________________________________________________________________________________



#  =============================================================================
#     🔵 178. Create a column containing the first letter of each state.
#  =============================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#_____________________________________________________________________________________________



#  =============================================================================
#    🔵 179. Create a column combining state and city into one location label.
#  =============================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')




#_____________________________________________________________________________________________


#  =============================================================================
#    🔵 180. Create a column combining city and centre name into one label
#  =============================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

