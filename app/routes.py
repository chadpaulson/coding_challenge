import logging

import flask
from flask import Response

from app.api import ProfileData, ProfileNotAvailable

app = flask.Flask("user_profiles_api")
logger = flask.logging.create_logger(app)
logger.setLevel(logging.INFO)


@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    profile = ProfileData(username=username)
    try:
        profile_data = profile.fetch_profile_data()
        return flask.jsonify(profile_data)
    except ProfileNotAvailable:
        return Response("Could not find profile.", status=404)

@app.route("/health-check", methods=["GET"])
def health_check():
    """
    Endpoint to health check API
    """
    app.logger.info("Health Check!")
    return Response("All Good!", status=200)
