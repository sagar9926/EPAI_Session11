import argparse
from PIL import Image
import os
print("#########################################################")
print("######## Welcome to Python Image Processing APP ########")
print("#########################################################")

print("######## Running __main__.py ########")
	
parser = argparse.ArgumentParser(description = """
											dir_path : Path of the folder in which the the images to be cropped are present
											
											Select one of the following to crop the image:
											crp_px : Center square/rectangle crop by user-determined pixels (new_width , new_height)
											crp_p : Centre square/rectangle crop by user-determined percentage 
											""")

parser.add_argument('-t',
						'--Task',
						type = str,
						help = """
						This image processing app performs following 4 tasks :
						-j2p : Convert jpeg image to png
						-p2j : Convert png image to jpeg
						-im_resize : Resizes the image
						-im_c_crop : Center crop the image """)
											
parser.add_argument('-dir',
						'--dir_path',
						type = str,
						help = 'Input images folder path')
parser.add_argument('-im',
						'--image_name',
						type = str,
						help = 'Input jpeg image name')

parser.add_argument('-p',
						'--image_path',
						type = str,
						help = 'Input jpeg image folder path')


parser.add_argument('-crp_px',
						'--new_width_height_dimensions_in_pixels',
						type = float,
						nargs= 2 ,
						help = """First value of tuple correspond to the new width(in pixels) after performing center crop
								Second value of tuple correspond to the new height(in pixels) after performing center crop""")

parser.add_argument('-crp_p',
						'--new_width_height_pixels_in_proportion',
						type = float,
						help = """First value of tuple correspond to the new width(proportion) after performing center crop
								Second value of tuple correspond to the new height(proportion) after performing center crop""")
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


if __name__ == "__main__":	  

	if args.Task == "j2p": 
		from J2P import jpeg_to_png 
		print("Converting Image from jpeg to png")
		jpeg_to_png(args.image_name,args.image_path)
		print("Finished Conversion!")
	  
	if args.Task == "p2j": 
		from P2J import png_to_jpeg 
		print("Converting Image from png to jpeg")
		png_to_jpeg(args.image_name,args.image_path)
		print("Finished Conversion!")
	  
	if args.Task == "resize_image":
		from image_resizer import image_resize
		print("Resizing !!")
		image_resize(args.dir_path,args.image_resize_proportion,args.image_width_resize_proportion,args.image_height_resize_proportion)
		print("Finished Resizing!")
		
	if args.Task == "center_crop":
		from image_cropper import image_crop
		print("Cropping !!")
		image_crop(args.dir_path,args.new_width_height_dimensions_in_pixels,args.new_width_height_pixels_in_proportion)
		print("Finished Cropping!")
		
	

