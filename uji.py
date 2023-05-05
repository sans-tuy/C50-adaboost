# from chefboost import Chefboost as chef
import pandas as pd
import Chefboost as chef

df = pd.read_csv("liver dataset convert.csv")
print(df)

config =  {'algorithm': 'C4.5', 'enableParallelism': False, 'boosting': 'adaboost'}
model = chef.fit(df.copy(), config=config, target_label = 'decision')

# config =  {'enableAdaboost': True, 'num_of_weak_classifier': 10, 'enableParallelism': False}
# dfTest = pd.read_csv("liver dataset convert test.csv")

# print("result actual" + " - " + "result prediction")
# for index, instance in dfTest.iterrows():
#     prediction = chef.predict(model, instance)
#     actual = instance['decision']
#     if actual == prediction:
#         classified = True
#     else :
#         classified = False
#         print("*", end=" ")
#     print(actual + " - " + prediction)