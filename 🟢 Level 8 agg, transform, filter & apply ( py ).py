# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================


"""

    🟢 Level 8: agg, transform, filter & apply
        
"""




# ======================================================================
#    🔵 141. Use groupby().agg() to calculate count, mean, maximum, 
#           and minimum Marks by state
# ======================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('state').agg({'Marks':['count','mean','max','min']})


#_______________________________________________________________________________________________


# ======================================================================
#  🔵 142. Use groupby().agg() to calculate count, mean, and 
#              standard deviation by city.
# ======================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('city').agg({'Marks':['count','mean','std']})

#___________________________________________________________________________________________


# ======================================================================
#    🔵 143. Use groupby().agg() to calculate total and average Marks
#           by centre.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('center_name').agg({'Marks':['sum','mean']})

#_______________________________________________________________________________________________


# ======================================================================
#    🔵 144. Give meaningful names to aggregated columns for
#           state-level statistics.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

state_stats = df.groupby('state').agg(
    student_count=('Marks', 'count'),
    average_marks=('Marks', 'mean'),
    maximum_marks=('Marks', 'max'),
    minimum_marks=('Marks', 'min')
).reset_index()

print(state_stats)

#_______________________________________________________________________________________________


# ======================================================================
#    🔵 145. Calculate multiple aggregations for Marks by state
#           in one operation.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

state = df.groupby('state')['Marks'].agg(
    ['count','mean','max','min'])

print(state)


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 146. Calculate the number of students and average Marks
#           for each city.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

city = df.groupby('city').agg(
    student_count = ('Marks','count'),
    average_Marks = ('Marks','mean'))

print(city)


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 147. Calculate the number of students, total Marks, and
#           average Marks for each centre.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

center = df.groupby('center_name').agg(
    student_count = ('Marks','count'),
    average_Marks = ('Marks','mean'),
    total_Marks = ('Marks','sum'))

print(center)

#_______________________________________________________________________________________________


# ======================================================================
#    🔵 148. Filter states having more than 10,000 students using
#           groupby().filter().
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

state_count = df.groupby('state')['Marks'].count()

state_count = state_count[state_count > 10000]

print(state_count)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>lamda

#_______________________________________________________________________________________________


# ======================================================================
#    🔵 149. Filter cities having more than 5,000 students using
#           groupby().filter().
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

city_count = df.groupby('city')['Marks'].count()

city_count = city_count[city_count > 5000]

print(city_count)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>lamda
#_______________________________________________________________________________________________


# ======================================================================
#    🔵 150. Filter centres having more than 300 students using
#           groupby().filter().
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 151. Filter states whose average Marks exceed 450.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 152. Filter cities whose average Marks exceed 500.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 153. Filter centres whose average Marks exceed 550.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 154. Filter states where the maximum Marks exceed 700.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 155. Filter cities having at least 20 students scoring
#           above 650.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 156. Use transform() to add each student's state average Marks.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 157. Use transform() to add each student's city average Marks.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 158. Use transform() to add each student's centre average Marks.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 159. Use transform() to add the number of students in each
#           state to every row.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#_______________________________________________________________________________________________


# ======================================================================
#    🔵 160. Use transform() to calculate each student's percentage
#           of their state's total Marks.
# ======================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')