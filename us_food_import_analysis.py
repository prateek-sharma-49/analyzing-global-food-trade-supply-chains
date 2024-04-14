# Step 1: Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Loading the dataset
dataset = pd.read_excel('us_food_import_dataset.xlsx', sheet_name='FoodValue', header=1)

# Printing the first few rows to verify the header
print(dataset.head())

# Step 3: Data Cleaning and Preprocessing
# Checking for missing values
missing_values = dataset.isnull().sum()
print("Missing Values:\n", missing_values)

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Display the entire dataset
print(dataset)

# Reset to default
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
pd.reset_option('display.width')
pd.reset_option('display.max_colwidth')

# Step 4: Trend Analysis
total_imports = dataset[dataset['Category'] == 'Total - US Imports']

years = total_imports.columns[2:]
import_values = total_imports.iloc[:, 2:].values.flatten()

years = years.astype(int)

# Plotting the trend
plt.figure(figsize=(10, 6))
plt.plot(years, import_values, marker='o', linestyle='-')
plt.title('Trend Analysis of Total US Food Imports')
plt.xlabel('Year')
plt.ylabel('Total Import Value ($, Millions)')
plt.grid(True)
plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()

# comparing total import values of animals, plants, and beverages over time
years = dataset.columns[2:]

# Extracting total import values for animals, plants, and beverages
total_animals_imports = dataset[dataset['Category'] == 'Total - Animals'].iloc[:, 2:].squeeze().tolist()
total_plants_imports = dataset[dataset['Category'] == 'Total - Plants'].iloc[:, 2:].squeeze().tolist()
total_beverages_imports = dataset[dataset['Category'] == 'Total - Beverages'].iloc[:, 2:].squeeze().tolist()

plt.figure(figsize=(12, 8))

# Plotting total import values for animals
plt.plot(years, total_animals_imports, marker='o', label='Total Animals')

# for plants
plt.plot(years, total_plants_imports, marker='o', label='Total Plants')

# for beverages
plt.plot(years, total_beverages_imports, marker='o', label='Total Beverages')

