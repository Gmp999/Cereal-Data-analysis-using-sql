# Example Python code for connecting to MySQL database using
import mysql.connector
import pandas as pd
# Replace 'your_username', 'your_password', 'your_host', and 'your_database' with
connection = mysql.connector.connect(
user='root',
password='1234',
host='localhost',
database='sprint2prj'
)
# Create a cursor object to execute SQL queries
cursor = connection.cursor()
# Query data from the 'customer' table
cursor.execute('SELECT * FROM cerealinformation')
#After fetching data from the database we are storing it into Pandas DataFrame
customer_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in
cursor.description])
# Query data from the 'product' table
cursor.execute('SELECT * FROM nutritionalinformation')
product_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in
cursor.description])
# Query data from the 'order_details' table
cursor.execute('SELECT * FROM servinginformation')
order_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in
cursor.description])
#printing first 5 records from each table
print(customer_data.head())
print(product_data.head())
print(order_data.head())
                        name mfr type  shelf
0                  100% Bran   N    C      3
1          100% Natural Bran   Q    C      3
2                   All-Bran   K    C      3
3  All-Bran with Extra Fiber   K    C      3
4             Almond Delight   R    C      3
                        name  calories  protein  fat  sodium  fiber  carbo  \
0                  100% Bran        70        4    1     130   10.0    5.0   
1          100% Natural Bran       120        3    5      15    2.0    8.0   
2                   All-Bran        70        4    1     260    9.0    7.0   
3  All-Bran with Extra Fiber        50        4    0     140   14.0    8.0   
4             Almond Delight       110        2    2     200    1.0   14.0   

   sugars  potass  vitamins  
0       6     280        25  
1       8     135         0  
2       5     320        25  
3       0     330        25  
4       8      -1        25  
                        name  weight  cups   rating
0                  100% Bran     1.0  0.33  68.4030
1          100% Natural Bran     1.0  1.00  33.9837
2                   All-Bran     1.0  0.33  59.4255
3  All-Bran with Extra Fiber     1.0  0.50  93.7049
4             Almond Delight     1.0  0.75  34.3848
pip install mysql;
Collecting mysql
  Downloading mysql-0.0.3-py3-none-any.whl.metadata (746 bytes)
Collecting mysqlclient (from mysql)
  Downloading mysqlclient-2.2.4-cp311-cp311-win_amd64.whl.metadata (4.6 kB)
Downloading mysql-0.0.3-py3-none-any.whl (1.2 kB)
Downloading mysqlclient-2.2.4-cp311-cp311-win_amd64.whl (203 kB)
   ---------------------------------------- 0.0/203.2 kB ? eta -:--:--
   ---------------------------------------- 0.0/203.2 kB ? eta -:--:--
   -- ------------------------------------- 10.2/203.2 kB ? eta -:--:--
   -- ------------------------------------- 10.2/203.2 kB ? eta -:--:--
   -- ------------------------------------- 10.2/203.2 kB ? eta -:--:--
   ----------------- --------------------- 92.2/203.2 kB 581.0 kB/s eta 0:00:01
   ----------------- --------------------- 92.2/203.2 kB 581.0 kB/s eta 0:00:01
   ----------------- --------------------- 92.2/203.2 kB 581.0 kB/s eta 0:00:01
   ----------------- --------------------- 92.2/203.2 kB 581.0 kB/s eta 0:00:01
   -------------------------- ----------- 143.4/203.2 kB 387.0 kB/s eta 0:00:01
   -------------------------- ----------- 143.4/203.2 kB 387.0 kB/s eta 0:00:01
   -------------------------- ----------- 143.4/203.2 kB 387.0 kB/s eta 0:00:01
   -------------------------------- ----- 174.1/203.2 kB 349.3 kB/s eta 0:00:01
   -------------------------------- ----- 174.1/203.2 kB 349.3 kB/s eta 0:00:01
   -------------------------------- ----- 174.1/203.2 kB 349.3 kB/s eta 0:00:01
   ------------------------------------ - 194.6/203.2 kB 294.9 kB/s eta 0:00:01
   -------------------------------------- 203.2/203.2 kB 301.0 kB/s eta 0:00:00
