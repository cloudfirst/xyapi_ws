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
            dest_file = getImageFromPDF(full_path)
            orig, canny = step_1_pre_processing_image(dest_file)
            table       = step_2_location_table(orig, canny)
            text_blocks = step_3_find_text_lines(table, name)
            areas, ztgz = step_4_read_keyword_and_value(text_blocks, name)

            # construct result
            ret['filename']  = file_name
            if len(areas) == 2:
                ret['heji1'] = areas[0]
                ret['heji2'] = areas[1]
            else:
                ret['heji1'] = "0.0"
                ret['heji2'] = "0.0"
            ret['ztgz']      = ztgz
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

    
