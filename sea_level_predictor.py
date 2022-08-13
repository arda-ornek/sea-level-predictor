import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    print(df.info())
    print(df.head())
    # Create scatter plot
    """ ax = plt.axes()
    ax.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0]) """
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c ="blue")
    
    # Create first line of best fit
    """ x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    result = linregress(x, y)
    slope = result.slope
    intercept = result.intercept
    y_hat = slope*x + intercept
    plt.plot(x,y_hat,color="red") """

    slope, intercept, r_value, p_value, std_err = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    year_extended = list(range(1880, 2051, 1))
    line = [intercept + slope * j for j in year_extended]
    plt.plot(year_extended, line, linewidth=2, color="r")

    # Create second line of best fit

    mod_df = df.loc[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x=mod_df["Year"], y=mod_df["CSIRO Adjusted Sea Level"])
    year2 = list(range(2000, 2051, 1))
    line2 = [intercept2 + slope2 * j for j in year2]
    plt.plot(year2, line2, linewidth=3, color="k")


    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()