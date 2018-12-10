import os
from sinobotocr.cv2_helper import *
from sinobotocr.tesseract_helper import *
from sinobotocr.my_pdf2img import *

BASE_DIR = "/media/data"

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
        text_blocks = step_3_find_text_lines(table, name)

        logger.error("step_4_read_keyword_and_value ...")
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
    except Exception as e:
        ret['ErrDesc']   = str(e)
        ret['Status']    = "FAIL"

    return ret

file_name = "007.pdf"
full_path = os.path.join(BASE_DIR, file_name) 
path, fname = os.path.split(full_path)
name, extension = os.path.splitext(fname)

if extension == ".pdf" and os.path.exists(full_path):
    ret = ocr_pdf(full_path, file_name, name)
    print(ret)