import pytest
import random
import string
import os
import inspect
import re
import math
import subprocess

# Test 1
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"
# Test 2
def test_readme_contents():
    readme = open("README.md", "r",encoding = "utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"
#Test 3
def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding = "utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

#Test 4
def test_J2P():
	#Running the command line argument to conver jpeg image to png
    os.system(r'python3 J2P.py -im img1.jpg -p ".\images"')
	
	#Checking wheather output png file got created or not 
    converted_to_png = os.listdir(r'.\Converted_to_png')
    assert 'img1_jpg_to_png.png' in converted_to_png , "There is some error with your jpeg to png conversion"

#Test 5
def test_J2P_check_valid_directory() :
    with pytest.raises(ValueError):
        try : 
            subprocess.run(r'python3 J2P.py -im img1.jpg -p "C:\Users\Fake_Directory\Desktop\Assignment11\images"',check = True)
        except: 
            raise ValueError
#Test 6
def test_J2P_check_valid_jpg() :
    with pytest.raises(ValueError):
        try : 
            subprocess.run(r'python3 J2P.py -im img1.jpg -p r"python J2P.py -im img1.abc -p ".\images"',check = True)
        except: 
            raise ValueError


#Test 7
def test_P2J():
	#Running the command line argument to conver jpeg image to png
    os.system(r'python3 P2J.py -im img1.png -p ".\images"')
    #Checking wheather output png file got created or not 
    converted_to_jpg = os.listdir(r'.\Converted_to_jpg')
    assert 'img1_png_to_jpg.jpeg' in converted_to_jpg , "There is some error with your png to jpeg conversion"

#Test 8
def test_P2J_check_valid_directory() :
    with pytest.raises(ValueError):
        try : 
            subprocess.run(r'python3 P2J.py -im img1.png -p "C:\Users\Fake_Directory\Desktop\Assignment11\images"',check = True)
        except: 
            raise ValueError

#Test 9
def test_P2J_check_valid_jpg() :
    with pytest.raises(ValueError):
        try : 
            subprocess.run(r'python3 P2J.py -im img1.abc -p ".\images"',check = True)
        except: 
            raise ValueError

#Test 10
def test_image_resizer_directory_creation():
	os.system(r'python3 image_resizer.py -dir ".\images" -res_p 0.01')
	assert os.path.isdir(r'./Resized_images') ,"Resized images directory not found"
    
		
#Test 11
def test_image_resizer_res_p():
	os.system(r'python3 image_resizer.py -dir ".\images" -res_p 0.01')
	assert os.path.isdir(r'./Resized_images') ,"Resized images directory not found"
	assert len(os.listdir(r'./Resized_images')) != 0 , "Error!!. None of the images were resized"

#Test 12
def test_image_resizer_res_w():
	os.system(r'python3 image_resizer.py -dir ".\images" -res_w 0.01')
	assert os.path.isdir(r'./Resized_images') ,"Resized images directory not found"
	assert len(os.listdir(r'./Resized_images')) != 0 , "Error!!. None of the images were resized"

#Test 13
def test_image_resizer_res_h():
	os.system(r'python3 image_resizer.py -dir ".\images" -res_h 0.01')
	assert os.path.isdir(r'./Resized_images') ,"Resized images directory not found"
	assert len(os.listdir(r'./Resized_images')) != 0 , "Error!!. None of the images were resized"
	
#Test 14
def test_image_resizer_res_w_res_h():
	os.system(r'python3 image_resizer.py -dir ".\images" ,-res_w 0.2 , -res_h 0.01')
	assert os.path.isdir(r'./Resized_images') ,"Resized images directory not found"
	assert len(os.listdir(r'./Resized_images')) != 0 , "Error!!. None of the images were resized"

#Test 15
def test_image_resizer_check_valid_directory() :
    with pytest.raises(ValueError):
        try : 
            subprocess.run(r'python3 image_resizer.py -dir "C:\Users\Faked_Directory\Desktop\Assignment11\images" -res_p 0.01',check = True)
        except: 
            raise ValueError
#Test 16
def test_image_cropper_check_valid_directory() :
    with pytest.raises(ValueError):
        try : 
            subprocess.run(r'python3 image_cropper.py -dir "C:\Users\Faked_Directory\Assignment11\images" -crp_px 100 200',check = True)
        except: 
            raise ValueError


#Test 17 
def test_image_cropper_directory_creation_cropped():
	os.system(r'python3 image_cropper.py -dir ".\images" -crp_px 100 200')
	assert os.path.isdir(r'./Cropped') ,"Cropped images directory not found"
	
#Test 18
def test_image_cropper_directory_creation_uncropped():
	os.system(r'python3 image_cropper.py -dir ".\images" -crp_px 100 200')
	assert os.path.isdir(r'./Uncropped') ,"Uncropped images directory not found"

	
#Test 19 
def test_image_cropper_crp_p():
	os.system(r'python3 image_cropper.py -dir ".\images" -crp_p 0.5')
	len(os.listdir(r'./Cropped')) + len(os.listdir(r'./Uncropped')) == len(os.listdir(r'./images')),"Images are not cropped properly"

#Test 20
def test_image_cropper_crp_px():
	os.system(r'python3 image_cropper.py -dir ".\images" -crp_px 100 200')
	len(os.listdir(r'./Cropped')) + len(os.listdir(r'./Uncropped')) == len(os.listdir(r'./images')),"Images are not cropped properly"

            
