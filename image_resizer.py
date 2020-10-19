# image_resizer.py
import argparse
from PIL import Image
import os

print(f'loading image_resizer.py: __name__ = {__name__}')

def image_resize(dir_path,res_p = None,res_w = None,res_h = None) :

	"""
	dir_path : Path of the folder in which the the images to be resized are present
	res_p : Resize by user determined percentage (proportional)
	res_w : resize by user determined width (proportional) 
	res_h : resize by user determined height (proportional) 
	
	"""
	all_files_in_dir = os.listdir(path = dir_path)
	all_images_in_dir = [image  for image in all_files_in_dir if ('.jpg' in image.lower() ) or ('.png' in image.lower()) or ('.jpeg' in image.lower())]
	
	for image_name in all_images_in_dir:
		
		image_rel_path = os.path.join(dir_path,image_name)
		im = Image.open(image_rel_path)

		if not (res_p is None):
			
			#Make the new image half the width and half the height of the original image
			resized_im = im.resize((round(im.size[0]*res_p), round(im.size[1]*res_p)))

			#Save the cropped image
			resized_im.save(os.path.join(dir_path,"".join(["resized_",image_name])))
		
		elif not (res_w is None) and not (res_h is None) :
		
			#Make the new image half the width and half the height of the original image
			resized_im = im.resize((round(im.size[0]*res_w), round(im.size[1]*res_h)))

			#Save the cropped image
			resized_im.save(os.path.join(dir_path,"".join(["resized_",image_name])))

		elif not (res_w is None) and (res_h is None) :
		
			#Make the new image half the width and half the height of the original image
			resized_im = im.resize((round(im.size[0]*res_w), round(im.size[1]*1)))

			#Save the cropped image
			resized_im.save(os.path.join(dir_path,"".join(["resized_",image_name])))

		elif (res_w is None) and not (res_h is None) :
		
			#Make the new image half the width and half the height of the original image
			resized_im = im.resize((round(im.size[0]*1), round(im.size[1]*res_h)))

			#Save the cropped image
			resized_im.save(os.path.join(dir_path,"".join(["resized_",image_name])))
		else :
			print("Please Enter valid arguments !!")
			

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = """
												dir_path : Path of the folder in which the the images to be resized are present
												
												Select one of the following to resize image :
												res_p : Resize by user determined percentage (proportional)
												res_w : resize by user determined width (proportional) 
												res_h : resize by user determined height (proportional) 	
													""")
	parser.add_argument('-dir',
							'--dir_path',
							type = str,
							help = 'Input images folder path')

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

	image_resize(args.dir_path,args.image_resize_proportion,args.image_width_resize_proportion,args.image_height_resize_proportion)