plt.title('Comparison of Total Import Values for Animals, Plants, and Beverages Over Time')
plt.xlabel('Year')
plt.ylabel('Import Value ($, Millions)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Loading the dataset
data = {
    'Category': ['Live meat animals', 'Meats', 'Fish and shellfish', 'Dairy', 'Vegetables', 'Fruits', 'Nuts',
                 'Coffee, tea, and spices', 'Grains', 'Vegetable oils', 'Sugar and candy', 'Cocoa and chocolate',
                 'Other edible products', 'Beverages'],
    '2022': [2509.6, 14055.4, 30525.5, 2721.4, 15754.3, 27083.8, 2944.8, 12980.6, 19470.0, 12850.8, 7074.8, 6055.5, 29732.8, 16076.5],
    '2021': [2298.9, 13194.1, 28493.0, 2459.5, 16838.2, 23668.8, 3157.4, 9818.7, 15255.9, 9600.8, 5877.4, 5634.1, 18825.4, 19022.6],
    '2020': [2158.1, 10384.6, 21832.2, 2140.8, 15590.3, 20492.1, 2786.1, 8346.2, 13924.5, 6682.1, 5318.3, 5052.4, 16554.4, 16368.9],
    '2019': [2253.4, 9668.9, 22469.1, 2195.7, 13974.8, 20313.8, 3191.0, 8427.3, 13035.5, 6303.5, 4810.1, 4977.1, 15270.5, 16096.7],
    '2018': [2029.4, 9251.2, 22900.9, 2063.1, 13419.1, 19539.3, 3502.1, 8454.7, 12562.1, 6989.2, 4803.9, 4712.6, 14929.3, 15760.0],
    '2017': [2016.3, 8875.2, 21924.9, 1876.9, 12670.5, 18384.6, 3312.2, 9066.7, 11257.6, 7216.0, 4807.5, 5012.6, 10871.7, 15218.6],
    '2016': [2103.3, 8587.2, 19638.4, 1907.2, 12409.2, 17157.8, 2877.9, 8311.3, 10558.4, 6523.3, 4802.9, 5080.9, 11921.1, 13558.9],
    '2015': [2774.9, 9991.7, 18877.9, 1911.5, 11227.1, 15954.8, 2776.1, 8536.2, 10360.1, 6304.1, 4829.4, 4859.9, 12105.3, 12841.7],
    '2014': [3009.9, 8940.3, 20363.3, 1871.6, 10880.9, 14807.7, 2370.0, 8298.8, 10363.7, 7336.6, 4705.4, 4728.6, 12134.5, 12013.7],
    '2013': [2193.0, 6529.9, 18059.6, 1712.1, 10687.6, 13602.3, 2019.4, 7633.2, 10584.6, 6664.5, 4462.9, 4159.5, 12178.2, 11290.9],
    '2012': [2196.3, 6245.2, 16792.6, 1636.7, 9899.3, 12537.9, 2077.4, 8725.7, 9387.8, 6235.9, 4931.8, 4096.2, 13153.8, 10894.4],
    '2011': [1893.3, 5755.3, 16509.3, 1524.5, 9645.4, 12158.6, 1881.6, 9715.8, 8303.7, 6793.6, 5305.0, 4681.0, 10141.6, 10174.1],
    '2010': [2014.0, 5087.9, 14545.9, 1363.1, 8693.3, 10814.0, 1468.8, 6265.0, 7348.1, 4508.8, 4185.2, 4295.6, 8574.1, 9293.2],
    '2009': [1661.5, 4612.1, 12954.0, 1366.2, 7512.8, 9799.9, 1285.0, 5160.3, 7035.6, 4039.4, 3205.6, 3476.4, 7613.6, 8749.9],
    '2008': [2277.1, 5059.8, 13950.5, 1622.5, 7798.4, 10064.7, 1358.3, 5580.8, 7902.3, 5694.6, 3108.1, 3299.2, 8176.2, 9859.6],
    '2007': [2596.4, 5367.4, 13466.4, 1540.8, 7254.6, 9384.1, 1190.8, 4791.2, 6104.9, 3516.7, 2707.6, 2661.6, 7415.8, 9939.5],
    '2006': [2173.9, 5243.7, 13145.7, 1429.5, 6617.9, 7833.2, 1100.4, 4200.4, 5076.4, 2818.3, 3145.6, 2659.7, 7242.7, 9238.2],
    '2005': [1673.3, 5752.0, 11876.4, 1404.5, 6044.3, 7003.6, 1122.1, 3775.7, 4412.2, 2362.6, 2579.4, 2751.2, 6643.2, 7911.2],
    '2004': [1139.4, 5718.5, 11138.7, 1303.7, 5735.8, 6047.3, 1079.7, 3148.8, 4176.2, 2241.0, 2193.2, 2485.2, 5813.3, 7047.5],
    '2003': [1278.0, 4426.9, 10892.7, 1118.7, 5094.8, 5631.4, 781.3, 2875.5, 3759.2, 1506.5, 2205.0, 2440.2, 4470.9, 6621.1],
    '2002': [1725.2, 4283.5, 10000.9, 1013.9, 4397.7, 5138.8, 740.0, 2457.8, 3477.4, 1301.7, 1928.1, 1761.9, 3160.6, 5817.6],
    '2001': [1772.0, 4256.2, 9697.5, 1000.4, 4160.8, 4741.9, 717.0, 2403.4, 3100.7, 1309.8, 1684.9, 1536.9, 2891.7, 5123.2],
    '2000': [1420.3, 3827.7, 9946.7, 925.6, 3772.0, 4692.2, 849.2, 3444.3, 2833.8, 1501.0, 1642.0, 1405.9, 2689.3, 4838.6],
    '1999': [1190.6, 3260.5, 8914.4, 931.4, 3631.8, 4827.4, 833.3, 3605.9, 2755.6, 1518.7, 1661.9, 1523.1, 2737.1, 4433.3]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Summing up the values for each food type
df['Total'] = df.iloc[:, 1:].sum(axis=1)

# Excluding animals, plants, and beverages from the total
df_filtered = df[~df['Category'].isin(['Animal', 'Plants', 'Total - Beverages'])]

# Plotting the bar graph
plt.figure(figsize=(10, 6))
plt.bar(df_filtered['Category'], df_filtered['Total'], color='skyblue')
plt.title('Total Sales For Each Food Type')
plt.xlabel('Food Type')
plt.ylabel('Total Sales ($, Millions)')
plt.xticks(rotation=45, ha='right')

# Adding a horizontal line at y = 200000
plt.axhline(y=200000, color='green', linestyle='--')
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008,
             2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999],  # Add more years as needed
    'Total_Animals': [49811.9, 46445.5, 36515.7, 36587.1, 36244.6, 34693.3, 32236.1, 33556.0, 34185.1,
                      28494.6, 26870.8, 25682.4, 23010.9, 20593.8, 22909.9, 22971.0, 21992.8, 20706.2,
                      19300.3, 17716.3, 17023.5, 16726.1, 16120.3, 14296.9],
    'Total_Plants': [133947.4, 108676.7, 94746.4, 90303.6, 88912.3, 82599.4, 79642.8, 76953.0, 75626.2,
                     71992.2, 71045.8, 68626.3, 56152.9, 49128.6, 52982.6, 45027.3, 40694.6, 36694.3,
                     32920.5, 28764.8, 24364.0, 22547.1, 22829.7, 23094.8],
    'Total_Beverages': [16076.5, 19022.6, 16368.9, 16096.7, 15760.0, 15218.6, 13558.9, 12841.7, 12013.7,
                        11290.9, 10894.4, 10174.1, 9293.2, 8749.9, 9859.6, 9939.5, 9238.2, 7911.2,
                        7047.5, 6621.1, 5817.6, 5123.2, 4838.6, 4433.3]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Plotting the bar within a bar graph
plt.figure(figsize=(12, 8))
plt.bar(df['Year'], df['Total_Animals'] + df['Total_Plants'] + df['Total_Beverages'], color='skyblue', label='Total US Imports')
plt.bar(df['Year'], df['Total_Beverages'], color='orange', label='Total Beverages')
plt.bar(df['Year'], df['Total_Plants'], color='green', label='Total Plants', bottom=df['Total_Beverages'])
plt.bar(df['Year'], df['Total_Animals'], color='blue', label='Total Animals', bottom=df['Total_Beverages'] + df['Total_Plants'])
plt.title('Total US Imports and Contributions from Different Categories')
plt.xlabel('Year')
plt.ylabel('Import Value ($, Millions)')
plt.xticks(df['Year'])
plt.legend()
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Category': ['Live meat animals', 'Meats', 'Fish and shellfish', 'Dairy', 'Vegetables', 'Fruits', 'Nuts',
                 'Coffee, tea, and spices', 'Grains', 'Vegetable oils', 'Sugar and candy', 'Cocoa and chocolate',
                 'Other edible products', 'Beverages', 'Total - Animals', 'Total - Plants', 'Total - Beverages',
                 'Total - US Imports'],
    '2022': [2509.6, 14055.4, 30525.5, 2721.4, 15754.3, 27083.8, 2944.8, 12980.6, 19470.0, 12850.8, 7074.8, 6055.5, 29732.8, 16076.5, 49811.9, 133947.4, 16076.5, 199835.8],
    '2021': [2298.9, 13194.1, 28493.0, 2459.5, 16838.2, 23668.8, 3157.4, 9818.7, 15255.9, 9600.8, 5877.4, 5634.1, 18825.4, 19022.6, 46445.5, 108676.7, 19022.6, 174144.8],
    '2020': [2158.1, 10384.6, 21832.2, 2140.8, 15590.3, 20492.1, 2786.1, 8346.2, 13924.5, 6682.1, 5318.3, 5052.4, 16554.4, 16368.9, 36515.7, 94746.4, 16368.9, 147631.0],
    '2019': [2253.4, 9668.9, 22469.1, 2195.7, 13974.8, 20313.8, 3191.0, 8427.3, 13035.5, 6303.5, 4810.1, 4977.1, 15270.5, 16096.7, 36587.1, 90303.6, 16096.7, 142987.4],
    '2018': [2029.4, 9251.2, 22900.9, 2063.1, 13419.1, 19539.3, 3502.1, 8454.7, 12562.1, 6989.2, 4803.9, 4712.6, 14929.3, 15760.0, 36244.6, 88912.3, 15760.0, 140916.9],
    '2017': [2016.3, 8875.2, 21924.9, 1876.9, 12670.5, 18384.6, 3312.2, 9066.7, 11257.6, 7216.0, 4807.5, 5012.6, 10871.7, 15218.6, 34693.3, 82599.4, 15218.6, 132511.3],
    '2016': [2103.3, 8587.2, 19638.4, 1907.2, 12409.2, 17157.8, 2877.9, 8311.3, 10558.4, 6523.3, 4802.9, 5080.9, 11921.1, 13558.9, 32236.1, 79642.8, 13558.9, 125437.8],
    '2015': [2774.9, 9991.7, 18877.9, 1911.5, 11227.1, 15954.8, 2776.1, 8536.2, 10360.1, 6304.1, 4829.4, 4859.9, 12105.3, 12841.7, 33556.0, 76953.0, 12841.7, 123350.7],
    '2014': [3009.9, 8940.3, 20363.3, 1871.6, 10880.9, 14807.7, 2370.0, 8298.8, 10363.7, 7336.6, 4705.4, 4728.6, 12134.5, 12013.7, 34185.1, 75626.2, 12013.7, 121825.0],
    '2013': [2193.0, 6529.9, 18059.6, 1712.1, 10687.6, 13602.3, 2019.4, 7633.2, 10584.6, 6664.5, 4462.9, 4159.5, 12178.2, 11290.9, 28494.6, 71992.2, 11290.9, 111777.7],
    '2012': [2196.3, 6245.2, 16792.6, 1636.7, 9899.3, 12537.9, 2077.4, 8725.7, 9387.8, 6235.9, 4931.8, 4096.2, 13153.8, 10894.4, 26870.8, 71045.8, 10894.4, 108811.0],
    '2011': [1893.3, 5755.3, 16509.3, 1524.5, 9645.4, 12158.6, 1881.6, 9715.8, 8303.7, 6793.6, 5305.0, 4681.0, 10141.6, 10174.1, 25682.4, 68626.3, 10174.1, 104482.8],
    '2010': [2014.0, 5087.9, 14545.9, 1363.1, 8693.3, 10814.0, 1468.8, 6265.0, 7348.1, 4508.8, 4185.2, 4295.6, 8574.1, 9293.2, 23010.9, 56152.9, 9293.2, 88457.0],
    '2009': [1661.5, 4612.1, 12954.0, 1366.2, 7512.8, 9799.9, 1285.0, 5160.3, 7035.6, 4039.4, 3205.6, 3476.4, 7613.6, 8749.9, 20593.8, 49128.6, 8749.9, 78472.3],
    '2008': [2277.1, 5059.8, 13950.5, 1622.5, 7798.4, 10064.7, 1358.3, 5580.8, 7902.3, 5694.6, 3108.1, 3299.2, 8176.2, 9859.6, 22909.9, 52982.6, 9859.6, 85752.1],
    '2007': [2596.4, 5367.4, 13466.4, 1540.8, 7254.6, 9384.1, 1190.8, 4791.2, 6104.9, 3516.7, 2707.6, 2661.6, 7415.8, 9939.5, 22971.0, 45027.3, 9939.5, 77937.8],
    '2006': [2173.9, 5243.7, 13145.7, 1429.5, 6617.9, 7833.2, 1100.4, 4200.4, 5076.4, 2818.3, 3145.6, 2659.7, 7242.7, 9238.2, 21992.8, 40694.6, 9238.2, 71925.6],
    '2005': [1673.3, 5752.0, 11876.4, 1404.5, 6044.3, 7003.6, 1122.1, 3775.7, 4412.2, 2362.6, 2579.4, 2751.2, 6643.2, 7911.2, 20706.2, 36694.3, 7911.2, 65311.7],
    '2004': [1139.4, 5718.5, 11138.7, 1303.7, 5735.8, 6047.3, 1079.7, 3148.8, 4176.2, 2241.0, 2193.2, 2485.2, 5813.3, 7047.5, 19300.3, 32920.5, 7047.5, 59268.3],
    '2003': [1278.0, 4426.9, 10892.7, 1118.7, 5094.8, 5631.4, 781.3, 2875.5, 3759.2, 1506.5, 2205.0, 2440.2, 4470.9, 6621.1, 17716.3, 28764.8, 6621.1, 53102.2],
    '2002': [1725.2, 4283.5, 10000.9, 1013.9, 4397.7, 5138.8, 740.0, 2457.8, 3477.4, 1301.7, 1928.1, 1761.9, 3160.6, 5817.6, 17023.5, 24364.0, 5817.6, 47205.1],
    '2001': [1772.0, 4256.2, 9697.5, 1000.4, 4160.8, 4741.9, 717.0, 2403.4, 3100.7, 1309.8, 1684.9, 1536.9, 2891.7, 5123.2, 16726.1, 22547.1, 5123.2, 44396.4],
    '2000': [1420.3, 3827.7, 9946.7, 925.6, 3772.0, 4692.2, 849.2, 3444.3, 2833.8, 1501.0, 1642.0, 1405.9, 2689.3, 4838.6, 16120.3, 22829.7, 4838.6, 43788.6],
    '1999': [1190.6, 3260.5, 8914.4, 931.4, 3631.8, 4827.4, 833.3, 3605.9, 2755.6, 1518.7, 1661.9, 1523.1, 2737.1, 4433.3, 14296.9, 23094.8, 4433.3, 41825.0]

}

