from flask import jsonify
from flask import request
from flask_login import login_required
from app.devices import bp
from core import devices as core
from app.const_and_app_enum.constants import Constants


@bp.route("/")
def get_devices():
    return "helllo world"
