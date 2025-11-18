# %%
# --- Cell 1: Create your given dataset ---

import pandas as pd

# data = {
#     'Veg':      ['Veg', 'Veg', 'Non-Veg', 'Veg', 'Veg', 'Non-Veg', 'Veg'],
#     'Spicy':    ['Spicy', 'Normal', 'Spicy', 'Spicy', 'Normal', 'Spicy', 'Spicy'],
#     'Cheap':    ['Cheap', 'Cheap', 'Expensive', 'Cheap', 'Cheap', 'Cheap', 'Expensive'],
#     'Street':   ['Street', 'Restaurant', 'Restaurant', 'Street', 'Restaurant', 'Street', 'Restaurant'],
#     'Popular':  ['Popular', 'Popular', 'Popular', 'New', 'New', 'Popular', 'Popular'],
#     'Yes':      ['Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No']
# }

df = pd.read_csv("C:/Users/saipr/OneDrive/Desktop/Desktop_folders/COMEBACK/MachineLearning/dataset.csv")
print("Data Set")
print(df)


# %%
# --- Cell 2: Select only positive examples (Yes = Yes) ---

target_column = 'Yes'

positive_examples = df[df[target_column] == 'Yes']
print("\nPositive Examples")
print(positive_examples)


# %%
# --- Cell 3: Run Find-S ---

feature_columns = [col for col in df.columns if col != target_column]

hypothesis = ['Ø'] * len(feature_columns)

for index, row in positive_examples[feature_columns].iterrows():
    for i, attribute in enumerate(row):
        if hypothesis[i] == 'Ø':
            hypothesis[i] = attribute
        elif hypothesis[i] != attribute:
            hypothesis[i] = '?'

hypothesis


# %%
# --- Cell 4: Final hypothesis ---

print("\nFinal Find-S Hypothesis:")
for col, h in zip(feature_columns, hypothesis):
    print(f"{col}: {h}")



