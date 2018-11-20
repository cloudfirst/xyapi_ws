# coding=UTF-8

import functools, os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.exceptions import abort
from sinobotocr.cv2_helper import *
from sinobotocr.tesseract_helper import *

bp = Blueprint('wsapi', __name__, url_prefix='/api/1.0')

BASE_DIR = "/media/data"

@bp.before_app_request
def load_logged_in_user():
    pass

@bp.route('/get/data', methods=['POST'])
def get_data_from_pdf():
    if request.method == 'POST':
        ret = {}
        file_name = request.form['datafile']
        full_path = os.path.join(BASE_DIR, file_name) 
        name, extention = os.path.splitext(file_name) 
        if extention == ".pdf" and os.path.exists(full_path):
            # start to process
            ret['filename']  = file_name
            ret['heji1']     = '123.45'
            ret['heji2']     = '34.56'
            ret['ztgz']      = u"鋼筋混凝土造"
            ret['confident'] = 0.8
            ret['Status']    = "OK"
            ret['ErrDesc']   = ""
        else:
            # abort(400, "invalid file name: %s." % file_name)
            # start to process
            ret['filename']  = file_name
            ret['heji1']     = ''
            ret['heji2']     = ''
            ret['ztgz']      = u""
            ret['confident'] = 0
            ret['Status']    = "FAIL"
            ret['ErrDesc']   = "invalid file name: %s." % file_name
        
        return jsonify(ret)

    
