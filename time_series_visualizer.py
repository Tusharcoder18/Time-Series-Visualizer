import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')

# Clean data
df = df.sort_values(by='value')
shape = df.shape[0]
df = df.iloc[round(shape * 0.025) : round(shape * 0.975)]
df = df.sort_index()


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20,7))
    ax.plot(df.index, df['value'], color='red')
    ax.set(xlabel='Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar.index.month_name()
    df_bar.index = df_bar.index.year
    df_bar = df_bar.reset_index()
    df_bar = df_bar.rename(columns={'date' : 'year'})
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=months)
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    ax = df_bar.plot(kind='bar', figsize=(10,7), xlabel='Years', ylabel='Average Page Views')
    fig = ax.figure




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'], categories=months)
    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14,7))
    sns.boxplot(x='year', y='value', data=df_box, ax=axs[0])
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')
    axs[0].set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(x='month', y='value', data=df_box, ax=axs[1])
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Page Views')
    axs[1].set_title('Month-wise Box Plot (Seasonality)')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
