# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================

"""

    🟢 Level 7: groupby Operations
    
"""


# ======================================================================
#   🔵 121. Find the number of students in each state using groupby().
# ======================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('state').size()              # size ( group ke under row count karna )

#_________________________________________________________________________________________


# ======================================================================
#   🔵 122. Find the number of students in each city using groupby().
# ======================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('city').size()


#_________________________________________________________________________________________


# ======================================================================
#   🔵 123. Find the number of students in each centre using groupby().
# ======================================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('center_name').size()

#_________________________________________________________________________________________


# ==================================================
#     🔵 124. Find the average Marks by state.
# ==================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('state').agg({'Marks':'mean'})

#_________________________________________________________________________________________


# ================================================
#    🔵 125. Find the average Marks by city.
# ================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('city').agg({'Marks':'mean'})

#_________________________________________________________________________________________



# ===============================================================
#   🔵 126. Find the average Marks by examination centre.
# ===============================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('center_name').agg({'Marks':'mean'})


#_________________________________________________________________________________________


# ===============================================================
#    🔵 127. Find the maximum Marks by state.
# ===============================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('state').agg({'Marks':'max'})

#_________________________________________________________________________________________


#  ===============================================
#    🔵 128. Find the minimum Marks by state.
#  ===============================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('state').agg({'Marks':'min'})

#_________________________________________________________________________________________


# ===============================================
#    🔵 129. Find the maximum Marks by city.
# ===============================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('city').agg({'Marks':'max'})

#_________________________________________________________________________________________


# =============================================
#   🔵 130. Find the minimum Marks by city.
# =============================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('city').agg({'Marks':'min'})

#_________________________________________________________________________________________


# ==============================================
#   🔵 131. Find the maximum Marks by centre.
# ==============================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('center_name').agg({'Marks':'max'})

#_________________________________________________________________________________________



# ===============================================
#   🔵 132. Find the minimum Marks by centre.
# ===============================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('center_name').agg({'Marks':'min'})

#_________________________________________________________________________________________


# ===============================================
#   🔵 133. Find the total Marks by state.
# ===============================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('state').agg({'Marks':'sum'})

#_________________________________________________________________________________________


# =============================================
#    🔵 134. Find the total Marks by city.
# =============================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('city').agg({'Marks':'sum'})

#_________________________________________________________________________________________


# =============================================
#   🔵 135. Find the total Marks by centre.
# =============================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('center_name').agg({'Marks':'sum'})

#_________________________________________________________________________________________


# =============================================
#   🔵 136. Find the median Marks by state.
# =============================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('state').agg({'Marks':'median'})


#_________________________________________________________________________________________


# ===========================================
#   🔵 137. Find the median Marks by city.
# ===========================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('city').agg({'Marks':'median'})

#_________________________________________________________________________________________


#   ===========================================================
#    🔵 138. Find the standard deviation of Marks by state.
#   ===========================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('state').agg({'Marks':'std'})

#_________________________________________________________________________________________


#  ===========================================================
#    🔵 139. Find the standard deviation of Marks by city.
#  ===========================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df.groupby('city').agg({'Marks':'std'})

#_________________________________________________________________________________________


# ============================================================
#   🔵 140. Find the number of 650+ scorers in each state.
# ============================================================

import pandas as pd

import numpy as np        

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')

df[df['Marks'] >= 650].groupby('state').size()

#_________________________________________________________________________________________


