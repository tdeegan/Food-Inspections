import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import math


def search_by_zip(dataframe):
    '''The purpose of the search_by_zip function is to find all restaurants that had a failed inspection since 11/1/2016 in ZIP Code 60661
       It receives a DataFrame as an argument and returns a DataFrame with rows matching the aforementioned description'''
    
    fr1 = dataframe[(dataframe['Facility Type'] == 'Restaurant') & (dataframe['Zip'] == 60661) & (dataframe['Results'] == 'Fail')] #apply various filters
    fr1['Inspection Date'] = pd.to_datetime(fr1['Inspection Date']) #convert values in Inspection Date to datetime
    
    return fr1[fr1['Inspection Date'] > '11/1/2016'] #apply recency filter
    
def search_by_location(dataframe): 
    '''The purpose of the search_by_location function is to find all restaurants within 0.5 mi of a target location that failed an inspection since 11/1/16
        It receives a DataFrame as an argument.  This DataFrame contains all of the original data from Food_Inspections.csv
        The return value is a DataFrame with rows matching the aforementioned description sorted by increasing distance from the target location'''
    
    def dcalc(so):#function passed to DataFrame.apply that calculates distance from target location
    
        r = 3961
        la1 = 0.7310728810371 #target location latitude in radians
        lg1 = -1.52971051 #target location longitude in radians
    
        la2 = so['Latitude'] * (math.pi / 180) #convert latitude to radians
        lg2 = so['Longitude'] * (math.pi / 180) #convert longitude to radians
    
        c1 = math.sin((la2-la1)/2)**2
        c2 = (math.sin((lg2-lg1)/2)**2)*math.cos(la2) * math.cos(la1)
        
        p = math.sqrt(c1 + c2)
        
        d = 2*r*math.asin(p)
    
        return d #return distance

    fr1 = dataframe[(dataframe['Facility Type'] == 'Restaurant')  & (dataframe['Results'] == 'Fail')] #apply filters
    fr1['Inspection Date'] = pd.to_datetime(fr1['Inspection Date']) #convert Inspection Date values to datetime
    fr2 = fr1[fr1['Inspection Date'] > '11/1/2016'] #apply recency filter
    
    fr2['distance'] = fr2.apply(dcalc,axis=1) #apply dcalc method for each row, store result in distance column added to DataFrame
    
    fr3 = fr2[fr2['distance'] < 0.5] #apply distance filter
    
    rframe = fr3.sort_values(['distance']) #sort distance values
    
    del rframe['distance'] #remove this column now
    
    return rframe #return DataFrame with sorted rows

def main():

    fr = pd.read_csv('Food_Inspections.csv')

    x = search_by_zip(fr)
    x.to_csv('search_by_zip.csv')

    y = search_by_location(fr)
    y.to_csv('search_by_location.csv')
    
if __name__ == "__main__":
    main()





















