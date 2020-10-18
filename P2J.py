# P2J.py
import argparse
from PIL import Image
import os

print(f'loading P2J.py: __name__ = {__name__}')

def png_to_jpeg(image_name,image_path):
	
	image_rel_path = os.path.join(image_path,image_name)
	#image_abs_path = os.path.abspath(image_rel_path)
	
	im = Image.open(image_rel_path)
	rgb_im = im.convert('RGB')
	rgb_im.save(os.path.join(image_path,".".join([image_name[:-4],'jpeg'])))

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

if __name__ == '__main__':
	
	png_to_jpeg(args.image_name,args.image_path)
	
