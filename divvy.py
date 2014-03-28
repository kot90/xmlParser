import pandas as pd 
import numpy as np

#this is a local copy of the file, make sure that you replace this location w/your own location
df = pd.read_csv('/Users/jhbco/Desktop/Divvy Data/Divvy_Trips_2013.csv', low_memory= False)

#print df[df.gender == 'Female'].count().gender

tdmale = df[df.gender == 'Male'].tripduration
tdfemale = df[df.gender == 'Female'].tripduration

mean_male = np.mean(tdmale) / 60

mean_female = np.mean(tdfemale) / 60

print "The mean tripduration for males is %s" %mean_male

print "The mean tripduration for females is %s" %mean_female