# Creating a DataFrame
df = pd.DataFrame(data)

# Exclude categories
df_filtered = df[~df['Category'].isin(['Total - Plants', 'Total - Animals', 'Total - Beverages', 'Total - US Imports',  'Beverages', 'Dairy', 'Fish and shellfish', 'Meats', 'Live meat animals'])]

# Plotting the line plot
plt.figure(figsize=(12, 6))
for index, row in df_filtered.iterrows():
    plt.plot(df.columns[1:], row[1:], marker='o', label=row['Category'])
plt.title('Trend Analysis of Plants-Food Types')
plt.xlabel('Year')
plt.ylabel('Import Value ($, Millions)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.gca().invert_xaxis()
plt.tight_layout()
plt.show()

#loading second worksheet 'FoodVolume'
dataset_volume = pd.read_excel('us_food_import_dataset.xlsx', sheet_name='FoodVolume', header=1)
print(dataset_volume.head())

import pandas as pd
import matplotlib.pyplot as plt

# Loading the dataset
dataset_volume = pd.read_excel('us_food_import_dataset.xlsx', sheet_name='FoodVolume', header=1)

# Extracting the row corresponding to 'Total-US Imports'
total_us_imports = dataset_volume[dataset_volume['Category'] == 'Total - US Imports']

# Extracting the years and import values
years = total_us_imports.columns[2:]
import_values = total_us_imports.iloc[:, 2:].values.flatten()
years = years.astype(int)

# Plotting the trend
plt.figure(figsize=(10, 6))
plt.plot(years, import_values, marker='o', linestyle='-')
plt.title('Trend Analysis of Total US Food Imports - Volume (1999-2022)')
plt.xlabel('Year')
plt.ylabel('Total Import Volume (MT/KL)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Loading the dataset
dataset_volume = pd.read_excel('us_food_import_dataset.xlsx', sheet_name='FoodVolume', header=1)

# Extracting data for Total-Animals, Total-Plants, and Total-Beverages categories
categories_of_interest = ['Total - Animals', 'Total - Plants', 'Total - Beverages']
selected_categories = dataset_volume[dataset_volume['Category'].isin(categories_of_interest)]

years = dataset_volume.columns[2:]

plt.figure(figsize=(12, 8))

# Plotting total import values for each category
for category in categories_of_interest:
    import_values = selected_categories[selected_categories['Category'] == category].iloc[:, 2:].values.flatten()
    plt.plot(years, import_values, marker='o', label=category)

plt.title('Trend Analysis of Total Import Volume for Animals, Plants, and Beverages')
plt.xlabel('Year')
plt.ylabel('Total Import Volume (MT/KL)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Excluding categories that are not relevant
categories_to_exclude = ['Total - US Imports', 'Total - Animals', 'Total - Plants', 'Total - Beverages']
filtered_data = dataset_volume[~dataset_volume['Category'].isin(categories_to_exclude)]

# Grouping by food type and sum volumes from 1999 to 2022
summed_values = filtered_data.groupby('Food')[filtered_data.columns[2:]].sum()

# Plotting the bar graph
plt.figure(figsize=(12, 8))
summed_values.plot(kind='bar', color='skyblue', legend=False)
plt.title('Total Volume for Each Food Type (1999-2022)')
plt.xlabel('Food Type')
plt.ylabel('Total Volume')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Category': ['Live meat animals', 'Meats', 'Fish and shellfish', 'Dairy', 'Vegetables', 'Fruits', 'Nuts',
                 'Coffee, tea, and spices', 'Grains', 'Vegetable oils', 'Sugar and candy', 'Cocoa and chocolate',
                 'Other edible products', 'Beverages', 'Total - Animals', 'Total - Plants', 'Total - Beverages',
                 'Total - US Imports'],
    '2022': [8135.10, 2194.40, 3158.70, 407.20, 12100.70, 15308.30, 552.40, 2414.00, 12586.60, 7192.30, 4900.00, 1514.70, 4338.00, 7399.40, 13895.40, 60907.00, 7399.40, 82201.80],
    '2021': [8440.50, 2077.50, 3111.50, 396.70, 13349.00, 14768.30, 592.90, 2344.50, 11319.00, 6718.80, 4538.80, 1532.50, 3079.10, 10006.70, 14026.20, 58242.90, 10006.70, 82275.80],
    '2020': [7397.30, 1886.90, 2778.20, 392.80, 12278.70, 14168.00, 523.40, 2254.60, 11799.40, 6219.90, 4957.30, 1391.90, 2689.80, 8943.10, 12455.20, 56283.00, 8943.10, 77681.30],
    '2019': [7139.20, 1795.50, 2704.90, 408.10, 11763.40, 13882.40, 543.00, 2371.90, 11464.70, 6149.80, 4304.90, 1393.90, 2437.60, 8336.40, 12047.70, 54311.60, 8336.40, 74695.70],
    '2018': [7124.50, 1821.20, 2773.40, 379.90, 11663.00, 14017.00, 558.40, 2236.80, 12212.80, 6281.90, 4193.20, 1372.90, 2420.60, 8224.20, 12099.00, 54956.60, 8224.20, 75279.80],
    '2017': [7363.30, 1847.80, 2669.90, 382.30, 11070.20, 13606.20, 550.80, 2276.20, 11854.30, 6399.90, 4111.90, 1454.20, 2250.10, 8234.00, 12263.30, 53573.80, 8234.00, 74071.10],
    '2016': [7336.20, 1824.80, 2585.00, 395.60, 10588.40, 13249.50, 517.90, 2235.80, 10994.50, 6198.20, 4374.70, 1365.80, 2432.70, 7181.20, 12141.60, 51957.50, 7181.20, 71280.30],
    '2015': [7661.20, 1942.80, 2525.00, 359.30, 9733.10, 12861.10, 510.50, 2161.00, 10991.50, 6017.80, 4454.00, 1336.70, 2396.00, 6721.60, 12488.30, 50461.70, 6721.60, 69671.60],
    '2014': [7232.60, 1720.20, 2474.20, 302.50, 9574.50, 12161.70, 476.20, 2112.40, 11364.50, 7507.70, 4268.50, 1296.10, 2459.40, 6226.60, 11729.50, 51221.00, 6226.60, 69177.10],
    '2013': [6947.30, 1400.50, 2399.70, 293.60, 8989.30, 11833.30, 433.60, 2087.00, 13034.10, 6278.50, 4048.20, 1303.60, 2342.70, 5946.40, 11041.10, 50350.30, 5946.40, 67337.80],
    '2012': [7909.80, 1336.60, 2384.40, 292.00, 8628.10, 11031.80, 478.00, 2018.80, 10689.80, 5012.80, 4119.30, 1237.40, 2258.90, 5991.00, 11922.80, 45474.90, 5991.00, 63388.70],
    '2011': [7872.70, 1270.10, 2349.40, 248.60, 8440.90, 10466.40, 368.70, 2015.00, 8586.80, 5229.40, 4569.60, 1313.00, 2222.30, 5563.50, 11740.80, 43212.10, 5563.50, 60516.40],
    '2010': [7997.60, 1371.50, 2345.00, 249.70, 8087.00, 10148.80, 363.50, 1894.60, 8643.00, 4583.60, 4003.40, 1222.20, 2027.70, 5348.60, 11963.80, 40973.80, 5348.60, 58286.20],
    '2009': [8350.00, 1445.40, 2248.80, 289.40, 7312.60, 9495.20, 362.10, 1823.00, 8816.30, 4435.70, 3457.50, 1169.40, 1839.30, 5088.20, 12333.60, 38711.10, 5088.20, 56132.90],
    '2008': [11558.60, 1411.40, 2254.50, 309.80, 7348.80, 9782.50, 344.20, 1881.90, 9798.40, 4839.00, 3666.10, 1114.20, 2080.30, 5439.90, 15534.30, 40855.40, 5439.90, 61829.60],
    '2007': [12419.50, 1628.20, 2288.10, 370.80, 7204.50, 9933.50, 360.60, 1850.90, 8888.40, 3930.40, 2985.50, 1129.20, 1996.90, 5605.10, 16706.60, 38279.90, 5605.10, 60591.60],
    '2006': [10985.50, 1627.40, 2317.10, 375.60, 6616.60, 9111.90, 326.50, 1827.40, 7832.80, 3576.70, 3916.20, 1255.60, 1955.30, 5461.80, 15305.60, 36419.00, 5461.80, 57186.40],
    '2005': [9951.90, 1797.10, 2199.50, 382.40, 6368.60, 8757.50, 326.70, 1746.30, 6694.60, 2869.00, 3125.60, 1308.10, 1832.50, 4790.10, 14330.90, 33028.90, 4790.10, 52149.90],
    '2004': [9866.30, 1839.20, 2119.90, 346.40, 6245.50, 8428.60, 336.70, 1758.70, 6643.20, 2759.40, 2433.10, 1170.30, 1750.10, 4387.60, 14171.80, 31525.60, 4387.60, 50085.00],
    '2003': [9223.20, 1659.30, 2082.40, 339.00, 5967.20, 8288.90, 317.90, 1716.30, 6221.30, 2066.70, 2416.70, 1048.50, 1532.90, 4205.70, 13303.90, 29576.40, 4205.70, 47086.00],
    '2002': [8302.90, 1700.00, 1903.50, 332.80, 5584.60, 8006.70, 383.20, 1636.50, 7031.60, 2380.20, 2193.60, 918.60, 1502.90, 3981.80, 12239.20, 29637.90, 3981.80, 45858.90],
    '2001': [7758.10, 1634.00, 1759.00, 326.70, 5139.60, 7556.80, 374.40, 1600.90, 7435.50, 2803.10, 2085.70, 993.10, 1403.40, 3701.30, 11477.80, 29392.50, 3701.30, 44571.60],
    '2000': [6521.80, 1578.10, 1717.20, 298.90, 4755.40, 7688.50, 364.00, 1726.10, 6627.60, 2802.10, 2159.00, 1001.20, 1168.10, 3383.90, 10116.00, 28292.00, 3383.90, 41791.90],
    '1999': [6058.40, 1439.60, 1689.80, 299.20, 4790.10, 7870.20, 318.90, 1651.50, 6985.10, 2428.00, 2269.30, 924.70, 1099.20, 2974.10, 9487.00, 28337.00, 2974.10, 40798.10]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Exclude specified categories
df_filtered = df[~df['Category'].isin(['Total - Plants', 'Total - Animals', 'Total - Beverages', 'Total - US Imports', 'Beverages', 'Dairy', 'Fish and shellfish', 'Meats', 'Live meat animals'])]

# Plotting the line plot
plt.figure(figsize=(12, 6))
for index, row in df_filtered.iterrows():
    plt.plot(df.columns[1:], row[1:], marker='o', label=row['Category'])
plt.title('Trend Analysis of Plant-Based Food Types (Volume)')
plt.xlabel('Year')
plt.ylabel('Volume, MT/KL')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.gca().invert_xaxis()
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Category": ["Live meat animals", "Meats", "Fish and shellfish", "Dairy", "Vegetables", "Fruits", "Nuts", "Coffee, tea, and spices", "Grains", "Vegetable oils", "Sugar and candy", "Cocoa and chocolate", "Other edible products", "Beverages"],
    "Food": ["Live meat animals", "Meats", "Fish and shellfish", "Dairy", "Vegetables", "Fruits", "Nuts", "Coffee, tea, and spices", "Grains", "Vegetable oils", "Sugar and candy", "Cocoa and chocolate", "Other edible products", "Beverages"],
    "2022": [0.31, 6.41, 9.66, 6.68, 1.30, 1.77, 5.33, 5.38, 1.55, 1.79, 1.44, 4.00, 6.85, 2.17],
    "2021": [0.27, 6.35, 9.16, 6.20, 1.26, 1.60, 5.33, 4.19, 1.35, 1.43, 1.29, 3.68, 6.11, 1.90],
    "2020": [0.29, 5.50, 7.86, 5.45, 1.27, 1.45, 5.32, 3.70, 1.18, 1.07, 1.07, 3.63, 6.15, 1.83],
    "2019": [0.32, 5.39, 8.31, 5.38, 1.19, 1.46, 5.88, 3.55, 1.14, 1.02, 1.12, 3.57, 6.26, 1.93],
    "2018": [0.28, 5.08, 8.26, 5.43, 1.15, 1.39, 6.27, 3.78, 1.03, 1.11, 1.15, 3.43, 6.17, 1.92],
    "2017": [0.27, 4.80, 8.21, 4.91, 1.14, 1.35, 6.01, 3.98, 0.95, 1.13, 1.17, 3.45, 4.83, 1.85],
    "2016": [0.29, 4.71, 7.60, 4.82, 1.17, 1.29, 5.56, 3.72, 0.96, 1.05, 1.10, 3.72, 4.90, 1.89],
    "2015": [0.36, 5.14, 7.48, 5.32, 1.15, 1.2, 5.44, 3.95, 0.94, 1.05, 1.08, 3.64, 5.05, 1.91],
    "2014": [0.42, 5.20, 8.23, 6.19, 1.14, 1.22, 4.98, 3.93, 0.91, 0.98, 1.10, 3.65, 4.93, 1.93],
    "2013": [0.32, 4.66, 7.53, 5.83, 1.19, 1.15, 4.66, 3.66, 0.81, 1.06, 1.10, 3.19, 5.20, 1.90],
    "2012": [0.28, 4.67, 7.04, 5.61, 1.15, 1.14, 4.35, 4.32, 0.88, 1.24, 1.20, 3.31, 5.82, 1.82],
    "2011": [0.24, 4.53, 7.03, 6.13, 1.14, 1.16, 5.10, 4.82, 0.97, 1.30, 1.16, 3.57, 4.56, 1.83],
    "2010": [0.25, 3.71, 6.20, 5.46, 1.07, 1.07, 4.04, 3.31, 0.85, 0.98, 1.05, 3.51, 4.23, 1.74],
    "2009": [0.20, 3.19, 5.76, 4.72, 1.03, 1.03, 3.55, 2.83, 0.80, 0.91, 0.93, 2.97, 4.14, 1.72],
    "2008": [0.20, 3.58, 6.19, 5.24, 1.06, 1.03, 3.95, 2.97, 0.81, 1.18, 0.85, 2.96, 3.93, 1.81],
    "2007": [0.21, 3.30, 5.89, 4.16, 1.01, 0.94, 3.30, 2.59, 0.69, 0.89, 0.91, 2.36, 3.71, 1.77],
    "2006": [0.20, 3.22, 5.67, 3.81, 1.00, 0.86, 3.37, 2.30, 0.65, 0.79, 0.80, 2.12, 3.70, 1.69],
    "2005": [0.17, 3.20, 5.40, 3.67, 0.95, 0.80, 3.43, 2.16, 0.66, 0.82, 0.83, 2.10, 3.63, 1.65],
    "2004": [0.12, 3.11, 5.25, 3.76, 0.92, 0.72, 3.21, 1.79, 0.63, 0.81, 0.90, 2.12, 3.32, 1.61],
    "2003": [0.14, 2.67, 5.23, 3.30, 0.85, 0.68, 2.46, 1.68, 0.60, 0.73, 0.91, 2.33, 2.92, 1.57],
    "2002": [0.21, 2.52, 5.25, 3.05, 0.79, 0.64, 1.93, 1.50, 0.49, 0.55, 0.88, 1.92, 2.10, 1.46],
    "2001": [0.23, 2.60, 5.51, 3.06, 0.81, 0.63, 1.92, 1.50, 0.42, 0.47, 0.81, 1.55, 2.06, 1.38],
    "2000": [0.22, 2.43, 5.79, 3.10, 0.79, 0.61, 2.33, 2.00, 0.43, 0.54, 0.76, 1.40, 2.30, 1.43],
    "1999": [0.20, 2.26, 5.28, 3.11, 0.76, 0.61, 2.61, 2.18, 0.39, 0.63, 0.73, 1.65, 2.49, 1.49]
}

# Creating DataFrame
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))

