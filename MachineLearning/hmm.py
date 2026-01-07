import numpy as np
from hmmlearn.hmm import CategoricalHMM

# Hidden states
states = ['Sunny', 'Cloudy', 'Rainy']

# Observations
observations = ['Normal', 'Umbrella', 'Raincoat']

# Initial probabilities
start_probabilities = np.array([0.3, 0.5, 0.2])

# Transition probabilities
transition_matrix = np.array([
    [0.6, 0.3, 0.1],   # Sunny
    [0.2, 0.5, 0.3],   # Cloudy
    [0.1, 0.4, 0.5]    # Rainy
])

# Emission probabilities
emission_matrix = np.array([
    [0.6, 0.3, 0.1],   # Sunny
    [0.4, 0.4, 0.2],   # Cloudy
    [0.1, 0.4, 0.5]    # Rainy
])

# Create model
model = CategoricalHMM(n_components=3, init_params="")
model.startprob_ = start_probabilities
model.transmat_ = transition_matrix
model.emissionprob_ = emission_matrix

# Observed sequence: Normal, Umbrella, Raincoat
# Normal=0, Umbrella=1, Raincoat=2
observed_sequence = np.array([[0], [1], [2]])

# Decode using Viterbi
log_prob, hidden_states = model.decode(observed_sequence, algorithm="viterbi")

print("Predicted Weather States:")
print([states[state] for state in hidden_states])
