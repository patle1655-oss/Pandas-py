# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================



"""

    🟢 Level 12: Advanced Filtering & Comparative Analysis
    
"""


import pandas as pd

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#  =====================================================================
#   🔵  221. Find students scoring above the overall average Marks.
#  =====================================================================

average_Marks = df['Marks'].mean()    # pure data frame ke Marks ka avg

print(df[df['Marks'] > average_Marks])   # avg se jada Marks wale student



# %%

#  =====================================================================
#   🔵  222. Find students scoring below the overall average Marks.
#  =====================================================================

average_Marks = df['Marks'].mean()

print(df[df['Marks'] < average_Marks])



# %%

#  =====================================================================
#   🔵  223. Find students scoring equal to the maximum Marks.
#  =====================================================================

maximum_Marks = df['Marks'].max()

print(df[df['Marks'] == maximum_Marks])    



# %%

#  =====================================================================
#   🔵  224. Find students scoring equal to the minimum Marks.
#  =====================================================================

minimum_Marks = df['Marks'].min()

print(df[df['Marks'] == minimum_Marks])



# %%

#  =======================================================================
#   🔵  225. Find states whose average Marks exceed the national average.
#  =======================================================================

national_average = df['Marks'].mean()

state_average = df.groupby('state')['Marks'].mean()

print(state_average[state_average > national_average])



# %%

#  =====================================================================
#   🔵  226. Find cities whose average Marks exceed the overall average.
#  =====================================================================

overall_average = df['Marks'].mean()

city_average = df.groupby('city')['Marks'].mean()

print(city_average[city_average > overall_average])



# %%

#  ========================================================================
#   🔵  227. Find centres whose average Marks exceed the overall average.
#  ========================================================================

overage_average = df['Marks'].mean()

center_average = df.groupby('center_name')['Marks'].mean()

print(center_average[center_average > overall_average])



# %%

#  =====================================================================
#   🔵  228. Find students whose Marks exceed their state average.
#  =====================================================================

# transform('mean')  - har student ke saamne uske state ka average laga deta hai

state_average = df.groupby('state')['Marks'].transform('mean')

print(df[df['Marks'] > state_average])



# %%

#  =====================================================================
#   🔵  229. Find students whose Marks exceed their city average.
#  =====================================================================

city_average = df.groupby('city')['Marks'].transform('mean')

print(df[df['Marks'] > city_average])



# %%

#  =====================================================================
#   🔵  230. Find students whose Marks exceed their centre average.
#  =====================================================================

center_average = df.groupby('center_name')['Marks'].transform('mean')

print(df[df['Marks'] > center_average])



# %%

#  =====================================================================
#   🔵  231. Find the state with the highest average Marks.
#  =====================================================================

# highest k liy 'mean'() / 'max'()

highest_average = df.groupby('state')['Marks'].mean()

print(highest_average[highest_average == highest_average.max()])



# %%

#  =====================================================================
#   🔵  232. Find the state with the lowest average Marks.
#  =====================================================================

# lowest ke liy 'mean'() / 'min'()

lowest_average = df.groupby('state')['Marks'].mean()

print(lowest_average[lowest_average == lowest_average.min()])



# %%

#  =====================================================================
#   🔵  233. Find the city with the highest average Marks.
#  =====================================================================

highest_average = df.groupby('city')['Marks'].mean()

print(highest_average[highest_average == highest_average.max()])



# %%

#  =====================================================================
#   🔵  234. Find the city with the lowest average Marks.
#  =====================================================================

lowest_average = df.groupby('city')['Marks'].mean()

print(lowest_average[lowest_average == lowest_average.min()])



# %%

#  =====================================================================
#   🔵  235. Find the centre with the highest average Marks.
#  =====================================================================

highest_average = df.groupby('center_name')['Marks'].mean()

print(highest_average[highest_average == highest_average.max()])



# %%

#  =====================================================================
#   🔵  236. Find the centre with the lowest average Marks.
#  =====================================================================

lowest_average = df.groupby('center_name')['Marks'].mean()

print(lowest_average[lowest_average == lowest_average.min()])



# %%

#  =====================================================================
#   🔵  237. Find the state with the largest number of 650+ scorers.
#  =====================================================================

scorers = df[df['Marks'] >= 650]

state_count = scorers.groupby('state')['Marks'].count()

print(state_count[state_count == state_count.max()])



# %%

#  =====================================================================
#   🔵  238. Find the city with the largest number of 650+ scorers.
#  =====================================================================

scorers = df[df['Marks'] >= 650]

city_count = scorers.groupby('city')['Marks'].count()

print(city_count[city_count == city_count.max()])
      
      
      
# %%
      
#  =====================================================================
#   🔵  239. Find the centre with the largest number of 650+ scorers.
#  =====================================================================

scorers = df[df['Marks'] >= 650]

center_count = scorers.groupby('center_name')['Marks'].count()

print(center_count[center_count == center_count.max()])



# %%

#  =====================================================================
#   🔵  240. Find centres with more than the average number of students.
#  =====================================================================

center_count = df.groupby('center_name')['Marks'].count()

average_students = center_count.mean()

print(center_count[center_count > average_students])