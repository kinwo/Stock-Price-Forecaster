from __future__ import division

# Core
import numpy as np
import pandas as pd
from datetime import date, datetime, timedelta
from data_loader import DataLoader
from ETL import ETL

# Data Visualization
# %matplotlib inline
import matplotlib.pyplot as plt
from IPython.display import display

# Supervised Learning
from sklearn import grid_search
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

# Unsupervised Learning / PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# Misc
from os import getcwd
import operator
from math import floor

# Page Configuration
pd.set_option('display.max_columns', 200)

class Forecaster:
	def __init__(self, dataloader, symbol):
		self.label_ready = False
		self.label_name = None

		self.symbol = symbol
		self.e = ETL(dataloader, symbol)
		self.x_days = None
		self.df_main = self.e.df_temp

	def set_x_days(self, x):
		self.x_days = x
		self._make_label()

	def _make_label(self):
		if self.x_days is None or type(self.x_days) is not type(1):
			raise ValueError("Please set how far in the future would you like to forecast.")

		elif self.label_ready:
			self.df_main.drop([self.label_name], axis=1, inplace=True)
			self.label_name = self.symbol + str(self.x_days) + 'd'
			self.df_main[self.label_name] = self.df_main.shift(-self.x_days)[self.symbol]

		else:
			self.label_ready = True
			self.label_name = self.symbol + str(self.x_days) + 'd'
			self.df_main[self.label_name] = self.df_main.shift(-self.x_days)[self.symbol]




