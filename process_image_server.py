__author__ = 'zhanghengyang'

from flask import Flask
import os
import json
from flask import request
import uuid
import numpy as np
import cv2
import json
import _process_image as pi
#from _process_image import CRect, Cvec4i

app = Flask(__name__)

path = '/home/ubuntu/ocr/VLRecognitionSuiteServerSO/Debug/image_tmp.jpg'

@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':
        file = request.files['filename']
        _headers = request.headers
        print _headers
        print type(_headers)
        if type(_headers) != 'NoneType':
            ClicenseRect = json.loads( _headers.get('ClicenseRect'))
            CstampRect = json.loads(_headers.get('CstampRect'))
            CenginLine = json.loads(_headers.get('CenginLine'))
            CvinLine = json.loads(_headers.get('CvinLine'))
        r1 = (ClicenseRect[0], ClicenseRect[1], ClicenseRect[2], ClicenseRect[3])
        r2 = (CstampRect[0], CstampRect[1], CstampRect[2], CstampRect[3])
        v1 = (CenginLine[0], CenginLine[1], CenginLine[2], CenginLine[3] )
        v2 = (CvinLine[0], CvinLine[1], CvinLine[2], CvinLine[3])
        #print type(file)
        #data = request.data
        #rstream = file.stream.read()
        #barray = np.asarray(bytearray(rstream))
        #img = cv2.imdecode(barray,1)
        #print "file info",file
        file.save(path)
        file.flush()
        res = pi.process_image(path, r1, r2, v1, v2)
        return json.dumps(res).encode('utf8')


if __name__ == "__main__":
    print "start server!!!"
    app.debug = True
    app.run(host="0.0.0.0",port=8080)
    print "stop server!!!"