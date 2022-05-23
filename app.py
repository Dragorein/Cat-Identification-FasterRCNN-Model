import os
from flask import Flask, request, jsonify, request
import json
from identificationModel import identify
import pickle
from PIL import Image 
import io
import base64

UPLOAD_FOLDER = './images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

class Config:

	def __init__(self):

		# Print the process or not
		self.verbose = True

		# Name of base network
		self.network = 'vgg'

		# Setting for data augmentation
		self.use_horizontal_flips = False
		self.use_vertical_flips = False
		self.rot_90 = False

		# Anchor box scales
		# Note that if im_size is smaller, anchor_box_scales should be scaled
		# Original anchor_box_scales in the paper is [128, 256, 512]
		self.anchor_box_scales = [64, 128, 256] 

		# Anchor box ratios
		self.anchor_box_ratios = [[1, 1], [1./math.sqrt(2), 2./math.sqrt(2)], [2./math.sqrt(2), 1./math.sqrt(2)]]

		# Size to resize the smallest side of the image
		# Original setting in paper is 600. Set to 300 in here to save training time
		self.im_size = 300

		# image channel-wise mean to subtract
		self.img_channel_mean = [103.939, 116.779, 123.68]
		self.img_scaling_factor = 1.0

		# number of ROIs at once
		self.num_rois = 4

		# stride at the RPN (this depends on the network configuration)
		self.rpn_stride = 16

		self.balanced_classes = False

		# scaling the stdev
		self.std_scaling = 4.0
		self.classifier_regr_std = [8.0, 8.0, 4.0, 4.0]

		# overlaps for RPN
		self.rpn_min_overlap = 0.3
		self.rpn_max_overlap = 0.7

		# overlaps for classifier ROIs
		self.classifier_min_overlap = 0.1
		self.classifier_max_overlap = 0.5

		# placeholder for the class mapping, automatically generated by the parser
		self.class_mapping = None

		self.model_path = None

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict():
    catBreed, imagePath = identify()

    data = {
        "predictionBreed" : catBreed[0][0],
        "predictionAccuracy" : catBreed[0][1],
        "imagePath" : imagePath
    }

    jsonResult = json.dumps(data)
    return jsonResult

@app.route('/', methods=['GET'])
def connectionTest():
    data = {
        "test" : "Connection Establish"
    }

    jsonResult = json.dumps(data)
    return jsonResult

@app.route('/upload', methods=['POST'])
def index() :
	json_req = request.get_json()
	bytesOfImage = json_req['image']
	imageData = base64.b64decode(bytesOfImage)

	img = Image.open(io.BytesIO(imageData))
	img.save('images/image1.jpg')
	succesMessage = {
		"message": "file berhasil disimpan"
	}
	jsonResult = json.dumps(succesMessage)
	return jsonResult

if __name__ == '__main__':
    app.run(host = '192.168.100.155', port=3000, debug=True)