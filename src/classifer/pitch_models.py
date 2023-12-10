import numpy as np


class PitchClassifier:
    def __init__(self, alpha=1):
        self.alpha = alpha
        self.pitch_types = None
        self.pitch_type_counts = {}
        self.total_pitch_types = {}
        self.pitch_type_prior_probs = {}

    def _tokenize(self, pitch_data):
        # Simple tokenizer, you may want to improve this based on your specific use case
        # For simplicity, we'll use all the features as tokens
        return list(pitch_data.keys())

    def fit(self, X, y):
        self.pitch_types = np.unique(y)

        for pitch_type in self.pitch_types:
            X_pitch_type = [X[i] for i in range(len(X)) if y[i] == pitch_type]

            feature_counts = {}
            total_features = 0
            for pitch_data in X_pitch_type:
                tokens = self._tokenize(pitch_data)
                for token in tokens:
                    feature_counts[token] = feature_counts.get(token, 0) + 1
                    total_features += 1

            self.pitch_type_counts[pitch_type] = feature_counts
            self.total_pitch_types[pitch_type] = total_features
            self.pitch_type_prior_probs[pitch_type] = len(X_pitch_type) / len(X)

    def _calculate_likelihood(self, feature, pitch_type):
        return (self.pitch_type_counts[pitch_type].get(feature, 0) + self.alpha) / \
               (self.total_pitch_types[pitch_type] + self.alpha * len(self.pitch_type_counts[pitch_type]))

    def predict(self, X):
        predictions = []

        for pitch_data in X:
            tokens = self._tokenize(pitch_data)
            posterior_probs = {pitch_type: np.log(self.pitch_type_prior_probs[pitch_type]) for pitch_type in self.pitch_types}

            for feature in tokens:
                for pitch_type in self.pitch_types:
                    likelihood = self._calculate_likelihood(feature, pitch_type)
                    posterior_probs[pitch_type] += np.log(likelihood)

            predicted_pitch_type = max(posterior_probs, key=posterior_probs.get)
            predictions.append(predicted_pitch_type)

        return predictions
