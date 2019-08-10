# Machine Learning for Stock Market Investing
## Capstone Project / August 08 - 2019
### Carlos Viejo M.

### Definition
#### Project Overview
Stock market analysis and prediction is one of the most challenging fields to estimate due to the multi-dimensionality and complexity of the inputs. There can be many factors involved in the calculations varying from multiple company/competitor interactions variability, public perception, rational and irrational behaviour of traders and many more, the combination of all these aspects together make price volatile and challenging to predict.

Data scientists and Financial theorists for over half a century have been employed to make sense of the stock market and its variations in order to increase return on investments, but it has been an overwhelmingly difficult challenge for humans to solve due too  the complexity and massive amount of inputs

Thanks to the advancements in machine learning algorithms and its applications, the field has evolved to combine multiple inputs like never before. Current state of the art approaches join information from the organization historical price trends, technical data, social media, news and classic techniques utilizing non-deterministic solutions that can “learn” what is going on from millions of data inputs, these techniques can utilize a mix of neuronal network models that rely on long short term memory units and natural language understanding. unearthing patterns and insights we didn’t see before, using them to make unerringly accurate predictions.

I believe by building a system that can accurately prognosticate stock market variations we can use it to successfully predict a stock's future price maximizing investor's gains.

We will be using statistical figures to identify trends on the market, the datasets utilized will be obtained from 

*Quandl*<br> 
https://www.quandl.com/ is a platform source for financial, economic, and alternative datasets, serving investment professionals 

*Yahoo! Finance*<br> 
https://ca.finance.yahoo.com/ is a platform that provides  It provides financial news, data and commentary including stock quotes, press releases, financial reports, and original content.

The data that we will use is from J.P. Morgan Chase & Co.  we are planning to utilize a total of 10 years of data were 7 years will be used for training and 3 years for validation and testing
the data can be obtained with the following link. https://ca.finance.yahoo.com/quote/JPM?p=JPM

#### Problem Statement

Due to the multi-dimensionality and complexity of the problem the main objective of this capstone project is to provide a machine learning model that utilizes state of the art algorithms, historical stock market data of a public trade company to predict future trends. 

We will start simple utilizing one single attribute and expand to increased complexity by incorporating more inputs, moving from simple algorithms like linear regression to advanced techniques like LSTM Networks.  

To make machine learning predictions quantifiable, measurable and replicable, we will define the datasets utilized and provide access to them, select a well-known performance metric to quantify improvements over a baseline model and provide the codebase (hosted on GitHub) to replicate the results.

The goal is to create a stock market prediction model the task involved are the following:

1. Select a dataset from the financial sites described previously
2. Train a time series regressor that can predict the stock price for n days in the future
3. Submit the trained model for hosting in order to provide predictions
4. Invoke the endpoint for predictions, returning value of the stock the next day

#### Metrics

After our machine learning model has been trained is quite important  to assess how well the model it is able to capture patterns and predict, in order to diagnostic our model we will utilize evaluation metrics and residual diagnostics
For our model we will utilize:

* RMSE: Root mean squared error, this metric is typically used in regression problems and works quite well as an indicator of performance <br>
    *RMSE = MSE*
* MAPE: Mean absolute percentage error, it is scale-independent and represents the ratio of error to actual values as a percent <br>
    *MAPE = mean (et /yt)*

### Analysis
#### Data Exploration

Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Typi non habent claritatem insitam; est usus legentis in iis qui facit eorum claritatem. Investigationes demonstraverunt lectores legere me lius quod ii legunt saepius. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan.