# Using Seaborn's color palette for distinct colors
palette = sns.color_palette("tab20", len(df['Food']))

for i, food_type in enumerate(df['Food']):
    if food_type not in ['Animals', 'Plants', 'US Imports']:
        x = df.columns[2:].astype(int)  # Convert column names to integers
        y = df[df['Food'] == food_type].iloc[:, 2:].values.flatten()  # Flatten the values array
        plt.plot(x, y, marker='o', label=food_type, color=palette[i])

plt.title('Cost Per Volume Analysis (1999-2022)')
plt.xlabel('Year')
plt.ylabel('Value Per Volume')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

import pandas as pd

# Loading the vegetable imports dataset
vegetable_df = pd.read_excel('us_food_import_dataset.xlsx', sheet_name='Volume-Vegetables')

import pandas as pd
import math
from statsmodels.tsa.stattools import adfuller

data = {
    "Year": [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999],
    "Volume": [12100.70, 13349.00, 12278.70, 11763.40, 11663.00, 11070.20, 10588.40, 9733.10, 9574.50, 8989.30, 8628.10, 8440.90, 8087.00, 7312.60, 7348.80, 7204.50, 6616.60, 6368.60, 6245.50, 5967.20, 5584.60, 5139.60, 4755.40, 4790.10]
}

