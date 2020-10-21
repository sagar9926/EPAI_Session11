# Created By : Sagar Agrawal

# EPAI : Session 11 - Modules

## This repository have following Image processing  modules :

### 1. J2P.py

#### Description : 

This module takes .jpeg image as input , along with the directory path of the image and converts it into image with extension .png. The image is stored in a new directory named __Converted_to_jpg__

#### Arguments :
Following are the input arguments for this module :

-im / --image_name : Input jpeg image name

-p / --image_path : Input jpeg image folder path


#### Usage : 

To use this module run the following command in terminal :
```
python J2P.py -im image1.jpg -p ./images
```

### 2. P2J.py

#### Description : 

This module takes .png image as input , along with the directory path of the image and converts it into image with extension .jpeg. The image is stored in a new directory named __Converted_to_jpg__

#### Arguments :
Following are the input arguments for this module :

-im / --image_name : Input jpeg image name

-p / --image_path : Input jpeg image folder path


#### Usage : 

To use this module run the following command in terminal :
```
python P2J.py -im image1.png -p ./images
```

### 3. image_cropper,py

#### Description :

This module takes image as input (both .png/.jpg) and does a center crop on the image based on the pixel values for height and width or the percentage amount provided by the user.

#### Arguments :
Following are the input arguments for this module :

-dir / --dir_path : Path of the folder in which the the images to be cropped are present
-crp_px / --new_width_height_dimensions_in_pixels : Center square/rectangle crop by user-determined pixels (new_width , new_height)
-crp_p / --new_width_height_pixels_in_proportion : Centre square/rectangle crop by user-determined percentage 

#### Usage : 

##### Crop by user provided height and width pixel values :
```
python image_cropper.py -dir ".\images" -crp_px 100 200
```

##### Crop by user provided percentage values :
```
python image_cropper.py -dir ".\images" -crp_p 0.5
```
