# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================



"""

    🟢 Level 11: Missing Values, Duplicates & Data Quality
    
"""


import pandas as pd
  

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')



#  =====================================================================
#   🔵  201. Count missing values in every column.
#  =====================================================================

missing_values = df.isna().sum()

print(missing_values)       # isna() = har cell chack karta h ki value missing
                            #          h ya nhi 
                          
                            
# %%

#  =====================================================================
#   🔵  202. Display rows containing at least one missing value.
#  =====================================================================

missing_values = df[df.isna().any(axis=1)]

print(missing_values)


# %%

#  =====================================================================
#   🔵  203. Display rows where Marks is missing.
#  =====================================================================

misssing_values = df[df['Marks'].isna()]

print(missing_values)    # any(axis=1) - row mein koi bhi missing value hai kya

# %%

#  =====================================================================
#   🔵  204. Display rows where state is missing.
#  =====================================================================

missing_values = df[df['state'].isna()]

print(missing_values)

# %%

#  =====================================================================
#   🔵  205. Display rows where city is missing.
#  =====================================================================

missing_values = df[df['city'].isna()]

print(missing_values)

# %%

#  =====================================================================
#   🔵  206. Fill missing Marks with the median Marks.
#  =====================================================================

median_Marks = df['Marks'].median()    # median Marks dega

df['Marks'] = df['Marks'].fillna(median_Marks)

print(df)     # fillna - jaha Marks missing h waha median dega 

# %%

#  =====================================================================
#   🔵  207. Fill missing Marks with the mean Marks.
#  =====================================================================

mean_Marks = df['Marks'].mean()

df['Marks'] = df['Marks'].fillna(mean_Marks)

print(df)


# %%

#  =====================================================================
#   🔵  208. Fill missing categorical values with 'Unknown'.
#  =====================================================================




# %%

#  =====================================================================
#   🔵  209. Drop rows where Marks is missing.
#  =====================================================================

df = df.dropna(subset=['Marks'])      # subset = sirf Marks column check karega.

print(df)                        # jis row mw Marks NAN h puri row delete kr dega


# %%

#  =====================================================================
#   🔵  210. Drop rows where state or city is missing.
#  =====================================================================

df = df.dropna(subset =['state','city'])

print(df)


# %%

#  =====================================================================
#   🔵  211. Check for duplicated Srlno values.
#  =====================================================================

duplicated_Srlno = df[df['Srlno.'].duplicated()]    # srlno chack karega repet h ky

print(duplicated_Srlno)


# %%

#  =====================================================================
#   🔵  212. Display all duplicated Srlno records.
#  =====================================================================

# Keep=False -  duplicate Srlno ki first aur baaki sabhi occurrences dikhana. 

# occurrences -  kisi value ka kitni bar aana repeat hona

duplicated_Srlno = df[df['Srlno.'].duplicated(keep=False)]

print(duplicated_Srlno)


# %%

#  =====================================================================
#   🔵  213. Remove duplicate rows while keeping the first occurrence.
#  =====================================================================

# drop - hatana  

# Keep =First -  Agar same row 3 baar ha first ko rakhega baki delete

# drop_duplicates() - duplicate rows ko remove karta hai 

df = df.drop_duplicates(keep='first')

print(df)


# %%

#  =====================================================================
#   🔵  214. Remove duplicate rows while keeping the last occurrence.
#  =====================================================================

# drop         -  actual duplicate ko remove karta h
# keep='last' -  duplicate mein last row ko rakhta hai

df = df.drop_duplicates(keep='last')

print(df)


# %%

#  =====================================================================
#   🔵  215. Check whether center_num is unique within center_name.
#  =====================================================================

#  groupby('center_name') - har center name ka group banayega

#  .nunique() → unique center_num ki counting karega

check = df.groupby('center_name')['center_num'].nunique()

print(check)


# %%

#  =============================================================================
#   🔵  216. Check whether every row has a valid Marks value between 0 and 720.
#  =============================================================================

check = df['Marks'].between(0, 720).all()

print(check)          # all() - ky sabhi value True h 


# %%


#  =====================================================================
#   🔵  217. Display rows with Marks outside the valid 0–720 range.
#  =====================================================================

result = df[~df['Marks'].between(0, 720)]

print(result)     # ~ (Not) - unko ulta kar deta hai.


# %%

#  =====================================================================
#   🔵  218. Count invalid Marks values outside the range 0–720.
#  =====================================================================


result = (~df['Marks'].between(0, 720)).sum()

print(result)


# %%

#  =====================================================================
#   🔵  219. Check for blank strings in state, city, and center_name.
#  =====================================================================



#  =====================================================================
#   🔵  220. Replace blank strings with missing values.
#  =====================================================================