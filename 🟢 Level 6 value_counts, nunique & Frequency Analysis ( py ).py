# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================


"""

     🟢 Level 6: value_counts, nunique & Frequency Analysis
     
"""


# ===========================================================================
#   🔵 101. Count the number of students in each state using value_counts().
# ============================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['state'].value_counts()


#_____________________________________________________________________________________________



# ===============================================================
#      🔵 102. Count the number of students in each city.
# ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['city'].value_counts()


#_________________________________________________________________________________________



# ===============================================================
#   🔵 103. Count the number of students in each centre.
# ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['center_name'].value_counts()

#_________________________________________________________________________________________



# ===============================================================
#    🔵 104. Display the top 10 states by number of students.
# ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['state'].value_counts().head(10)


#_________________________________________________________________________________________



# ===============================================================
#    🔵 105. Display the top 10 cities by number of students.
# ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['city'].value_counts().head(10)


#_________________________________________________________________________________________



# ===============================================================
#   🔵 106. Display the top 10 centres by number of students.
# ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['center_name'].value_counts().head(10)


#_________________________________________________________________________________________



# ================================================================
#   🔵 107. Display the bottom 10 states by number of students.
# ================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['state'].value_counts().tail(10)


#_________________________________________________________________________________________



# ================================================================
#   🔵 108. Display the bottom 10 cities by number of students.
# ================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['city'].value_counts().tail(10)



#_________________________________________________________________________________________



# ==================================================================
#    🔵 109. Display the bottom 10 centres by number of students.
# ==================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['center_name'].value_counts().tail(10)


#_________________________________________________________________________________________



#  ==============================================
#    🔵 110. Find the number of unique states
#  ==============================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['state'].nunique()


#_________________________________________________________________________________________



# ===============================================================
#     🔵 111. Find the number of unique cities.
# ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['city'].nunique()


#_________________________________________________________________________________________



# ===============================================================
#    🔵 112. Find the number of unique examination centres.
# ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['center_name'].nunique()


#_________________________________________________________________________________________



# ===============================================================
#     🔵 113. Find the most common state.
# ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['state'].value_counts().head(1)


#_________________________________________________________________________________________



# ===============================================================
#     🔵 114. Find the most common city.
# ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['city'].value_counts().head(1)


#_________________________________________________________________________________________



# ===============================================================
#      🔵 115. Find the most common examination centre.
# ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['center_name'].value_counts().head(1)


#_________________________________________________________________________________________



# ===============================================================
#        🔵 116. Find the least common state.
# ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['state'].value_counts().tail(1)


#_________________________________________________________________________________________



# ===============================================================
#       🔵 117. Find the least common city.
# ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['city'].value_counts().tail(1)


#_________________________________________________________________________________________



# ===============================================================
#       🔵 118. Find the least common examination centre.
# ===============================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['center_name'].value_counts().tail(1)


#_________________________________________________________________________________________



# ===============================================================
#      🔵 119. Create a frequency table of Marks.
# ===============================================================

import pandas as pd           

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df['Marks'].value_counts()


#_________________________________________________________________________________________



# =====================================================================
#    🔵 120. Create a frequency table of state and city combinations.
# =====================================================================

import pandas as pd

import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df[['state','city']].value_counts()


#_________________________________________________________________________________________
