# analyzing-global-food-trade-supply-chains
Project Report

Executive Summary:
- The project delves into the intricate landscape of global food trade, focusing on the United States' food imports from 1999 to 2022. Employing advanced data analytics techniques, including descriptive analytics, time series analysis, and predictive modeling, the project aims to provide actionable insights for stakeholders in the areas of supply chain optimization, strategic planning, and risk assessment.

Introduction:
- The global food trade landscape has undergone significant transformations over the past two decades, influenced by economic shifts, geopolitical dynamics, and advancements in data analytics and machine learning. As the United States remains one of the largest importers of food products worldwide, understanding the intricate patterns, trends, and drivers behind its food imports becomes paramount for stakeholders ranging from policymakers to supply chain managers. 

Problem Statement:
- Despite the critical role of food imports in ensuring nutritional security and catering to consumer demands, there exists a gap in comprehensive analyses that integrate multi-dimensional data, employing techniques such as descriptive analytics, time series analysis, and predictive modeling, to explain the underlying dynamics of US food imports. This project seeks to address this gap by leveraging advanced data analytics techniques, including statistical modeling, machine learning algorithms, and optimization methods, to analyze and forecast US food imports from 1999 to 2022.

Objectives:
The primary objectives of this project are:
1.	Data Analysis and Insights Generation: To conduct exploratory data analysis (EDA) and employ data visualization techniques to analyze historical trends and patterns in US food imports across various food categories such as animals, plants, and beverages, deriving actionable insights for stakeholders.
2.	Forecasting Future Trends: To utilize time series forecasting methods, including ARIMA (Autoregressive Integrated Moving Average) modeling and Exponential Smoothing, to predict future trends in US food imports, aiding stakeholders in strategic planning, risk assessment, and decision-making.
3.	Cost-Effectiveness Analysis: To perform Cost-Per-Volume (CPV) analysis and supply chain optimization using linear programming and heuristic algorithms, evaluating the cost dynamics associated with different modes of transportation used for food imports, and identifying the most cost-effective transportation methods to optimize supply chain logistics.

Methodology:
- Data Collection:
The project leverages data from the US government’s official website, data.gov, with a specific focus on food imports from the years 1999 to 2022. The dataset encompasses information on sales, volume, pricing, and import locations (countries) for three categories of food: animals, plants, and beverages. These categories were then divided into different food types.
- Data Preprocessing: 
Prior to analysis, the dataset underwent rigorous preprocessing, addressing concerns such as data formatting inconsistencies, duplicate entries, missing values, and outliers. Data types were appropriately assigned to facilitate seamless analysis.
- Analysis Techniques:
The project employed a range of statistical and machine learning techniques, including:
•	Descriptive Statistics: Identifying the distribution and summary statistics of food import sales, volumes, and prices.
•	Time Series Analysis: Uncovering trends, seasonality, and patterns.
•	ARIMA Modeling: Forecasting future food import trends using past data.
•	CPV Analysis: Optimizing supply chain logistics for cost-effectiveness and efficiency through transportation mode analysis.

Results
 
- Descriptive Analysis
•	Steady increase in US food imports with fluctuations attributed to economic, geopolitical, and environmental factors.
•	Mexico and Canada emerged as key contributors to US food imports.
- Time Series Analysis
•	Short-term volatility and long-term trends observed in food import volumes.
•	Seasonal patterns were identified, with peaks corresponding to factors such as economic growth, or trade agreements that influence consumer behavior and increase import volumes, while declines were observed during periods of reduced agricultural output, decreased consumer demand, or global issues such as the COVID-19 pandemic.

- ARIMA Forecasting
•	ARIMA modeling provided forecasts of future food import trends, enabling stakeholders to anticipate demand and plan accordingly.
•	The estimates predicted continued growth in food imports, with potential swings affected by global supply chain disruptions.


 
Data Analysis
- Total US Imports and Contributions from several categories: Plants have consistently been the most significant contributor to import sales values.
  
     <img width="468" alt="image" src="https://github.com/prateek-sharma-49/analyzing-global-food-trade-supply-chains/assets/162940123/188162cd-a277-428a-ac84-b4ea0994c2a0">
   
- Trend Analysis of Plant-Based Food Types (Volume): Vegetables, fruits, and grains accounted for most of the plants-based food consumption.
  
     <img width="468" alt="image" src="https://github.com/prateek-sharma-49/analyzing-global-food-trade-supply-chains/assets/162940123/503ad911-2fbd-41a9-a5c6-067a1ff577e9">
- Cost Per Volume Analysis: Revealed that fruits, vegetables, and grains provide the highest value for money.
  <img width="468" alt="image" src="https://github.com/prateek-sharma-49/analyzing-global-food-trade-supply-chains/assets/162940123/02b863f4-6497-4863-b311-1ff1f4f661e0">
- ARIMA Model Predictions on Testing Data: Evaluated ARIMA model performance on testing data.
   <img width="468" alt="image" src="https://github.com/prateek-sharma-49/analyzing-global-food-trade-supply-chains/assets/162940123/efda794d-4a88-4167-a1ef-9c284a2dfd91">

- Vegetable Imports by Country: Analyzed country-wise vegetable imports using a stacked area plot.
  <img width="468" alt="image" src="https://github.com/prateek-sharma-49/analyzing-global-food-trade-supply-chains/assets/162940123/8f7fd1c7-4d70-47f4-b8c9-72545fdcc058">
- Total Volume and Contributions from Different Transportation Modes: After identifying Mexico and Canada as key partners in US food commerce, analyzed the contribution of various modes of transportation and plotted a pattern from 2010-2022. As expected, Pipelines and Waterways continue to be favored method of delivering goods.

  <img width="468" alt="image" src="https://github.com/prateek-sharma-49/analyzing-global-food-trade-supply-chains/assets/162940123/12d5b064-49fc-4829-b5d6-77cec8680e17">
- CPV Analysis for Transportation Modes: The Cost-Per-Volume analysis revealed that Pipelines are consistently the most efficient method of carrying goods, followed by waterways, rail, trucks, and air.

  <img width="468" alt="image" src="https://github.com/prateek-sharma-49/analyzing-global-food-trade-supply-chains/assets/162940123/ba7d9c68-55d6-48ab-bd61-c4cd9406cbf7">


Conclusion:

As an analyst, with access to data on the overall value of imports for each food type, total volume of imports, and prices for different food types, I attempted to evaluate the dataset to identify insights and opportunities. Essentially, I aimed to:
1. Identify Imports with High Profit Margins: By evaluating the profit margins of importing each food type and comparing the cost per unit volume across different food types, I attempted to identify food types with lower cost per unit volume, indicating greater value for money in terms of import costs.
2. Forecasting Market Trends: Using historical data on import volumes, I built an ARIMA model to forecast volume values for 2023-2025. This data can be used to uncover new opportunities and challenges in the global food trade.
3. Evaluating Cost-Effective Modes of Transportation: After finding the profit margins for food types such as vegetables, I evaluated and plotted to show that Mexico and Canada are the largest contributors to US food trade. With this information in hand, I proceeded to examine and determine which modes of transportation are most cost effective.

