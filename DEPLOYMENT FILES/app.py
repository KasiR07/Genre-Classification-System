""" Flask server """
import os
import random
from flask import Flask, request, jsonify, render_template
from playsound import playsound
from genre_rec_service import Genre_Recognition_Service

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    audio_file = request.files["UploadedAudio"] # get audio file
    file_name = str(random.randint(0, 100000)) # random string of digits for file name
    audio_file.save(file_name) # save the file locally
    grs = Genre_Recognition_Service() # invoke the genre recognition service
    prediction = grs.predict(file_name) # make prediction
    os.remove(file_name) # remove the .wav file
    prediction_message = f"""The song is predicted to be in the {prediction} genre.""" # message to be displayed on the html webpage
    return render_template("index.html", prediction_text=prediction_message)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)
