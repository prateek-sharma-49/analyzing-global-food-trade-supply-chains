# analyzing-global-food-trade-supply-chains
Project Report:
Analyzing Global Food Trade Supply Chains and Forecasting US Food Imports
Prateek Sharma, Graduate Student – MS Business Analytics
University at Buffalo, SUNY 
Email: ps238@buffalo.edu Phone: +1(202) 913-7646
The project analyze trends in food imports to the United States from 1999 to 2022. Using data analysis techniques and time series forecasting, this project provides insights into significant contributor countries and regions, forecast future trends, and to help assessing which modes of transportation are more cost effective than others.
 
  
Executive Summary
The project aims to analyze trends and patterns in food imports to the United States over the last two decades, from 1999 to 2022. Using data analysis techniques and time series forecasting, this project aimed to provide insights into the volume of food imports from various countries and regions, identify significant contributors, forecast future trends, and to help assessing which modes of transportation are more cost effective than others.
Introduction
Food imports play an important role in supporting a country’s nutritional needs, especially in a world with widespread international trade. Understanding the patterns of food imports reveals important information about economic trends, dietary habits, and international trade linkages.
Methodology Data Collection
The project used data from the US government’s official website, data.gov, with a specific focus on food imports from the years 1999 to 2022. The dataset included information on sales, volume, pricing, and import locations (countries) for three categories of food: animals, plants, and beverages. These categories were then divided into different food types.
    
Data Preprocessing
Before analysis, the data went through preprocessing steps to address a variety of concerns, including:
• Data Formatting: The dataset was not properly formatted, requiring changes for consistency and readability.
• Data Cleaning: Removed duplicates, missing values, and checked for outliers to improve data quality.
• Data Type Usage: Each attribute was assigned the appropriate data type for simplicity of analysis.
• Other Issues: Additional data wrangling tasks were performed to ensure data integrity.
Analysis Techniques
The analysis included a variety of statistical and machine learning techniques, including:
• Descriptive Statistics: Identifying the distribution and summary statistics of food import volumes.
• Time Series Analysis: Identifying trends, seasonality, and patterns in import data.
• ARIMA Modeling: Forecasting future food import trends using past data.
• CPV Analysis: Optimizing supply chain logistics for cost-effectiveness and
efficiency through transportation mode analysis.

Results Descriptive Analysis
• Over the past two decades, food imports to the US have steadily increased with fluctuations attributed to economic, geopolitical, and environmental factors.
• Mexico and Canada have emerged as key contributors to US food imports. Time Series Analysis
• Time series analysis revealed short-term volatility and long-term trends in food import volumes.
• Seasonal patterns were observed, with peaks corresponding to factors such as economic growth, or trade agreements that influence consumer behavior and increase import volumes, while declines were observed during periods of reduced agricultural output, decreased consumer demand, or global issues such as the COVID-19 pandemic.
ARIMA Forecasting
• ARIMA modeling provided forecasts of future food import trends, enabling stakeholders to anticipate demand and plan accordingly.
• The estimates predicted continued growth in food imports, with potential swings affected by global supply chain disruptions.
 
Data Analysis
o Total Import Value: The overall trend in total import value from 1999 to 2022 shows steady increase and a sharp surge in demand after the COVID-19 epidemic. The sole exception is the 2008 financial crisis.
o Comparing Total Import Values for Animals, Plants, and Beverages Over Time: Plants have shown the highest growth trajectory.
  
 o Total US Imports and Contributions from several categories: Plants have consistently been the most significant contributor to import sales values.
 
o Trend Analysis of Plants-Food Types: Vegetables, fruits, and grains were the top contributors in the plants category.
 o Trend Analysis of Total US Food Imports – Volume: Analyzed total US import volume trends and found a steady rising trend.

 o Trend Analysis of Total Import Volume for Animals, Plants, and Beverages: Plants have the highest growth rate.
 
