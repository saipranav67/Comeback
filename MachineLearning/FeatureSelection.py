# %%
import pandas as pd

# %%
import pandas as pd
df=pd.read_csv('breast-cancer.csv')

# %%
df.shape

# %%
df.columns

# %%
df.info()

# %%
X=df.drop('diagnosis',axis=1)
Y=df['diagnosis']

# %%
X.shape

# %%
X.isna().sum()


# %%
X = X.drop(columns=['Unnamed: 32'])

# %%
X.isna().sum()

# %%
Y.shape

# %%
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
Y = le.fit_transform(Y)


# %%
from sklearn.feature_selection import f_classif

# Compute F-statistic and p-values for each feature
F_statistic, p_values = f_classif(X, Y)

# Create a DataFrame to display the F-statistics and p-values for each feature
f_statistic_df = pd.DataFrame({
    'Feature': X.columns,
    'F-statistic': F_statistic,
    'p_values': p_values
})

# Sort the DataFrame by F-statistic in descending order
f_statistic_df_sorted = f_statistic_df.sort_values(by='F-statistic', ascending=False)

# Display the sorted results
print(f_statistic_df_sorted)


# %%
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif, chi2, mutual_info_classif
from sklearn.preprocessing import MinMaxScaler


# %%
# 1. Split first
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42
)

# %%
# 2. Feature selection
selector = SelectKBest(score_func=f_classif, k=7)
X_train_selected = selector.fit_transform(X_train, y_train)
X_test_selected = selector.transform(X_test)

# %%

# # Get the selected feature columns (boolean mask)
selected_columns = X.columns[selector.get_support()]

# # Print the names of the selected features
print("Selected Features:", selected_columns)

# %%
# 3. Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_selected)
X_test_scaled = scaler.transform(X_test_selected)

# %%
# 4. Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# %%
y_pred = model.predict(X_test_scaled)
y_pred

# %%
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)


# %%
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"Classification Report:\n{class_report}")

# %%
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

cm = confusion_matrix(y_test, y_pred)

plt.figure()
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.colorbar()

plt.xlabel("Predicted Label")
plt.ylabel("True Label")

# Show values inside cells
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.show()


# %%
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# %%
y_prob = model.predict_proba(X_test_scaled)[:, 1]

# Compute the ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# Calculate the AUC (Area Under the Curve)
roc_auc = roc_auc_score(y_test, y_prob)

# Plot the ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')  # Diagonal line (random classifier)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate (Recall)')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

# Optionally, you can print the AUC value
print(f"AUC (Area Under the Curve): {roc_auc:.2f}")

# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plt.scatter(range(len(y_test)), y_test, color='blue', label='True Values', alpha=0.6)
plt.scatter(range(len(y_test)), y_pred, color='red', label='Predicted Values', alpha=0.6)
plt.xlabel('Sample Index')
plt.ylabel('Target Value')
plt.title('Scatter Plot of True vs Predicted Values')
plt.legend()
plt.show()

# %% [markdown]
# #CHi2 test

# %%
# 1. Split first
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42
)

# %%
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# %%
# Select
selector = SelectKBest(score_func=chi2, k=7)
X_train_selected = selector.fit_transform(X_train_scaled, y_train)
X_test_selected = selector.transform(X_test_scaled)

# %%
# Feature names
selected_columns = X_train.columns[selector.get_support()]
print("Selected Features:", selected_columns)

# %%
# 4. Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_selected, y_train)

# %%
y_pred = model.predict(X_test_selected)

# %%
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# %%
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"Classification Report:\n{class_report}")

# %%
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

cm = confusion_matrix(y_test, y_pred)

plt.figure()
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.colorbar()

plt.xlabel("Predicted Label")
plt.ylabel("True Label")

# Show values inside cells
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.show()


# %%
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# %%
y_prob = model.predict_proba(X_test_selected)[:, 1]

# Compute the ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# Calculate the AUC (Area Under the Curve)
roc_auc = roc_auc_score(y_test, y_prob)

# Plot the ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')  # Diagonal line (random classifier)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate (Recall)')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

# Optionally, you can print the AUC value
print(f"AUC (Area Under the Curve): {roc_auc:.2f}")

# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plt.scatter(range(len(y_test)), y_test, color='blue', label='True Values', alpha=0.6)
plt.scatter(range(len(y_test)), y_pred, color='red', label='Predicted Values', alpha=0.6)
plt.xlabel('Sample Index')
plt.ylabel('Target Value')
plt.title('Scatter Plot of True vs Predicted Values')
plt.legend()
plt.show()

# %% [markdown]
# mutual_info_classif

# %%
# 1. Train–test split
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42
)

# 2. Feature selection (NO scaling here)
selector = SelectKBest(score_func=mutual_info_classif, k=7)
X_train_selected = selector.fit_transform(X_train, y_train)
X_test_selected = selector.transform(X_test)

selected_columns = X_train.columns[selector.get_support()]
print("Selected Features:", selected_columns)

# 3. Scaling (ONLY because Logistic Regression needs it)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_selected)
X_test_scaled = scaler.transform(X_test_selected)


# %%
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# %%
y_pred = model.predict(X_test_scaled)

# %%
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# %%
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"Classification Report:\n{class_report}")

# %%
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

cm = confusion_matrix(y_test, y_pred)

plt.figure()
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.colorbar()

plt.xlabel("Predicted Label")
plt.ylabel("True Label")

# Show values inside cells
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.show()


# %%
y_prob = model.predict_proba(X_test_scaled)[:, 1]

# Compute the ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# Calculate the AUC (Area Under the Curve)
roc_auc = roc_auc_score(y_test, y_prob)

# Plot the ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')  # Diagonal line (random classifier)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate (Recall)')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

# Optionally, you can print the AUC value
print(f"AUC (Area Under the Curve): {roc_auc:.2f}")

# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plt.scatter(range(len(y_test)), y_test, color='blue', label='True Values', alpha=0.6)
plt.scatter(range(len(y_test)), y_pred, color='red', label='Predicted Values', alpha=0.6)
plt.xlabel('Sample Index')
plt.ylabel('Target Value')
plt.title('Scatter Plot of True vs Predicted Values')
plt.legend()
plt.show()


