import numpy as np
import pickle as pkl

def update_time(s):
    return int(s.split()[1][:2])

# Define your prediction method here
# df is a dataframe containing timestamps, weather data and potentials
def my_predict( df ):
	# Load your model file
	with open( "model", "rb" ) as file:
		models = pkl.load( file )
	
	# update Time column
	df['Time'] = df['Time'].apply( update_time )

	# Transform the dataframe into a numpy array and make predictions
	X = df[['no2op1','no2op2','o3op1','o3op2','temp','humidity','Time']].to_numpy()

	# Make two sets of predictions, one for O3 and another for NO2
	pred_o3 = models[0].predict( X )
	pred_no2 = models[1].predict( X )
	
	# Return both sets of predictions
	return ( pred_o3, pred_no2 )