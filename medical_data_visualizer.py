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

    #6
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio','variable','value'], as_index = False).count()

    #7
 
    # 8
    fig = sns.catplot(x = "variable", y = "total", kind = "bar", data = df_cat, hue = "value", col="cardio").fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
      (df['ap_lo']<=df['ap_hi']) &
      (df['height'] >= df['height'].quantile(0.025)) &
      (df['height'] <= df['height'].quantile(0.975)) &
      (df['weight'] >= df['weight'].quantile(0.025)) &
      (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr(method = "pearson")

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots(figsize = (10,10))

    # 15
    sns.heatmap(corr, vmin = 0, vmax = .25, linewidths=1, square = True, mask = mask, annot = True, fmt = ".1f", cbar_kws = {"shrink":0.5})
    sns.color_palette("rocket", as_cmap=True)

    # 16
    fig.savefig('heatmap.png')
    return fig