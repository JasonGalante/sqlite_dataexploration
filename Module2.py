import pandas as pd
import sqlite3

# Step 1: Step 1: Find a Public Healthcare Dataset
# Found Leading_Causes_of_Death.csv

# Step 2:Set Up a Local SQLite Database
# Use Pandas to load your dataset into the SQLite database

conn = sqlite3.connect('Death_Cause_database.db')
df = pd.read_csv('C:\\Users\\grift\\OneDrive\\Documents\\GitHub\\sqlite_dataexploration\\Leading_Causes_of_Death.csv')
# Practiced loading from website instead of local
# Practice code:df = pd.read_csv('https://data.cdc.gov/resource/bi63-dtpu.csv')
# Save the DataFrame to the SQLite database
df.to_sql('Deaths_By_State', conn, if_exists='replace', index=False)

#test to make sure .csv is loaded into df
df

#Step 3:Perform SQL Queries Using SQLite and Pandas
# Query 1: Select all records based on a specific filter of your choice (e.g., a particular value in one of the columns)
query = """
SELECT * 
FROM Deaths_By_State
WHERE State = "Colorado"
"""
result_df = pd.read_sql(query, conn)
result_df

# Query 2: Count the number of records that meet a certain condition (e.g., count the number of entries for a specific category).
query1 = """
SELECT COUNT(Deaths) as "Total_Deaths"
FROM Deaths_By_State
WHERE State = "Colorado"
"""
result1_df = pd.read_sql(query1, conn)
result1_df

# Query 3: Group the data by a specific column and calculate a summary statistic (e.g., average, sum, count) for each group.
query2 = """
Select SUM(Deaths) as "Total_Deaths"
FROM Deaths_By_State
"""
result2_df = pd.read_sql(query2, conn)
result2_df

# Query 4: Sort the records based on a numerical or categorical field and return a limited set of results (e.g., top 5 records).
query4 = """
SELECT * 
FROM Deaths_By_State
WHERE State !="United States" 
ORDER BY Deaths DESC
LIMIT 5
"""
result4_df = pd.read_sql(query4, conn)
result4_df


# Close the connection
conn.close()