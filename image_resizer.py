# image_resizer.py
import argparse
from PIL import Image
import os

print(f'loading image_resizer.py: __name__ = {__name__}')

def image_resize(image_name,image_path,res_p,res_w,res_h) :

	"""
	res_p : Resize by user determined percentage (proportional)
	res_w : resize by user determined width (proportional) 
	res_h : resize by user determined height (proportional) 
	
	"""
	
	image_rel_path = os.path.join(image_path,image_name)
	im = Image.open(image_rel_path)

	if not (res_p is None):
		
		#Make the new image half the width and half the height of the original image
		resized_im = im.resize((round(im.size[0]*res_p), round(im.size[1]*res_p)))

		#Save the cropped image
		resized_im.save(os.path.join(image_path,"".join(["resized_",image_name])))
	
	elif not (res_w is None) and not (res_h is None) :
	
		#Make the new image half the width and half the height of the original image
		resized_im = im.resize((round(im.size[0]*res_w), round(im.size[1]*res_h)))

		#Save the cropped image
		resized_im.save(os.path.join(image_path,"".join(["resized_",image_name])))

	elif not (res_w is None) and (res_h is None) :
	
		#Make the new image half the width and half the height of the original image
		resized_im = im.resize((round(im.size[0]*res_w), round(im.size[1]*1)))

		#Save the cropped image
		resized_im.save(os.path.join(image_path,"".join(["resized_",image_name])))

	elif (res_w is None) and not (res_h is None) :
	
		#Make the new image half the width and half the height of the original image
		resized_im = im.resize((round(im.size[0]*1), round(im.size[1]*res_h)))

		#Save the cropped image
		resized_im.save(os.path.join(image_path,"".join(["resized_",image_name])))
	else :
		print("Please Enter valid arguments !!")
		
parser = argparse.ArgumentParser(description = """
											Select one of the following :
											res_p : Resize by user determined percentage (proportional)
											res_w : resize by user determined width (proportional) 
											res_h : resize by user determined height (proportional) 	
												""")
parser.add_argument('-im',
						'--image_name',
						type = str,
						help = 'Input jpeg image name')

parser.add_argument('-p',
						'--image_path',
						type = str,
						help = 'Input jpeg image folder path')

parser.add_argument('-res_p',
						'--image_resize_proportion',
						type = float,
						help = 'Amount by which the image has to be resized')

parser.add_argument('-res_w',
						'--image_width_resize_proportion',
						type = float,
						help = 'Amount by which the image width has to be resized')
parser.add_argument('-res_h',
						'--image_height_resize_proportion',
						type = float,
						help = 'Amount by which the image height has to be resized')


args = parser.parse_args()

if __name__ == '__main__':
	
	image_resize(args.image_name,args.image_path,args.image_resize_proportion,args.image_width_resize_proportion,args.image_height_resize_proportion)