df = pd.DataFrame(data)

# Sorting the DataFrame by the 'Year' column
df.sort_values(by='Year', inplace=True)

# Log transformation
df['Volume_log'] = df['Volume'].apply(lambda x: 0 if x == 0 else math.log(x))

# Differencing
df['Volume_log_diff'] = df['Volume_log'].diff()

# Removing the first observation
df.dropna(inplace=True)

# Checking stationarity using the ADF test
result = adfuller(df['Volume_log_diff'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])
print('Critical Values:')
for key, value in result[4].items():
    print(f'   {key}: {value}')

import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Plotting ACF
plt.figure(figsize=(10, 5))
plot_acf(df['Volume'], lags=22, alpha=0.05, ax=plt.gca())
plt.title('Autocorrelation Function (ACF)')
plt.show()

# Plotting PACF
plt.figure(figsize=(10, 5))
plot_pacf(df['Volume'], lags=11, alpha=0.05, ax=plt.gca())
plt.title('Partial Autocorrelation Function (PACF)')
plt.show()

df.sort_values(by='Year', inplace=True)

# Determining the number of years to reserve for testing
test_years = 3

# Splitting the data into training and testing sets
train_data = df.iloc[:-test_years]
test_data = df.iloc[-test_years:]

import matplotlib.pyplot as plt

