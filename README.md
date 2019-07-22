Investment-and-Trading [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/cviejom/Investment-and-Trading/blob/master/LICENSE) [![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://naereen.github.io/badges/)
==============================

This project, consists on building a **Stock Price Predictor** that takes daily trading data over a certain date range as input, and outputs projected estimates for given dates. Note that the inputs will contain multiple metrics, such as **opening price** (Open), **highest price** the stock traded at (High), **stock volume** how many stocks were traded (Volume) and **closing price** adjusted for stock splits and dividends (Adjusted Close); our system will predict the **Adjusted Close Price**.

You can read the **Capstone Project Proposal** in the following file: [Project Capstone Proposal](https://github.com/cviejom/Investment-and-Trading/blob/master/PROPOSAL.md) <br>
The pdf version can be located here [Project Capstone Proposal PDF Version](https://github.com/cviejom/Investment-and-Trading/blob/master/reports/documents/Capstone%20Proposal.pdf)

Project Organization
--------------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


Machine Learning for Stock Market Investing
-------------------------------------------
Stock market analysis/prediction is one of the most challenging fields to estimate due to the multi-dimensionality and complexity of the inputs. There can be many factors involved in the calculations varying from multiple company/competitor interactions and competition, public perception, rational and irrational behaviour of traders and many others, the combinations of all these aspects together make price volatile and challenging to predict.

Data
----
There are several open sources for historical stock price data that could be used. The data utilised in the project can be downloaded from the folowing **Amazon S3 Storage**
Please utilize this link [stock market data.csv](https://investment-and-trading-udacity.s3-us-west-2.amazonaws.com/JPM+2009-2019.csv). <br>

If more information is required can extraced from the following location:
https://ca.finance.yahoo.com/quote/JPM/history?p=JPM


Other sources of information if you are interted to get similar information.<br/>
**Yahoo! Finance**: Directly query for a stock through the web API, or download a dump of .csv files and use them. <br/>
https://ca.finance.yahoo.com/<br>
**Bloomberg API**: Multiple APIs available, including Python.<br/>
https://www.programmableweb.com/api/bloomberg<br>
**Quandl**: Also multiple APIs, including Python.<br/>
https://www.quandl.com/<br>

Project Details
---------------
Detailed information about the project **Capstone Proposal** can be found here [PROPOSAL.md](https://github.com/cviejom/Investment-and-Trading/blob/master/PROPOSAL.md).

https://docs.google.com/document/d/1ycGeb1QYKATG6jvz74SAMqxrlek9Ed4RYrzWNhWS-0Q/pub

Project Resources
-----------------
Courses
Machine Learning for Trading, Tucker Balch (Georgia Tech and Udacity): https://www.google.com/url?q=https://www.udacity.com/course/machine-learning-for-trading--ud501&sa=D&ust=1562198292357000

Stocks and Bonds, Khan Academy: https://www.google.com/url?q=https://www.khanacademy.org/economics-finance-domain/core-finance/stock-and-bonds&sa=D&ust=1562198292358000

Cookiecutter Data Science: https://drivendata.github.io/cookiecutter-data-science/

Contributing
------------
Please see [CONTRIBUTING.md](https://github.com/cviejom/Investment-and-Trading/blob/master/CONTRIBUTING.md) if you want to help

Licence
-------
The MIT License (MIT)
Copyright (c) 2019, cviejom
May be redistributed under the terms specified in the [LICENSE](https://github.com/cviejom/Investment-and-Trading/blob/master/LICENSE) file.

About this Project
------------------
This project was created as a capstone project for **Udacity**, the goal is to build an end to end **Machine Learning** solution