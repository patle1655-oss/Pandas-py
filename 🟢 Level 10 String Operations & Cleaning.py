# =========================================================
#   🔴  NEET_Pandas_300_Practice_Questions 
# =========================================================


"""

    🟢 Level 10: String Operations & Cleaning
    
"""


import pandas as pd
       

df = pd.read_csv(r'C:\Users\User\Downloads\all_neet_marks_2607.csv')


#  =====================================================================
#   🔵  181. Convert state names to uppercase.
#  =====================================================================

df['state'] = df['state'].str.upper()

print(df[['state']].head())


# %%

#  =====================================================================
#   🔵  182. Convert city names to lowercase.
#  =====================================================================

df['city'] = df['city'].str.lower()

print(df[['city']].head())


# %%


#  =====================================================================
#   🔵  183. Remove leading and trailing spaces from state values.
#  =====================================================================

df['state'] = df['state'].str.strip()

print(df[['state']].head())
   
#.str.strip() → starting aur ending ke extra spaces remove karta hai.


# %%


#  =====================================================================
#   🔵  184. Remove leading and trailing spaces from city values.
#  =====================================================================

df['city'] = df['city'].str.strip()

print(df[['city']].head())


# %%


#  =========================================================================
#   🔵  185. Find rows where city contains a specific word, ignoring case.
#  =========================================================================

result =df[df['city'].str.contains('pur', case=False, na=False)]

print(result)


# %%


#  =====================================================================
#   🔵  186. Find rows where center_name contains 'school', ignoring case.
#  =====================================================================

result =df[df['center_name'].str.contains('school', case=False, na=False)]

print(result)


# %%


#  =====================================================================
#   🔵  187. Extract the first word from center_name.
#  =====================================================================

df['first_word'] = df['center_name'].str.split().str[0]

print(df[['center_name', 'first_word']].head())


# %%


#  =====================================================================
#   🔵  188. Extract the last word from center_name.
#  =====================================================================

# str.split() → sentence ko words me todta hai.

df['last_word'] = df['center_name'].str.split().str[-1]

print(df[['center_name', 'last_word']].head())

# %%

#  =====================================================================
#   🔵  189. Find the length of each state name.
#  =====================================================================

# str.len → string me kitne characters hain, wo count karta hai.

df['State_length'] = df['state'].str.len()

print(df[['state', 'State_length']].head())

# %%


#  =====================================================================
#   🔵  190. Find the length of each city name.
#  =====================================================================

df['city_length'] = df['city'].str.len()

print(df[['city', 'city_length']].head())


# %%

#  =====================================================================
#   🔵  191. Find the length of each centre name.
#  =====================================================================

df['center_length'] = df['center_name'].str.len()

print(df[['center_name', 'center_length']])

# %%

#  =====================================================================
#   🔵  192. Replace a selected word in center_name with another word.
#  =====================================================================

# case=False → Capital/small ignore

df['center_name_new'] = df['center_name'].str.replace(
    'SHCOOL', 'COLLEGE', case=False, regex=False)

print(df[['center_name', 'center_name_new']].head())

# %%

#  =====================================================================
#      🔵 193. Replace multiple variations of a centre name with a 
#                standard value.
#  =====================================================================



# %%

#  =====================================================================
#   🔵  194. Check whether city values start with a particular prefix.
#  =====================================================================

df['city_start'] = df['city'].str.upper().str.startswith('Ra', na=False)

print(df[['city', 'city_start']].head())

# %%

#  =====================================================================
#   🔵  195. Check whether city values end with a particular suffix.
#  =====================================================================

df['city_end'] = df['city'].str.upper().str.endswith('PUR', na=False)

print(df[['city', 'city_end']].head())

# %%

#  =====================================================================
#   🔵  196. Split center_name into separate words.
#  =====================================================================

# .str.split() string ko space ke basis par alag-alag words mein todta hai.

df['center_words'] = df['center_name'].str.split()

print(df[['center_name', 'center_words']].head())

# %%

#  =====================================================================
#   🔵  197. Extract a specific part of center_name using string slicing.
#  =====================================================================

#  .str - string operation

#  [:5] - first 5 characters

result = df['center_name'].str[:5]

print(result)


# %%

#  =====================================================================
#   🔵  198. Find the number of spaces in each center_name.
#  =====================================================================

# .str.count(' ') - har center_name me kitne space " " hain wo count karta hai

result = df['center_name'].str.count(' ')

print(result)


# %%

#  =====================================================================
#   🔵  199. Create a standardized version of state and city names.
#  =====================================================================



#  =====================================================================
#   🔵  200. Find duplicate centre names after converting them to lowercase.
#  =====================================================================