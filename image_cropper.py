# image_cropper.py
import argparse
from PIL import Image
import os

print(f'loading image_cropper.py: __name__ = {__name__}')

def image_crop(dir_path,crp_px,crp_p) :

	"""
	dir_path : Path of the folder in which the the images to be cropped are present
	crp_px : Center square/rectangle crop by user-determined pixels (new_width , new_height)
	crp_p : centre square/rectangle crop by user-determined percentage 
	"""
	all_files_in_dir = os.listdir(path = dir_path)
	all_images_in_dir = [image  for image in all_files_in_dir if ('.jpg' in image.lower() ) or ('.png' in image.lower()) or ('.jpeg' in image.lower())]
	images_not_cropped = []
	for image_name in all_images_in_dir:
		
		image_rel_path = os.path.join(dir_path,image_name)
		im = Image.open(image_rel_path)
		width, height = im.size   # Get dimensions

		if crp_p is None:
		
			"""
			crp_px : Image width and height after performing center crop 
			"""
			
			new_width , new_height = crp_px
			"""
			The top left coordinates correspond to (x, y) = (left, top), 
			and the bottom right coordinates correspond to (x, y) = (right, bottom). 
			The area to be cropped is left <= x <right and upper <= y <lower,
			and the pixels of x = right andy = lower are not included.
			"""
			left = (width - new_width)/2
			top = (height - new_height)/2
			right = (width + new_width)/2
			bottom = (height + new_height)/2
			# Save the list of images which couldn't be cropped due to size mismatches
			if (left < 0) or (top < 0) or (right > width) or (bottom > height):
				images_not_cropped.append(image_name) 
			else:
				# Crop the center of the image
				cropped_im = im.crop((left, top, right, bottom))
				
				#Save the cropped image
				cropped_im.save(os.path.join(dir_path,"".join(["cropped_",image_name])))
			
		elif crp_px is None :
		
		
			"""
			crp_p : Image width and height after performing center crop (proportion)
			"""
			
			new_width , new_height = crp_p[0]*width,crp_p[1]*height
			"""
			The top left coordinates correspond to (x, y) = (left, top), 
			and the bottom right coordinates correspond to (x, y) = (right, bottom). 
			The area to be cropped is left <= x <right and upper <= y <lower,
			and the pixels of x = right andy = lower are not included.
			"""
			left = (width - new_width)/2
			top = (height - new_height)/2
			right = (width + new_width)/2
			bottom = (height + new_height)/2
			
			# Save the list of images which couldn't be cropped due to size mismatches
			if (left < 0) or (top < 0) or (right > width) or (bottom > height):
				images_not_cropped.append(image_name) 
			else:
				# Crop the center of the image
				cropped_im = im.crop((left, top, right, bottom))
				
				#Save the cropped image
				cropped_im.save(os.path.join(dir_path,"".join(["cropped_",image_name])))

		else :
			print("Please Enter valid arguments !!")
	
	print("List of images which didn't get cropped due to size mismatch :")
	print(images_not_cropped)
			
parser = argparse.ArgumentParser(description = """
											dir_path : Path of the folder in which the the images to be cropped are present
											
											Select one of the following to crop the image:
											crp_px : Center square/rectangle crop by user-determined pixels (new_width , new_height)
											crp_p : Centre square/rectangle crop by user-determined percentage 
											""")
parser.add_argument('-dir',
						'--dir_path',
						type = str,
						help = 'Input images folder path')

parser.add_argument('-crp_px',
						'--new_width_height_dimensions_in_pixels',
						type = float,
						nargs= 2 ,
						help = """First value of tuple correspond to the new width(in pixels) after performing center crop
								Second value of tuple correspond to the new height(in pixels) after performing center crop""")

parser.add_argument('-crp_p',
						'--new_width_height_pixels_in_proportion',
						type = float,
						nargs='+',
						help = """First value of tuple correspond to the new width(proportion) after performing center crop
								Second value of tuple correspond to the new height(proportion) after performing center crop""")

args = parser.parse_args()

if __name__ == '__main__':
	image_crop(args.dir_path,args.new_width_height_dimensions_in_pixels,args.new_width_height_pixels_in_proportion)
