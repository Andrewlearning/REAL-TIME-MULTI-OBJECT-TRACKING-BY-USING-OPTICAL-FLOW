##REAL-TIME MULTI-OBJECT TRACKING BY USING OPTICAL FLOW

**2020Fall CMPUT414 Group9**  
**Github link:** https://github.com/Andrewlearning/yolov4-deepsort <br>
<br>

# Announcement
Most of the code for this project comes from: https://github.com/theAIGuysCode/yolov4-deepsort. 
Only for personal learning, not for commercialization.
Please contact me if there is any infringement.
<br>

# Environment Config
Please refer the requirements.txt in the root path.
<br>

##How to run the code
Runing the algorithm:** YOLO + DeepSORT**  
Command line:
> ./runDeepSort.sh normal
<br>

Runing the algorithm: **YOLO + optical flow + DeepSORT**
Command line:  
> ./runDeepSort.sh optical
<br>

Runing the algorithm: **YOLO + background subtraction + optical flow + DeepSORT**  
Command line:
> ./runDeepSort.sh bgextract
<br>

#Mainly addtion and change

###runDeepSort.sh
Shell script file, the user can run the code by running the pre-written command in the terminal.

###Rectangle.py
A class used to store bounding box information, which contains some basic position information of the bounding box and feature point information. It also contains functions that can use optical flow to update the coordinates of the bounding box.

###object_tracker.py
The main logic program of the algorithm. It decides to choose different algorithms through the parameters passed in when running the program. At the same time, there is a function I wrote to calculate IoU and match the bounding box.

###ground_truth.py
The ground truth data of yifuziyi.mp4 was recorded, and all data were collected by manual measurement. Use in object_tracker.py.

###opticalFlowInput/yifuziyi.mp4
A video of about 10 seconds, in order to ensure that the output of the algorithm can be obtained quickly, we only use the first 80 frames in the code

###output/tracker.avi
The output video after run the algorithm.
<br>


#Discription of funtion

###Rectangle.py
#### Class variable
```
#The location information of the bounding box in current frame
self.left
self.top
self.right
self.bottom
self.height
self.width
# Check this bounding box is new
self.ready = False
# The feature points in current bounding box
self.features = None
```

####update_right_bottom()
Update_right_bottom.  

####set_lower_right(x, y)
Set lower right corner coodinate for bounding box.   

####set_height(height)
Set height for bounding box.   

####set_width(width)
Set width for bounding box.   

####find_features(current)
Find the feature points for current bounding box

####update_features(prev, current)
Update the features points for bounding box according to last frame and current frame.  

####is_ready()
Return self.ready

####get_xywh()
Return the (left,top,width,height) data of bounding box 

-------------------------------------------------------------------------------

###object_tracker.py

####Important Flag
**runmode**: Select the different algorithm to run.
- normal: run ** YOLO + DeepSORT** 
- optical: run  **YOLO + optical flow + DeepSORT**

**additional**: Do background extract or not.
- subtract: run  **YOLO + background subtraction + optical flow + DeepSORT**

####Important variable
```
# Current frame number
frame_num = 0

# The class list which contain all the bounding box information
rectangles = []

#Previous frame, store it to use in optical flow
prev = None

# Record the processing speed for each frame, unit: fps
timeRecorder = []

# Record the IoU value for each frame
iou = []
```

####isMatch(current, trueBox)
Check current bounding box can match the ground truth bounding box.

####calIou(curBox, trueBox)
Calulate IoU according to current bounding box and ground truth bounding box.
<br>
















