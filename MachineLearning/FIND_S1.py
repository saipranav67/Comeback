# %%
# --- Cell 1: Load Your Dataset ---

import pandas as pd

# Replace "your_dataset.csv" with your actual file name
df = pd.read_csv("Sports_data.csv")
print("Data Set")
print(df)


# %%
# --- Cell 2: Initialize hypothesis and select positive examples ---

target_column = 'enjoy sport'

# Select only positive training examples
positive_examples = df[df[target_column] == 'yes']

# Initialize hypothesis with the most specific values
hypothesis = ['Ø'] * (len(df.columns) - 1)

print("\nPositive Examples- ")
print(positive_examples)



# %%
# --- Cell 3: Find-S algorithm ---

feature_columns = [col for col in df.columns if col != target_column]

for index, row in positive_examples[feature_columns].iterrows():
    for i, attribute in enumerate(row):
        if hypothesis[i] == 'Ø':
            hypothesis[i] = attribute
        elif hypothesis[i] != attribute:
            hypothesis[i] = '?'

#print(hypothesis)


# %%
# --- Cell 4: Final hypothesis---

print("\nFinal Find-S Hypothesis:")
for col, h in zip(feature_columns, hypothesis):
    print(f"{col}: {h}")



