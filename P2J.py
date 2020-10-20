# P2J.py
import argparse
from PIL import Image
import os

print(f'loading P2J.py: __name__ = {__name__}')

print("Creating a new directory to store Converted Png images :")
directory = "Converted_to_jpg"
path = os.path.join('.',directory)

try: 
	os.makedirs(path, exist_ok = True) 
	print("Directory '%s' created successfully" % directory) 
except OSError as error: 
	print("Directory '%s' can not be created" % directory) 


def png_to_jpeg(image_name,image_path):
	if not os.path.isdir(image_path):
		raise ValueError('Input path is not a Directory')
	if(image_name.find(".png") == -1):
		raise ValueError("Input image is not png")
	
	image_rel_path = os.path.join(image_path,image_name)
	#image_abs_path = os.path.abspath(image_rel_path)
	
	im = Image.open(image_rel_path)
	rgb_im = im.convert('RGB')
	rgb_im.save(os.path.join(path,"".join([image_name[:-4],'_png_to_jpg','.jpeg'])))


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Converts Png image to Jpeg')
	parser.add_argument('-im',
							'--image_name',
							type = str,
							help = 'Input png image name')

	parser.add_argument('-p',
							'--image_path',
							type = str,
							help = 'Input png image folder path')
	args = parser.parse_args()
	
	png_to_jpeg(args.image_name,args.image_path)
	
