# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================



"""
     🟢  Level 14: Merging, Joining & Relational-Style Operations
    
"""


import pandas as pd    

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#  =============================================================================
#   🔵  261. Create a state-level summary DataFrame containing student count 
#             and average Marks.
#  =============================================================================

state_summary = df.groupby('state').agg(
    student_count = ('Marks','count'),
    average_Marks = ('Marks','mean')
    ).reset_index()

print(state_summary)


# %%

#  ===========================================================================
#   🔵  262. Create a city-level summary DataFrame containing student count 
#               and average Marks.
#  ===========================================================================

city_summary = df.groupby('city').agg(
    student_count = ('Marks','count'),
    avrage_Marks = ('Marks','mean')
    ).reset_index()

print(city_summary)


# %%

#  ==========================================================================
#   🔵  263. Merge the state-level summary back into the original DataFrame.
#  ==========================================================================

state_summary = df.groupby('state').agg(
    student_count = ('Marks','count'),
    avrage_Marks  = ('Marks','mean')
    ).reset_index()

df_merged = df.merge(
    state_summary,
    on = 'state',
    how = 'left'
    )

print(df_merged)


# %%

#  ==========================================================================
#   🔵  264. Merge the city-level summary back into the original DataFrame.
#  ==========================================================================

city_summary = df.groupby('city').agg(
    student_count = ('Marks','count'),
    avrage_Marks  = ('Marks','mean')
    ).reset_index()

df_merged = df.merge(
    city_summary,
    on = 'city',
    how = 'left'
    )

print(df_merged)


# %%

#  ==========================================================================
#   🔵  265. Merge a centre-level summary back into the original DataFrame.
#  ==========================================================================

center_summary = df.groupby('center_num').agg(
    student_count = ('Marks','count'),
    avrage_Marks = ('Marks','mean')
    ).reset_index()

df_merged = df.merge(
    center_summary,
    on = 'center_num',
    how = 'left'
    )

print(df_merged)


# %%

#  =====================================================================
#   🔵  266. Join state-level statistics to each student record.
#  =====================================================================

state_summary = df.groupby('state').agg(
    student_count = ('Marks','count'),
    avrage_Marks = ('Marks','mean')
    ).reset_index()

df_merged = df.merge(
    state_summary ,
    on = 'state',
    how = 'left'
    )

print(df_merged)


# %%

#  =====================================================================
#   🔵  267. Join city-level statistics to each student record.
#  =====================================================================

# City-level statistics

city_stats = df.groupby('city').agg(
    city_student_count=('Marks', 'count'),
    city_average_marks=('Marks', 'mean')
).reset_index()

# Original data ke saath merge

df2 = df.merge(city_stats, on='city', how='left')

print(df2)


# %%

#  =====================================================================
#   🔵  268. Create separate DataFrames for state totals and state 
#              averages, then merge them.
#  =====================================================================



#  =====================================================================
#   🔵  269. Create separate DataFrames for city totals and city averages
#            , then merge them.
#  =====================================================================



#  =====================================================================
#   🔵  270. Merge two summaries using state as the key.
#  =====================================================================



#  =====================================================================
#   🔵  271. Merge two summaries using city as the key.
#  =====================================================================



#  =====================================================================
#   🔵  272. Create a centre-to-city mapping DataFrame and join it to student data.
#  =====================================================================



#  =====================================================================
#   🔵  273. Identify records that do not match during a merge using an indicator column.
#  =====================================================================



#  =====================================================================
#   🔵  274. Perform a left merge between student data and state statistics.
#  =====================================================================



#  =====================================================================
#   🔵  275. Perform an inner merge between student data and city statistics.
#  =====================================================================



#  =====================================================================
#   🔵  276. Perform an outer merge between two summary DataFrames.
#  =====================================================================



#  =====================================================================
#   🔵  277. Use merge validation to check whether a state-level merge is one-to-many.
#  =====================================================================



#  =====================================================================
#   🔵  278. Merge state and city summaries to create a combined location report.
#  =====================================================================



#  =====================================================================
#   🔵  279. Compare two summary DataFrames and identify states with changed averages.
#  =====================================================================



#  =====================================================================
#   🔵  280. Create a table containing each state, its average Marks, and national average.
#  =====================================================================