# Set the index of the DataFrame to the 'Year' column
df.set_index('Year', inplace=True)

plt.figure(figsize=(10, 6))
plt.plot(train_data['Year'], train_data['Volume'], label='Training Data')
plt.plot(test_data['Year'], test_data['Volume'], label='Testing Data')
plt.xlabel('Year')
plt.ylabel('Volume')
plt.title('Training and Testing Data')
plt.legend()
plt.show()

from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Fit the ARIMA model
model = ARIMA(train_data['Volume'], order=(1, 1, 2))
arima_result = model.fit()

# Printing the summary of the model
print(arima_result.summary())

# Making predictions on the testing data
predictions = arima_result.forecast(steps=len(test_data))

# Set the index of the predicted values to match the index of the testing data
predictions.index = test_data.index

# Plotting the training and testing data along with the predicted values
plt.figure(figsize=(10, 6))
plt.plot(train_data['Year'], train_data['Volume'], label='Training Data')
plt.plot(test_data['Year'], test_data['Volume'], label='Testing Data')
plt.plot(test_data['Year'], predictions, label='Predicted Data', linestyle='--', color='green')
plt.xlabel('Year')
plt.ylabel('Volume')
plt.title('ARIMA Model Predictions on Testing Data')
plt.legend()
plt.show()

