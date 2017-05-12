import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
prices = []

def get_data(filename):
	with open (filename,'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)