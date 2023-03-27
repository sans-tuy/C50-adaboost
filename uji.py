# from chefboost import Chefboost as chef
import pandas as pd
import Chefboost as chef

df = pd.read_csv("liver dataset convert.csv")
# print(df)

# df['liver'] = df['liver'].map({2:-1,1:1})
# print(df)

# df['decision'] = df['decision'].map({2:'normal',1:'liver'})
print(df)

# config =  {'enableAdaboost': True, 'num_of_weak_classifier': 10, 'enableParallelism': False}
config =  {'algorithm': 'C4.5', 'enableParallelism': False}
model = chef.fit(df.copy(), config=config, target_label = 'decision')

# print("result actual" + " - " + "result prediction")
# # print('ini model', model)
# for index, instance in df.iterrows():
#     prediction = chef.predict(model, instance)
#     actual = instance['liver']
#     if actual == float(prediction):
#         classified = True
#     else :
#         classified = False
#         print("*", end=" ")
#     print(str(actual) + " - " + str(prediction))