# Defining the number of steps to forecast (3 years beyond 2022)
forecast_steps = 3

# Making predictions for the next 3 years
future_predictions = arima_result.forecast(steps=forecast_steps)

future_years = [2023, 2024, 2025]

future_predictions_df = pd.DataFrame({'Year': future_years, 'Predicted_Volume': future_predictions})

# Printing the DataFrame with years and predicted volume values
print(future_predictions_df)

import pandas as pd

data = {
    "Year": range(1999, 2023),
    "Mexico": [2119.13, 2138.29, 2377.10, 2450.13, 2674.86, 2837.14, 2957.18, 3037.10, 3276.32, 3283.80, 3310.18, 3936.57, 4160.77, 4150.15, 4483.38, 4797.15, 4898.76, 5521.34, 5511.47, 5886.30, 6097.44, 6433.47, 6827.67, 5537.23],
    "Canada": [1047.10, 1190.87, 1292.19, 1464.44, 1569.45, 1615.98, 1585.12, 1662.87, 1716.36, 1803.37, 1789.90, 1818.19, 1850.53, 1858.31, 2018.13, 2123.11, 2069.19, 2181.04, 2440.24, 2589.32, 2553.81, 2648.02, 3011.93, 2896.92],
    "Peru": [102.09, 79.55, 106.48, 138.55, 152.14, 183.58, 233.28, 278.25, 327.03, 359.13, 371.63, 397.68, 415.33, 449.65, 461.68, 487.75, 506.55, 490.72, 500.54, 483.59, 489.57, 469.56, 510.95, 527.37],
    "China (Mainland)": [144.95, 122.67, 141.56, 181.09, 201.10, 241.29, 266.68, 328.14, 427.23, 400.50, 358.78, 450.71, 468.19, 471.62, 450.49, 425.45, 463.29, 538.58, 616.48, 525.57, 379.04, 400.17, 401.86, 434.74],
    "Spain": [373.13, 320.98, 317.46, 351.00, 358.05, 353.99, 316.94, 277.55, 291.18, 284.78, 271.95, 293.12, 252.47, 243.87, 237.61, 279.56, 295.45, 304.96, 304.75, 269.34, 305.22, 290.15, 303.56, 310.46],
    "Guatemala": [61.46, 55.09, 48.42, 57.91, 63.48, 69.80, 70.59, 70.49, 87.99, 114.40, 118.65, 100.65, 129.78, 142.16, 144.67, 159.36, 166.54, 156.83, 172.99, 210.77, 197.14, 215.88, 246.48, 247.94],
    "Greece": [57.37, 51.44, 51.51, 72.26, 72.73, 81.66, 79.55, 67.59, 96.23, 91.03, 93.15, 96.84, 103.09, 99.01, 102.87, 114.66, 118.08, 117.15, 143.81, 155.14, 154.55, 139.72, 154.67, 189.56],
    "Rest of world": [884.87, 796.52, 804.88, 869.24, 875.38, 862.05, 859.25, 894.62, 982.17, 1011.80, 998.37, 993.24, 1060.74, 1213.34, 1090.48, 1187.47, 1215.26, 1277.77, 1379.92, 1542.97, 1586.63, 1681.73, 1891.89, 1956.48]
}

