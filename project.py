#!/usr/bin/env python3

import jetson_inference
import jetson_utils

# import argparse

net = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson_utils.videoSource("/dev/video0")      # '/dev/video0' for V4L2
display = jetson_utils.videoOutput() # 'my_video.mp4' for file

while display.IsStreaming():
	img = camera.Capture()
	detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))