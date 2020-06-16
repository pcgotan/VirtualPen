# VirtualPen

## Background

Drawing on the screen by waving a virtual pen in the air without any special hardware using computer vision.

Color masking is used to get a binary mark of target colored Object ( as a pen) then used contour detection to detect and track the location of that pen all over the screen.

Once done with that it’s just a matter of connecting the dots. Draw a line using the x,y coordinates of pen’s previous location (location in the previous frame) with the new x,y points (x,y points in new frame) and that’s it, Virtual pen is ready to serve.

## Steps

-   Finding the color range of the target object and save it
-   Morphological operations for reducing the noise in the video
-   Tracking the colored object with contour detection
-   Wiping functionality
-   Eraser functionality

## Files

```
-python3 select.py
```

This file will let you select the object to be pen. It is basically a range of HSV in order to detect the color of the object by appling binary masking. After tuning, by pressing c, it will save a range of HSV in a file.  
Later this file will be used to load the pen object.

```
python draw.py
```

This is the main file. It creates a canavs on which drawing can be done. Erase functionality is also added.

```
betterCam.py
```

This file is for using mobile camera as a webcam in opencv. It provides a better quality and frame rate.

Download a Android app `IP Webcam` it provides a IP address for camera instance. It will be needed in that file.
