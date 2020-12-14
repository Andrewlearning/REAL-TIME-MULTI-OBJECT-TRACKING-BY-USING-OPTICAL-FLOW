#!/bin/bash

# 使用方法
# 运行optical flow的计算方式
# ./runDeepSort.sh optical
#
# 运行普通deepSort + optical flow的计算方式
# ./runDeepSort.sh normal


if [ "$1" == "normal" ]
then
  echo "now run with normal mode"
  echo "========================="
  /Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 object_tracker.py --video ./opticalFlowInput/yifuziyi.mp4  --runmode normal         --output ./outputs/tracker.avi --model yolov4 --dont_show --info

elif [ "$1" == "optical" ]
then
   echo "now run with optical flow mode"
   echo "========================="


   /Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 object_tracker.py --video ./opticalFlowInput/yifuziyi.mp4 --runmode optical        --output ./outputs/tracker.avi --model yolov4 --dont_show --info

elif [ "$1" == "bgextract" ]
then
   echo "now run with background extract mode"
   echo "========================="


   /Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 object_tracker.py --video ./opticalFlowInput/yifuziyi.mp4 --runmode optical        --output ./outputs/tracker.avi --model yolov4 --dont_show --info --additional extract

else
  echo "invalue input, shall run error"
fi