df = pd.DataFrame(data)

# Set the 'Year' column as the index
df.set_index('Year', inplace=True)

# Plot stacked area plot
df.plot(kind='area', stacked=True, figsize=(10, 6))
plt.title('Vegetable Imports by Country (1999-2022)')
plt.xlabel('Year')
plt.ylabel('Volume')
plt.xticks(rotation=45)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()

import matplotlib.pyplot as plt

# Data for the year 2022
year_2022_data = {
    "Mexico": 5537.23,
    "Canada": 2896.92,
    "Peru": 527.37,
    "China (Mainland)": 434.74,
    "Spain": 310.46,
    "Guatemala": 247.94,
    "Greece": 189.56,
    "Rest of world": 1956.48
}

total_volume_2022 = sum(year_2022_data.values())

# percentage of total volume for each country
percentage_data = {country: (volume / total_volume_2022) * 100 for country, volume in year_2022_data.items()}

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(percentage_data.values(), labels=percentage_data.keys(), autopct='%1.1f%%')
plt.title('Percentage of Total Volume by Country for the Year 2022')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Mode': ['Truck', 'Rail', 'Air', 'Water', 'Pipeline', 'Other', 'Total'],
    '2010': [187.60, 134.20, 0.00, 210.20, 106.50, 11.10, 650.00],
    '2016': [213.40, 163.30, 0.00, 194.30, 208.90, 33.30, 813.60],
    '2017': [223.40, 170.20, 0.00, 210.50, 223.20, 20.40, 848.00],
    '2018': [234.80, 180.60, 0.40, 232.00, 209.70, 22.20, 879.70],
    '2019': [113.60, 107.80, 0.30, 231.00, 180.30, 5.70, 638.70],
    '2020': [122.00, 102.60, 0.30, 206.70, 179.80, 3.50, 614.80],
    '2021': [213.20, 102.90, 0.40, 213.20, 191.90, 0.20, 721.80],
    '2022': [131.50, 103.70, 0.40, 216.70, 198.50, 0.20, 651.00]
}

df = pd.DataFrame(data)

# colors for each mode of transportation
colors = {'Truck': 'blue', 'Rail': 'green', 'Air': 'red', 'Water': 'orange', 'Pipeline': 'purple', 'Other': 'yellow'}

# Plotting the bar within a bar graph
plt.figure(figsize=(12, 8))

plt.bar(df.columns[1:], df.loc[df['Mode'] == 'Total'].values[0][1:], color='skyblue', label='Total Volume')
modes = ['Truck', 'Rail', 'Air', 'Water', 'Pipeline', 'Other']
bottom_values = [0] * len(df.columns[1:])
for mode in modes:
    if mode != 'Total':
        plt.bar(df.columns[1:], df.loc[df['Mode'] == mode].values[0][1:], color=colors[mode], label=mode, bottom=bottom_values)
        bottom_values = [bottom_values[i] + df.loc[df['Mode'] == mode].values[0][i+1] for i in range(len(bottom_values))]

plt.title('Total Volume and Contributions from Different Transportation Modes')
plt.xlabel('Year')
plt.ylabel('Volume')
plt.legend()
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Mode': ['Truck', 'Rail', 'Air', 'Water', 'Pipeline', 'Other'],
    '2010': [2.99, 0.98, 0.00, 0.39, 0.61, 3.37],
    '2016': [3.28, 1.01, 0.00, 0.30, 0.24, 1.62],
    '2017': [3.23, 1.02, 0.00, 0.36, 0.29, 2.93],
    '2018': [3.29, 0.99, 117.00, 0.42, 0.35, 2.74],
    '2019': [6.80, 1.66, 165.00, 0.41, 0.40, 10.23],
    '2020': [5.69, 1.45, 155.00, 0.33, 0.30, 14.94],
    '2021': [3.88, 1.81, 131.75, 0.46, 0.51, 282.00],
    '2022': [7.21, 2.03, 144.50, 0.64, 0.75, 303.00]
}

df = pd.DataFrame(data)

# Plotting the line plot for cost per volume analysis excluding "Other" mode
plt.figure(figsize=(10, 6))
for mode in df['Mode']:
    if mode != 'Other':
        plt.plot(df.columns[1:], df[df['Mode'] == mode].values[0][1:], marker='o', label=mode)

plt.title('Cost Per Volume Analysis for Transportation Modes (Excluding "Other")')
plt.xlabel('Year')
plt.ylabel('Cost Per Volume')
plt.ylim(0, 100)  # Set y-axis limits to focus on the range 0-25
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()








