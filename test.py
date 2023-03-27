import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

# Fungsi untuk menghitung tingkat kesalahan pada setiap sampel
def calculate_error_rate(model, X, y, weights):
    incorrect = []
    predictions = model.predict(X)
    incorrect.append(predictions != y)
    # print(y,'actual')
    # print(predictions, 'predictions')
    # print((np.sum(predictions == y)/len(predictions))*100, 'akurasi data training')
    error_rate = (np.sum(incorrect * weights) / np.sum(weights))
    # print(error_rate)
    # print(incorrect, 'incorrect')
    return error_rate


# Fungsi untuk menghitung bobot kesalahan total dan koefisien Adaboost
def calculate_error_weight(error_rate):
    # print(0.5 * np.log((1 - error_rate) / error_rate))
    return 0.5 * np.log((1 - error_rate) / error_rate)

# Fungsi untuk mengupdate bobot sampel berdasarkan prediksi model
def update_weights(weights, error_weight, predictions, y):
    incorrect = predictions != y
    factor = np.exp(error_weight * incorrect)
    weights *= factor
    weights /= np.sum(weights)

# Fungsi untuk menggabungkan model-model C4.5
def combine_models(models, error_weights, X):
    predictions = np.zeros(len(X))
    for i, model in enumerate(models):
        model_predictions = model.predict(X)
        model_predictions[model_predictions == 'liver'] = 1
        model_predictions[model_predictions == 'normal'] = -1
        predictions += error_weights[i] * model_predictions.astype(np.float64)
    return np.sign(predictions)

# Fungsi utama Adaboost pada C4.5
def adaboost_c45(X_train, y_train, X_test, y_test, M):
    # Inisialisasi bobot awal setiap sampel dalam data training
    n_samples = len(X_train)
    weights = np.full(n_samples, 1 / n_samples)

    models = []
    error_weights = []
    for m in range(M):
        print('epoch', m + 1)
        # Train model C4.5 pada data training dengan bobot saat ini
        model = DecisionTreeClassifier(criterion='entropy', splitter='random', max_depth=9)
        # print('weights', weights)
        model.fit(X_train, y_train)
        # print(model.score(X=X_train, y=y_train, sample_weight=weights), 'score')
        models.append(model)

        prediksi = model.predict(X_test)
        # Hitung tingkat kesalahan C4.5 pada setiap sampel dalam data training
        error_rate = calculate_error_rate(model, X_train, y_train, weights)
        # print(model.score(X_train, y_train), 'akurasi data training')
        # print(model.score(X_test, y_test), 'akurasi data testing\n')
        print('error_rate', error_rate)

        # Hitung bobot kesalahan total dan koefisien Adaboost
        error_weight = calculate_error_weight(error_rate)
        error_weights.append(error_weight)

        # Tingkatkan bobot sampel yang salah klasifikasi dan kurangi bobot sampel yang benar klasifikasi
        predictions = model.predict(X_train)
        update_weights(weights, error_weight, predictions, y_train)

    # Gabungkan model-model C4.5 untuk membuat model gabungan
    y_pred = combine_models(models, error_weights, X_test)

    return y_pred


# Load dataset iris
# iris = load_iris()
data = pd.read_csv("liver dataset convert.csv")
data2 = pd.read_csv("liver dataset convert test.csv")
X_train = data.drop(columns=['decision'])
X_test = data2.drop(columns=['decision'])
y_train = data.iloc[:, -1]
y_test = data2.iloc[:, -1]

# Terapkan Adaboost pada C4.5 dengan 50 iterasi
y_pred = adaboost_c45(X_train, y_train, X_test, y_test, M=6)
# print(y_pred, 'y_pred')
test = y_test.map({'liver': 1, 'normal': -1})


# # Hitung akurasi prediksi
accuracy = accuracy_score(test, y_pred)
print(f'Akurasi prediksi gabungan: {accuracy:.2f}')

# adaboost menggunakan samme

# dtc = DecisionTreeClassifier(criterion='entropy',splitter='random', max_depth=9)
# dtc.fit(X_train, y_train)
# akurasi = dtc.score(X_test, y_test)
# print("Accuracy pohon:", akurasi)

# ada = AdaBoostClassifier(estimator=dtc, n_estimators=50, learning_rate=2.0, random_state=1)
# ada.fit(X_train, y_train)
# accuracy = ada.score(X_test, y_test)
# print("Accuracy:", accuracy)