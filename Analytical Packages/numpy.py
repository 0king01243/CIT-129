import numpy
import pandas as pd
from pandas import DataFrame, Series
import csv
import matplotlib


seriesObj = Series([4,7,-5,3])
print(seriesObj)
seriesWithLabels = Series([4,7,8,-3], ['t','g','k','u'])
print(seriesWithLabels)

# Read in energy CSV with csv and feed into a DataFrame which Pandas can visualize

with open('usaPowerSources2001-2018.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    energy = [row for row in reader]
energyDF = DataFrame(energy)
print(energyDF)
energyPD = pandas.read_csv('usaPowerSources2001-2018.csv',index_column)
print(energyPD.solar.describe())
energyPD.plot()

