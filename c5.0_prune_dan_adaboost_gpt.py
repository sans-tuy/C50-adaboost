import numpy as np
import pandas as pd

class Node:
    def __init__(self, is_leaf=False, label=None, attribute=None, children=None):
        self.is_leaf = is_leaf
        self.label = label
        self.attribute = attribute
        self.children = children

class DecisionTree:
    def __init__(self, data, target_attribute):
        self.data = data
        self.target_attribute = target_attribute
        self.tree = self.build_tree(data, target_attribute)

    def build_tree(self, data, target_attribute):
        labels = data[target_attribute].unique()

        if len(labels) == 1:
            return Node(is_leaf=True, label=labels[0])

        if data.empty:
            return Node(is_leaf=True, label=self.majority_vote(self.data[target_attribute]))

        attribute = self.select_attribute(data)

        node = Node(attribute=attribute, children={})
        for value in data[attribute].unique():
            subset = data[data[attribute] == value]

            # seleksi nilai kosong
            if subset.empty:
                child = Node(is_leaf=True, label=self.majority_vote(data[target_attribute]))
            else:
                child = self.build_tree(subset, target_attribute)

            node.children[value] = child

        return node

    def select_attribute(self, data):
        information_gain = []
        for attribute in data.columns[:-1]:
            information_gain.append(self.calculate_information_gain(data, attribute))

        return data.columns[:-1][np.argmax(information_gain)]

    def calculate_entropy(self, data):
        labels = data[self.target_attribute].unique()
        entropy = 0

        for label in labels:
            probability = len(data[data[self.target_attribute] == label]) / len(data)
            entropy += -probability * np.log2(probability)

        return entropy

    def calculate_information_gain(self, data, attribute):
        entropy_before_split = self.calculate_entropy(data)
        entropy_after_split = 0
        for value in data[attribute].unique():
            subset = data[data[attribute] == value]
            entropy_after_split += len(subset) / len(data) * self.calculate_entropy(subset)

        return entropy_before_split - entropy_after_split

    def majority_vote(self, labels):
        return labels.value_counts().idxmax()

    def predict(self, instance):
        current_node = self.tree
        while not current_node.is_leaf:
            attribute = current_node.attribute
            value = instance[attribute]
            current_node = current_node.children[value]
        return current_node.label

class AdaBoost:
    def __init__(self, base_estimator, n_estimators):
        self.base_estimator = base_estimator
        self.n_estimators = n_estimators

    def fit(self, data, target_attribute):
        weights = np.ones(len(data)) / len(data)
        self.estimators = []
        self.estimator_weights = []

        for i in range(self.n_estimators):
            estimator = self.base_estimator(data, target_attribute)
            predictions = data.apply(estimator.predict, axis=1)
            error = np.sum(weights[predictions != data[target_attribute]]) / np.sum(weights)

            alpha = np.log((1 - error) / error)
            weights[predictions == data[target_attribute]] *= np.exp(-alpha)
            weights /= np.sum(weights)

            self.estimators.append(estimator)
            self.estimator_weights.append(alpha)

    def predict(self, instance):
        predictions = []
        for estimator, weight in zip(self.estimators, self.estimator_weights):
            predictions.append(weight * estimator.predict(instance))
        return np.sign(np.sum(predictions))

# contoh penggunaan
data = pd.read_csv('file.txt')
# data['liver'] = data['liver'].map({2:'normal',1:'liver'})
print(data)
adaboost = AdaBoost(DecisionTree, 10)
adaboost.fit(data, 'liver')

# membuat instance baru
new_instance = pd.Series({
    'x1': 0.5,
    'x2': 0.8,
    'x3': 1.0,
    'x4': 0.4
})

# melakukan klasifikasi pada instance baru
prediction = adaboost.predict(new_instance)

print('Prediksi:', prediction)
