import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")


# Add 'overweight' column
df['overweight'] = np.where(df["weight"]/(df['height']/100)**2 > 25,1,0 )


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['gluc'] = np.where(df["gluc"] > 1,1,0 )
df['cholesterol'] = np.where(df["cholesterol"] > 1,1,0 )
# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars="cardio",value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])
    

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.

    fig = sns.catplot(data=df_cat, kind="count", x="variable", hue="value", col="cardio")

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) ]
    df_heat = df_heat[(df_heat["weight"] >= df_heat['weight'].quantile(0.025)) & (df_heat["weight"] <= df_heat['weight'].quantile(0.975))]
    df_heat = df_heat[df_heat['ap_lo'] <= df_heat['ap_hi']]
    

    # Calculate the correlation matrix
    corr = np.round(df_heat.corr(),1)
    
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=np.bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(9,9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr,mask=mask,square=True, annot=True)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
draw_heat_map()

