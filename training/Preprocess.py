import numpy as np

import math

from training import Training
#from training import Training

def processContinuousFeatures(algorithm, df, column_name, entropy, config):
	# Mencari nilai unik pada suatu fitur yang akan dijadikan nilai treshold dengan jumlah maksimal nilai unik sebanyak 20
	#if True langsung digunakan sebagai nilai unik dan diurutkan
	if df[column_name].nunique() <= 20:
		unique_values = sorted(df[column_name].unique())
	else:
		# akan dicari nilai rata-rata, standar deviasi,minimum, maksimum dari seluruh data pada colom fitur
		# print('\n nama kolom',column_name)
		unique_values = []
		
		df_mean = df[column_name].mean()
		# print(df[column_name].sum(), 'sum', column_name)
		# print(df[column_name].mean(), 'sum', column_name)
		df_std = df[column_name].std(ddof=0)
		df_min = df[column_name].min()
		df_max = df[column_name].max()
		
		unique_values.append(df[column_name].min())
		unique_values.append(df[column_name].max())
		unique_values.append(df[column_name].mean())

		# nilai unik yang digunakan pada data adalah nilai rata-rata yang ditambahkan dengan standar deviasi yang sudah dikalikan dengan skala standar deviasi untuk mendapatkan nilai unik pada kisaran data, nilai + dan - untuk memastikan persebaran data berada pada kiri dan kanan dari nilai rata-rata
		
		scales = list(range(-3,+4, 1))
		for scale in scales:
			if df_mean + scale * df_std > df_min and df_mean + scale * df_std < df_max:
				unique_values.append(df_mean + scale * df_std)
		
		unique_values.sort()
		
	# print(column_name,"->",unique_values)
	
	subset_gainratios = []; subset_gains = []
	
	# bila nilai unik berjumlah satu maka nilai akan langsung digunakan untuk menjadi treshold (binary splitting)
	if len(unique_values) == 1:
		winner_threshold = unique_values[0]
		df[column_name] = np.where(df[column_name] <= winner_threshold, "<="+str(winner_threshold), ">"+str(winner_threshold))
		return df
	
	# multi splitting
	for i in range(0, len(unique_values)-1):
		threshold = unique_values[i]
		# print('\n',threshold)
		
		subset1 = df[df[column_name] <= threshold]
		subset2 = df[df[column_name] > threshold]
		
		subset1_rows = subset1.shape[0]; subset2_rows = subset2.shape[0]
		total_instances = df.shape[0] #subset1_rows+subset2_rows
		# print(subset1_rows, 'subset1_rows')
		# print(subset2_rows, 'subset2_rows')
		# print(total_instances, 'total_instances')
		
		subset1_probability = subset1_rows / total_instances
		subset2_probability = subset2_rows / total_instances
		
		threshold_gain = entropy - subset1_probability*Training.calculateEntropy(subset1, config) - subset2_probability*Training.calculateEntropy(subset2, config)
		subset_gains.append(threshold_gain)
		
		threshold_splitinfo = -subset1_probability * math.log(subset1_probability, 2)-subset2_probability*math.log(subset2_probability, 2)
		gainratio = threshold_gain / threshold_splitinfo
		subset_gainratios.append(gainratio)
		
		#----------------------------------

	winner_one = subset_gainratios.index(max(subset_gainratios))
	
	winner_threshold = unique_values[winner_one]
	# print('\n',column_name,": ", winner_threshold," in ", unique_values)
	df[column_name] = np.where(df[column_name] <= winner_threshold, "<="+str(winner_threshold), ">"+str(winner_threshold))
	
	return df