Installing collected packages: mysqlclient, mysql
Successfully installed mysql-0.0.3 mysqlclient-2.2.4
Note: you may need to restart the kernel to use updated packages.
pip install mysql-connector-python
Requirement already satisfied: mysql-connector-python in c:\users\gouth\anaconda3\lib\site-packages (8.4.0)
Note: you may need to restart the kernel to use updated packages.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the CSV file
cereal_data = pd.read_csv("D:\\Downloads\\archive\\cereal.csv")

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# 1. Bar Plot for Average Calories by Manufacturer
plt.figure(figsize=(12, 6))
avg_calories = cereal_data.groupby('mfr')['calories'].mean().reset_index()
sns.barplot(x='mfr', y='calories', data=avg_calories)
plt.title('Average Calories by Manufacturer')
plt.xlabel('Manufacturer')
plt.ylabel('Average Calories')
plt.show()

# 2. Line Plot for Rating by Fiber Content
plt.figure(figsize=(12, 6))
sorted_data = cereal_data.sort_values('fiber')
sns.lineplot(x='fiber', y='rating', data=sorted_data, marker='o')
plt.title('Rating by Fiber Content')
plt.xlabel('Fiber (grams)')
plt.ylabel('Rating')
plt.show()

# 3. Pie Chart for Distribution of Cereal Types
plt.figure(figsize=(8, 8))
type_counts = cereal_data['type'].value_counts()
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Cereal Types')
plt.show()

# 4. Bar Plot for Total Sugars by Shelf Position
plt.figure(figsize=(12, 6))
total_sugars = cereal_data.groupby('shelf')['sugars'].sum().reset_index()
sns.barplot(x='shelf', y='sugars', data=total_sugars)
plt.title('Total Sugars by Shelf Position')
plt.xlabel('Shelf Position')
plt.ylabel('Total Sugars (grams)')
plt.show()

# 5. Scatter Plot for Sodium vs. Potassium
plt.figure(figsize=(12, 6))
sns.scatterplot(x='sodium', y='potass', data=cereal_data, hue='type', style='type', s=100)
plt.title('Sodium vs. Potassium in Cereals')
plt.xlabel('Sodium (mg)')
plt.ylabel('Potassium (mg)')
plt.legend(title='Type', loc='upper right')
plt.show()
No description has been provided for this image
C:\Users\gouth\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
C:\Users\gouth\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
No description has been provided for this image
No description has been provided for this image
No description has been provided for this image
No description has been provided for this image
# 1. Bar Plot for Average Calories by Manufacturer
plt.figure(figsize=(12, 6))
avg_calories = cereal_data.groupby('mfr')['calories'].mean().reset_index()
sns.barplot(x='mfr', y='calories', data=avg_calories)
plt.title('Average Calories by Manufacturer')
plt.xlabel('Manufacturer')
plt.ylabel('Average Calories')
plt.show()
No description has been provided for this image
plt.figure(figsize=(12, 6))
sorted_data = cereal_data.sort_values('fiber')
sns.lineplot(x='fiber', y='rating', data=sorted_data, marker='o')
plt.title('Rating by Fiber Content')
plt.xlabel('Fiber (grams)')
plt.ylabel('Rating')
plt.show()
C:\Users\gouth\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
C:\Users\gouth\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
No description has been provided for this image
# 3. Pie Chart for Distribution of Cereal Types
plt.figure(figsize=(8, 8))
type_counts = cereal_data['type'].value_counts()
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Cereal Types')
plt.show()
No description has been provided for this image
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Database connection details
db_user = 'root'
db_pass = '1234'
db_host = 'localhost'
db_name = 'sprint2prj'

# Connect to the MySQL database
conn = mysql.connector.connect(
    user=db_user,
    password=db_pass,
    host=db_host,
    database=db_name
)

# SQL query to fetch the data from the new table
fetch_data_query = "SELECT * FROM joined_cereal_data"

# Fetch the data into a pandas DataFrame
cereal_data = pd.read_sql(fetch_data_query, conn)

# Close the connection
conn.close()

# Display the first few rows of the DataFrame
print(cereal_data.head())

# Visualization 1: Bar Plot for Average Calories by Manufacturer
plt.figure(figsize=(10, 6))
avg_calories = cereal_data.groupby('mfr_name')['calories'].mean().reset_index()
sns.barplot(x='mfr_name', y='calories', data=avg_calories)
plt.title('Average Calories by Manufacturer')
plt.xlabel('Manufacturer')
plt.ylabel('Average Calories')
plt.show()