o Trend Analysis of Plant-Based Food Types (Volume): Vegetables, fruits, and grains accounted for most of the plants-based food consumption.
 o Cost Per Volume Analysis: Revealed that fruits, vegetables, and grains provide the highest value for money.
 
o ADF Statistic: Confirmed stationarity of data through differencing and logarithmic transformation.
o Autocorrelation Function (ACF): Determined parameter 'q' for ARIMA modeling.
  o Partial Autocorrelation Function (PACF): Determined parameter 'p' for ARIMA modeling.

 o Training and Testing Data: Prepared data for ARIMA modeling by splitting into training and testing sets.
 
o ARIMA Model Predictions on Testing Data: Evaluated ARIMA model performance on testing data.
 o Future Predictions: Generated forecasts for the next three years using the ARIMA model.
o Vegetable Imports by Country: Analyzed country-wise vegetable imports using a stacked area plot.
 
 o Percentage of Total Volume by Country for the Year 2022: Visualized country contributions to vegetable imports for the year 2022 using a pie chart.
 
o Total Volume and Contributions from Different Transportation Modes: After identifying Mexico and Canada as key partners in US food commerce, analyzed the contribution of various modes of transportation and plotted a pattern from 2010-2022. As expected, Pipelines and Waterways continue to be favored method of delivering goods.
 
o CPV Analysis for Transportation Modes: The Cost-Per-Volume analysis revealed that Pipelines are consistently the most efficient method of carrying goods, followed by waterways, rail, trucks, and air.
 
Conclusion
As an analyst, with access to data on the overall value of imports for each food type, total volume of imports, and prices for different food types, I attempted to evaluate the dataset to identify insights and opportunities. Essentially, I aimed to:
1. Identify Imports with High Profit Margins: By evaluating the profit margins of importing each food type and comparing the cost per unit volume across different food types, I attempted to identify food types with lower cost per unit volume, indicating greater value for money in terms of import costs.
2. Forecasting Market Trends: Using historical data on import volumes, I built an ARIMA model to forecast volume values for 2023-2025. This data can be used to uncover new opportunities and challenges in the global food trade.
3. Evaluating Cost-Effective Modes of Transportation: After finding the profit margins for food types such as vegetables, I evaluated and plotted to show that Mexico and Canada are the largest contributors to US food trade. With this information in hand, I proceeded to examine and determine which modes of transportation are most cost effective.
Next, here's how various entities can use the analysis and observation obtained from this project:
o Businesses and Importers: The findings from this analysis can help businesses and importers examine the cost-effectiveness of their import operations. This information will allow importers to identify food types that offer the best value for money. This information can help with procurement decisions, supplier negotiations, and pricing strategies.
 
o Government Agencies and Policy Makers: They can use this analysis to monitor trade patterns and evaluate the economic impact of food imports. Policymakers can identify sectors with excessively high or low import costs compared to the volume imported by studying the relationship between the overall value, volume, and cost per unit volume of imports for different food types. This insight can help to shape trade policy reforms, tariff adjustments, and investment initiatives aimed at increasing economic efficiency and competitiveness.
o Supply Chain Managers: They can optimize their operations using this integrated information. Understanding the cost dynamics of importing different food types allows them to make better decisions about sourcing, transportation, warehousing, and inventory management. This can help to optimize supply chain processes, lower costs, and improve overall operational efficiency.
o Market Analysts and Researchers: They can use this data to examine global trade and food markets, including pricing dynamics and competitive landscapes. Analysts can detect market inefficiencies, pricing anomalies, and new possibilities by investigating the relationship between import sales, volume, and prices for various food types. This information can help food sector businesses and investors make better market forecasts, investment decisions, and strategic plans.
o Consumers and Retailers: While consumers may not have direct access to this detailed data, retailers can use it to support sourcing and pricing strategies.
Overall, collecting data on the total value, volume, and cost per unit volume of imports for each food type, as well as information on cost-effective modes of transportation, can provide valuable insights to a wide range of stakeholders, allowing them to make informed decisions, optimize operations, and navigate the complexities of global food markets more effectively.
