from flask import Flask, jsonify, request 
import prediction
import os
import random

def flask_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.route('/predict/lstm', methods=['POST'])
    def lstm_predict():
        # get file from request and save it
        audio_file = request.files['file']
        file_name = str(random.randint(0,100000))

        audio_file.save(file_name)

        # instantiate keyword spotting service singleton and get prediction
        kss = prediction.Keyword_Spotting_Service_LSTM()
        predicted_genre = kss.predict(file_name)

        os.remove(file_name)

        #return result as JSON
        result = {"genre": predicted_genre}
        return jsonify(result)

    @app.route('/predict/gru', methods=['POST'])
    def gru_predict():
        # get file from request and save it
        audio_file = request.files['file']
        file_name = str(random.randint(0,100000))

        audio_file.save(file_name)

        # instantiate keyword spotting service singleton and get prediction
        kss = prediction.Keyword_Spotting_Service_GRU()
        predicted_genre = kss.predict(file_name)

        os.remove(file_name)

        #return result as JSON
        result = {"genre": predicted_genre}
        return jsonify(result)
    return app

app = flask_app()
