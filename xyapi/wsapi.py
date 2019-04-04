# coding=UTF-8

import functools, os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.exceptions import abort
from sinobotocr.cv2_helper import *
from sinobotocr.tesseract_helper import *
from sinobotocr.my_pdf2img import *
from sinobotocr.cv2_helper2 import *

logger = get_my_logger()

bp = Blueprint('wsapi', __name__, url_prefix='/api/1.0')

BASE_DIR = "/media/data"

@bp.before_app_request
def load_logged_in_user():
    pass

def make_unicode(input):
    input =  input.encode('utf-8')
    return input

def ocr_pdf(file_path, file_name, name):
    ret = {}
    try:    
        # start to process
        logger.error("Get image from pdf from %s" % file_path)
        dest_file = getImageFromPDF(file_path)

        logger.error("step_1_pre_processing_image ...")
        orig, canny = step_1_pre_processing_image(dest_file)
        
        logger.error("step_2_location_table ...")
        table       = step_2_location_table(orig, canny)
        
        logger.error("step_3_find_text_lines ...")
        text_blocks = step_3_find_text_lines_v2(table, name)

        logger.error("step_4_read_keyword_and_value ...")
        areas, ztgz, confidence = step_4_read_keyword_and_value_v2(text_blocks, name)

        # construct result
        ret['filename']  = file_name
        if len(areas) == 2:
            ret['heji1'] = areas[0]
            ret['heji2'] = areas[1]
        else:
            ret['heji1'] = "0.0"
            ret['heji2'] = "0.0"
        ret['ztgz']      = ztgz
        ret['confident'] = float('%.2f' % (confidence * 100 ))
        ret['Status']    = "OK"
        ret['ErrDesc']   = ""
    except Exception as e:
        ret['ErrDesc']   = str(e)
        ret['Status']    = "FAIL"

    return ret

@bp.route('/get/data', methods=['POST'])
def get_data_from_pdf():
    if request.method == 'POST':
        ret = {}
        file_name = request.form['datafile']
        full_path = os.path.join(BASE_DIR, file_name) 
        path, fname = os.path.split(full_path)
        name, extension = os.path.splitext(fname)

        logger.error("start to process %s" % full_path)
        flag = os.path.exists(full_path)
        if flag and extension == ".pdf" or extension == ".PDF":
            ret = ocr_pdf(full_path, file_name, name)
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
