import pickle, re
from submodules.retrieve_song import get_song_id, get_song_features


def predict_popularity(songname, model):

	songid = get_song_id(songname)
	if songid == "Unable to find specified song.":
		return "Unable to find specified song."
	song_features = get_song_features(songid)
	if model == "xgboost":
		loaded_model = pickle.load(open("./models/xgboost_model", "rb"))
		prediction = loaded_model.predict_proba(song_features.iloc[0])
		prediction = round(prediction[0][1], 2)
	
	return str(prediction)
