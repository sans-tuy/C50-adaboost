import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
import numpy as np

class AdaboostDecisionTree:
    def __init__(self, n_estimators=50, max_depth=1):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.tree_ensemble = []
        self.alpha_ensemble = []
        self.n_classes = None
    
    def fit(self, X, y):
        # Initialize sample weights
        w = np.ones(len(y)) / len(y)
        print(w)
        
        self.n_classes = len(np.unique(y))
        
        for i in range(self.n_estimators):
            # Sample indices with replacement according to sample weights
            indices = np.random.choice(len(y), size=len(y), replace=True, p=w)
            X_sampled, y_sampled = X[indices], y[indices]

            # Build decision tree using sampled data
            tree = self._build_tree(X_sampled, np.column_stack((X_sampled, y_sampled)), depth=1)
            
            # Predict using decision tree and calculate error rate
            y_pred = self._predict_tree(X_sampled, tree)
            error_rate = np.sum(w[indices] * (1 - (y_pred * y_sampled))) / np.sum(w[indices])
            print(error_rate,'error_rate')
            # Calculate alpha
            alpha = np.log((1 - error_rate) / error_rate) + np.log(self.n_classes - 1)
            print(np.log(self.n_classes - 1), 'alpha')
            # Update sample weights
            w = w * np.exp(alpha * (1 - (y_pred * y_sampled)))
            w = w / np.sum(w)
            
            # Add decision tree and alpha to ensembles
            self.tree_ensemble.append(tree)
            self.alpha_ensemble.append(alpha)
    
    def predict(self, X):
        n_samples = X.shape[0]
        y_pred = np.zeros((n_samples, self.n_classes))
        
        for i in range(self.n_estimators):
            y_pred += self.alpha_ensemble[i] * self._predict_tree(X, self.tree_ensemble[i])
        
        return np.argmax(y_pred, axis=1)
    
    def _build_tree(self, X, Xy, depth):
        node = {}
        
        n_samples, n_features = X.shape
        y = Xy[:, -1]
        
        if len(np.unique(y)) == 1:
            # Leaf node: all samples belong to the same class
            node['class'] = int(y[0])
            return node
        
        if depth == self.max_depth:
            # Leaf node: maximum depth reached
            node['class'] = int(np.bincount(y).argmax())
            return node
        
        # Find best feature and threshold to split data
        best_feature, best_threshold, max_gain_ratio = self._find_split(Xy)
        X_left, X_right, Xy_left, Xy_right = self._split(Xy, best_feature, best_threshold)
        
        if max_gain_ratio == 0:
            # Leaf node: unable to split data further
            node['class'] = int(np.bincount(y).argmax())
            return node
        
        # Recursive split data
        node['feature'] = best_feature
        node['threshold'] = best_threshold
        node['left'] = self._build_tree(X_left, Xy_left, depth + 1)
        node['right'] = self._build_tree(X_right, Xy_right, depth + 1)
        
        return node
    
    def _predict_tree(self, X, tree):
        n_samples = X.shape[0]
        y_pred = np.zeros(n_samples)
        
        for i in range(n_samples):
            node = tree

            while 'class' not in node:
                if X[i, node['feature']] <= node['threshold']:
                    node = node['left']
                else:
                    node = node['right']
            
            y_pred[i] = node['class']
            
        return y_pred

    def _find_split(self, Xy):
        best_feature = None
        best_threshold = None
        max_gain_ratio = -1
        
        n_samples, n_features = Xy.shape
        H_S = self._entropy(Xy[:, -1])
        
        for feature in range(n_features - 1):
            values = np.unique(Xy[:, feature])
            thresholds = (values[:-1] + values[1:]) / 2
            
            for threshold in thresholds:
                X_left, X_right, Xy_left, Xy_right = self._split(Xy, feature, threshold)
                
                if len(X_left) == 0 or len(X_right) == 0:
                    # Unable to split data using this feature-threshold pair
                    continue
                
                # Calculate information gain and split information
                H_S_X = self._entropy_weighted(Xy_left[:, -1], Xy_right[:, -1])
                IG_X = H_S - H_S_X
                H_X = self._entropy(np.concatenate((Xy_left[:, -1], Xy_right[:, -1])))
                
                if H_X == 0:
                    # Unable to split data further using this feature-threshold pair
                    continue
                
                # Calculate gain ratio
                gain_ratio = IG_X / H_X
                
                if gain_ratio > max_gain_ratio:
                    # Found new best feature-threshold pair
                    max_gain_ratio = gain_ratio
                    best_feature = feature
                    best_threshold = threshold
        
        return best_feature, best_threshold, max_gain_ratio

    def _split(self, Xy, feature, threshold):
        mask_left = Xy[:, feature] <= threshold
        mask_right = Xy[:, feature] > threshold
        
        X_left = Xy[mask_left, :-1]
        X_right = Xy[mask_right, :-1]
        Xy_left = Xy[mask_left, :]
        Xy_right = Xy[mask_right, :]
        
        return X_left, X_right, Xy_left, Xy_right

    def _entropy(self, y):
        _, counts = np.unique(y, return_counts=True)
        p = counts / len(y)
        return -np.sum(p * np.log2(p))

    def _entropy_weighted(self, y_left, y_right):
        n_left = len(y_left)
        n_right = len(y_right)
        n_total = n_left + n_right
        
        return (n_left / n_total) * self._entropy(y_left) + (n_right / n_total) * self._entropy(y_right)


from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import KBinsDiscretizer

# Generate synthetic binary classification data
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_classes=2, random_state=1)
est = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform')
X_discretized = est.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_discretized.astype(int), y, test_size=0.2, random_state=1)

# Train Adaboost decision tree
adaboost = AdaboostDecisionTree(n_estimators=50, max_depth=5)
adaboost.fit(X_train, y_train)

# Predict on testing set
y_pred = adaboost.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")