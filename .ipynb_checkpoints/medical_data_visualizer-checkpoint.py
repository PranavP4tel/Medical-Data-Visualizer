import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("./medical_examination.csv")

# 2
def label_overweight(x):
    if (x['weight']/(x['height']/100)**2)>25:
      return 1
    else:
       return 0

df['overweight'] = df.apply(label_overweight, axis=1)

# 3
'''Normalize the data by making 0 always good and 1 always bad. 
If the value of cholesterol or gluc is 1, make the value 0. 
If the value is more than 1, make the value 1.'''

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x==1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x==1 else 1)

# 4
def draw_cat_plot():
    # 5
    df_cat=df.melt(id_vars=['cardio'],value_vars=sorted(['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']))

    # 8
    fig = sns.catplot(x = "variable", col = "cardio", kind = "count", data = df_cat, hue = "value")


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.query("ap_lo<=ap_hi & height>=159.0 & height<=180 & weight>=51.0 & weight<=108")

    # 12
    corr = np.corrcoef(df_heat)

    # 13
    mask = np.triu(corr, k = 1)



    # 14
    fig, ax = plt.subplots()

    # 15
    fig = sns.heatmap(mask, cmap = "magma", annot = True)

    # 16
    fig.savefig('heatmap.png')
    return fig