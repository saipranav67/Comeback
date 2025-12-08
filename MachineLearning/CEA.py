import numpy as np 
import pandas as pd

# ---- 1. Read CSV ----
data = pd.read_csv('ceadataset1.csv')
print(data.info())
unique_dict = {col: data[col].unique().tolist() for col in data.columns}
print(unique_dict)

# All columns except last = concepts, last column = target
concepts = np.array(data.iloc[:, 0:-1])
target   = np.array(data.iloc[:, -1])

# ---- 2. Candidate Elimination (very simple version) ----
def learn(concepts, target): 
    # Take first training example as initial specific hypothesis
    specific_h = concepts[0].copy()
    print("Initial Specific_h:\n", specific_h)

    # Most general hypotheses (matrix of '?')
    general_h = [["?" for _ in range(len(specific_h))] 
                 for _ in range(len(specific_h))]
    print("Initial General_h:\n", general_h)
    print("\n")

    # Go through all training examples
    for i, h in enumerate(concepts):
        if target[i].lower() == "yes":   # Positive example
            print(f"Instance {i+1} is Positive")
            for x in range(len(specific_h)): 
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'

        elif target[i].lower() == "no":  # Negative example
            print(f"Instance {i+1} is Negative")
            for x in range(len(specific_h)): 
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'

        print("Step", i+1)
        print("Specific_h:", specific_h)
        print("General_h:", general_h)
        print("\n")

    # Remove fully '?' rows from G
    empty = ["?"] * len(specific_h)
    general_h = [g for g in general_h if g != empty]

    return specific_h, general_h

# ---- 3. Run learning ----
s_final, g_final = learn(concepts, target)

print("Final Specific_h:")
print(s_final)

print("\nFinal General_h:")
for g in g_final:
    print(g)
