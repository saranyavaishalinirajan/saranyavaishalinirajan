import os
import pandas as pd
import numpy as np

os.chdir("C:/Users/chait/Desktop")  # Make sure directory is where the 'apy.csv' file is

df = pd.read_csv('apy_1.csv')

# QUESTION 1
# ----------
# season = df.groupby('Season')

# kharif = season.get_group('Kharif     ')
# print('Kharif Production: ', kharif['Production'].aggregate(np.sum))

# summer = season.get_group('Summer     ')
# print('Summer Production: ', summer['Production'].aggregate(np.sum))

# autumn = season.get_group('Autumn     ')
# print('Autumn Production: ', autumn['Production'].aggregate(np.sum))
