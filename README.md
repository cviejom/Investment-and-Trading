Investment-and-Trading
==============================

Stock market analysis/prediction is one of the most challenging fields to estimate due to the multi-dimensionality and complexity of the inputs. There can be many factors involved in the calculations varying from multiple company/competitor interactions and competition, public perception, rational and irrational behaviour of traders and many others, the combinations of all these aspects together make price volatile and challenging to predict.


Project Organization
------------

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


# Investment and Trading
### Machine Learning for Stock Market Investing
This project, consists on building a stock price predictor that takes daily trading data over a certain date range as input, and outputs projected estimates for given query dates. Note that the inputs will contain multiple metrics, such as opening price (Open), highest price the stock traded at (High), how many stocks were traded (Volume) and closing price adjusted for stock splits and dividends (Adjusted Close); your system only needs to predict the Adjusted Close price.

Data
----
There are several open sources for historical stock price data sources that could be used:

**Yahoo! Finance**: Directly query for a stock through the web API, or download a dump of .csv files and use them. <br/>
https://ca.finance.yahoo.com/

**Bloomberg API**: Multiple APIs available, including Python.<br/>
https://www.programmableweb.com/api/bloomberg

**Quandl**: Also multiple APIs, including Python.<br/>
https://www.quandl.com/

Look for an API endpoint/library function that lets you obtain daily stock values such as Open, High, Low, Close, Volume and Adjusted Close. Remember that Adjusted Close is what you are trying to predict.

Project Details
---------------
https://docs.google.com/document/d/1ycGeb1QYKATG6jvz74SAMqxrlek9Ed4RYrzWNhWS-0Q/pub

Project Resources
-----------------
Courses
Machine Learning for Trading, Tucker Balch (Georgia Tech and Udacity) <br/>
https://www.google.com/url?q=https://www.udacity.com/course/machine-learning-for-trading--ud501&sa=D&ust=1562198292357000

Stocks and Bonds, Khan Academy <br/>
https://www.google.com/url?q=https://www.khanacademy.org/economics-finance-domain/core-finance/stock-and-bonds&sa=D&ust=1562198292358000

Contributing
------------
Please see [LICENSE](https://github.com/cviejom/Investment-and-Trading/blob/master/LICENSE).

Licence
-------
The MIT License (MIT)
Copyright (c) 2019, cviejom
May be redistributed under the terms specified in the LICENSE file.
[CONTRIBUTING.md](https://github.com/cviejom/Investment-and-Trading/blob/master/CONTRIBUTING.md).


About this Project
------------------
This project was created as a capstone project for Udacity, the goal is to build an end to end machine learning solution