import requests
from multiprocessing import Process, Lock
from flask import Blueprint, make_response, request

# from multiprocessing import Process, Queue
bp = Blueprint("models", __name__, url_prefix="/models")


# if the model isn't run in a separate thread, it blocks the entire server
def asr_model_thread():
    pass

# using mutliprocessing to sidestep GIL
model_init_process = Process(target=asr_model_thread)
model_init_process.start()


@bp.route("/transcribe", methods=["GET", "POST"])
def transcribe():
    """
    Endpoint URI: /models/transcribe

    Expects a JSON object in the request body with the following:
    * ``audio_url`` - (``String`` | ``str``) The URL/URI to the audio stream to be transcribed

    For example:

        {
            "audio_url": "https://livetraffic2.near.aero/stream/KDAB_132875.mp3"
        }
    """
    request_body = request.get_data()
    print(request_body)
    # response = requests.get(request_body["audio_url"])
    return make_response("Service has not been implemented", 501)
