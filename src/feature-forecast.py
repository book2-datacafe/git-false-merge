

#### P will be working on this project

import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from prophet import Prophet
from prophet.plot import add_changepoints_to_plot
from prophet.diagnostics import cross_validation
from prophet.diagnostics import performance_metrics
from prophet.plot import plot_cross_validation_metric
from prophet.plot import plot_seasonality
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import mean_absolute_percentage_error
import math
from datetime import date, timedelta
import logging
import scipy.stats as stats
from google.cloud import bigquery
import pandas_gbq
import random

#Get Forecast result and past data to determine ROP from BQ¶

client = bigquery.Client()
sql = """
SELECT
    FORMAT_TIMESTAMP('%Y-%m-%d', CAST(ds AS TIMESTAMP)) AS ds,
    shop_id AS shop_id,
    material_name AS material_name,
    y AS y,
    yhat AS yhat
FROM datacafeplayground.total_supply_chain.table_forecast_material
ORDER BY
  ds,shop_id,material_name;
"""
result= client.query(sql).to_dataframe()

result.head()