# Visualization 2: Line Plot for Rating by Fiber Content
plt.figure(figsize=(10, 6))
sns.lineplot(x='fiber', y='rating', data=cereal_data)
plt.title('Rating by Fiber Content')
plt.xlabel('Fiber Content')
plt.ylabel('Rating')
plt.show()

# Visualization 3: Pie Chart for Distribution of Cereal Types
plt.figure(figsize=(8, 8))
type_counts = cereal_data['type'].value_counts()
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Cereal Types')
plt.show()

# Visualization 4: Bar Plot for Total Sugars by Shelf Position
plt.figure(figsize=(10, 6))
total_sugars = cereal_data.groupby('shelf')['sugars'].sum().reset_index()
sns.barplot(x='shelf', y='sugars', data=total_sugars)
plt.title('Total Sugars by Shelf Position')
plt.xlabel('Shelf Position')
plt.ylabel('Total Sugars')
plt.show()

# Visualization 5: Scatter Plot for Sodium vs. Potassium
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sodium', y='potass', hue='type', data=cereal_data)
plt.title('Sodium vs. Potassium')
plt.xlabel('Sodium (mg)')
plt.ylabel('Potassium (mg)')
plt.show()
C:\Users\gouth\AppData\Local\Temp\ipykernel_39488\2020132259.py:24: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
  cereal_data = pd.read_sql(fetch_data_query, conn)
                        name type mfr_name  shelf  weight  cups   rating  \
0                  100% Bran    C        N      3     1.0  0.33  68.4030   
1          100% Natural Bran    C        Q      3     1.0  1.00  33.9837   
2                   All-Bran    C        K      3     1.0  0.33  59.4255   
3  All-Bran with Extra Fiber    C        K      3     1.0  0.50  93.7049   
4             Almond Delight    C        R      3     1.0  0.75  34.3848   

   calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  
0        70        4    1     130   10.0    5.0       6     280        25  
1       120        3    5      15    2.0    8.0       8     135         0  
2        70        4    1     260    9.0    7.0       5     320        25  
3        50        4    0     140   14.0    8.0       0     330        25  
4       110        2    2     200    1.0   14.0       8      -1        25  
No description has been provided for this image
C:\Users\gouth\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
C:\Users\gouth\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
No description has been provided for this image
No description has been provided for this image
No description has been provided for this image
No description has been provided for this image
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize= (18, 10))
avg_calories = cereal_data.groupby('name')['calories'].mean().reset_index()
sns.barplot(x='name', y='calories', data=avg_calories)
plt.title('Average Calories by Manufacturer')
plt.xlabel('Manufacturer')
plt.ylabel('Average Calories')
plt.xticks(rotation=90)  # Adjust the rotation angle as needed
plt.show()
No description has been provided for this image
# Visualization 2: Line Plot for Rating by Fiber Content
plt.figure(figsize=(10, 6))
sns.barplot(x='fiber', y='rating', data=cereal_data)
plt.title('Rating by Fiber Content')
plt.xlabel('Fiber Content')
plt.ylabel('Rating')
plt.show()
No description has been provided for this image
# Visualization 3: Pie Chart for Distribution of Cereal Types
plt.figure(figsize=(8, 8))
type_counts = cereal_data['type'].value_counts()
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Cereal Types')
plt.show()
No description has been provided for this image
# Visualization 4: Bar Plot for Total Sugars by Shelf Position
plt.figure(figsize=(10, 6))
total_sugars = cereal_data.groupby('shelf')['sugars'].sum().reset_index()
sns.barplot(x='shelf', y='sugars', data=total_sugars)
plt.title('Total Sugars by Shelf Position')
plt.xlabel('Shelf Position')
plt.ylabel('Total Sugars')
plt.show()
No description has been provided for this image
# Visualization 5: Scatter Plot for Sodium vs. Potassium
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sodium', y='potass', hue='type', data=cereal_data)
plt.title('Sodium vs. Potassium')
plt.xlabel('Sodium (mg)')
plt.ylabel('Potassium (mg)')
plt.show()
No description has been provided for this image
 
