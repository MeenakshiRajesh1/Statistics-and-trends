# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 20:32:57 2023

@author: iamme
"""

# import Modules
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sts
 
# Define Function 
#1. A function named read_file was defined to read the datas in dataframe

def read_file(filename,countries, years):
    ''' This function is defined to read the datas which was assigned by
    calling the function. From the datas Countries and year will be read
    as the arguments are mentioned so. column named Country Code was 
    dropped and the values are retrieved using loc[] later they are transposed. '''
    
    df1 = pd.read_csv(filename, on_bad_lines=("skip"), skiprows=3, index_col=0)
    df1.drop(columns=("Country Code"), axis=1, inplace= True)
    df1 = df1.loc[countries, years]
    df2 = df1.transpose()
    
    return  df1, df2

# 2. Function to explore dataframe

def des(data):
    '''This function is used to explore the data. Argument of the function
    is given as data to retrieve the datas. .describe() is used to explore
    the dataframe to understand the distribution.'''
    
    print(data.describe())
   

# 3. Function using statistical calculations.

def stat(data):
    '''This function is used to calculate a particular value.
    Statistical tools such as Skewness and Kurtosis are being
    used here to calculate the values passed as the argument called data.'''
    
    print("Skewness: ", sts.skew(data))
    print("Kurtosis: ", sts.kurtosis(data))

# 4. Function to plot

def plot(data, kind, title,x,y):
    ''' Function to plots an insight of the dataframes. Arguments
    such as data, kind, title, x, y are assigned. data get the dataframe, 
    kind,title, x, and y are used to specify which graph to be plotted,label 
    the graph and the coordinates on the graph respectievely'''
    
    data.plot(kind=kind)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend(loc='upper left', bbox_to_anchor = (1.0, 1.0))
    plt.show()
    
    return  

# Assigning variables to take the specific values from the datasets

countries= ["Japan", "Russian Federation",  "United Kingdom", "Brazil", "India", "United States", "Canada", "China"]  
years = ["1990", "1995", "2000", "2005", "2010", "2015"]

# Functions are called and assigned the specific datasets to the variables

df_co2emissions_1, df_co2emissions_2 = read_file("API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5358347.csv", countries, years)
df_gdp_1, df_gdp_2 = read_file("API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5358352.csv", countries, years)
df_enguse_1, df_enguse_2 = read_file("API_EG.USE.PCAP.KG.OE_DS2_en_csv_v2_5358565.csv", countries, years)
df_waterwid_1, df_waterwid_2 = read_file("API_ER.H2O.FWTL.K3_DS2_en_csv_v2_5362986.csv", countries, years)
df_totpop_1,df_totpop_2 = read_file("API_SP.POP.TOTL_DS2_en_csv_v2_5358404.csv", countries, years)

#Specify variables of dataframe called to the function des()

des(df_co2emissions_2)
des(df_enguse_2)
des(df_gdp_2)
des(df_waterwid_2)
des(df_totpop_2)

# Specify variables of dataframe called to the function stat()

stat(df_gdp_2)

# Plotting graphs for dataframes and the figures are saved

plot(df_co2emissions_1, 'bar', 'Carbon Dioxide emissions(kt)', "countries", "rate of Emission")
plt.savefig("plot1.png")
plot(df_gdp_1, 'bar', 'GDP (USD)', 'countries', 'GDP')
plt.savefig("plot2.png")
plot(df_waterwid_2, 'line', 'Water withdrawal', 'years', 'rate of Withdrawal' )
plt.savefig("plot3.png")
plot(df_totpop_2, 'line', 'Total population', 'years', 'population')
plt.savefig("plot4.png")
