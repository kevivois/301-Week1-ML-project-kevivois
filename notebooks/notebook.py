# %% [markdown]
# # MiniLab 1: Fuel Consumption Analysis

# %%
import pandas as pd
import numpy as np
from isc301.config import houses_raw_path
from isc301.training import data_processing,model_predict,model_fit
import matplotlib.pyplot as plt

# %%
df = pd.read_csv(houses_raw_path)
df.head()

# %%
df.plot.scatter("qualite_materiau",'prix')

# %%


# %%
df.plot.scatter("surf_hab",'prix')

# %%
df.plot.scatter("surface_sous_sol","prix")

# %%
df.plot.scatter("qualite_globale","prix")

# %%
df.plot.scatter("surface_jardin","prix")

# %%




df.boxplot(column="surf_hab")


# %%
import seaborn as sns

sns.scatterplot(data=df, x="n_garage_voitures", y="prix", hue="type_batiment", palette="Set2")

# %%
df.boxplot(column="qualite_globale")

# %%
df.boxplot(column="surface_sous_sol")

# %% [markdown]
# 

# %%
df.plot.scatter("n_garage_voitures","prix")

# %%
from sklearn.model_selection import train_test_split




X,Y,X_train, Y_train,X_test, Y_test,X_val,Y_val = data_processing(df)


print(f"Train shape: {X_train.shape}")
print(f"Test shape: {X_test.shape}")
print(f"Validation shape: {X_val.shape}")

# %%





# %%
import matplotlib.pyplot as plt



model, poly = model_fit(X_train, Y_train)



# %%
y_pred_train = model_predict(poly,model,X_train)

residuals = Y_train - y_pred_train
#df_train["residuals"] = residuals
plt.scatter(Y_train, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel("Prices")
plt.ylabel("Residuals")
plt.title("Model Prices residuals (train set)")
plt.show()
print("mean of residuals:", np.mean(np.abs(residuals)))
print(Y_train.shape)

# %%


y_pred = model_predict(poly,model,X_val)
residuals = Y_val - y_pred
#df_train["residuals"] = residuals
plt.scatter(Y_val, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel("Prices")
plt.ylabel("Residuals")
plt.title("Model Prices residuals")
plt.show()
print("mean of residuals:", np.mean(np.abs(residuals)))
print(Y_val.shape)




# %%

import matplotlib.pyplot as plt

plt.scatter(Y_val, y_pred, alpha=0.5)
plt.xlabel("True Prices")
plt.ylabel("Predicted Prices")
plt.axline((0, 0), slope=1, color='red', linestyle='--')
plt.title("True vs Predicted Prices")
plt.show()

# %%
from sklearn.metrics import r2_score

r2 = r2_score(Y_val, y_pred)
print("R² score:", r2)



