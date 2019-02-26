#%%
# get stuff set up
import os
import nilearn as nil
from nilearn import plotting
import nibabel as nib
import pandas as pd
import numpy as np
import crazyscripts
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

#%%
# look at the data
for i, j, fl in os.walk("data/JHU_VBM"):
    for eachfile in fl:
        if eachfile.endswith(".nii"):
            plotting.plot_anat(os.path.join(i, eachfile), title=eachfile)
            plt.show()

#%%
df = pd.read_excel("data/VH_n216_vs_NV_n135_vs_VNH_n538_covariates.xlsx")
#%%
df.describe()
df.head()
len(df["SubNum"].unique())
df.tail()
df.groupby("Group").mean()

#%%
df["PCLR_Total"].describe()

#%%
df["log10subuse"].describe()

df.describe()

#%%
df["Group_Lab"].describe()
df["Group_Lab"].unique()
df.groupby("Group_Lab").mean()

#%%
df["log10subuse"].plot.hist()
plt.title("log10subuse histogram")

for var in df:
    df[var].plot.hist()
    plt.title(var)

