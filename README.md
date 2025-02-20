# Real-Time Object Tracker

## Overview
This project is a real-time object tracking system that allows users to select an object from a webcam feed and track it as it moves. The system leverages OpenCV's tracking algorithms for efficient and accurate tracking.

## Features
- Allows user to select an object in the first frame using a bounding box.
- Tracks the selected object in real time as it moves.
- Displays the tracking results in a live video feed.
- Supports multiple OpenCV tracking algorithms.

## Installation

### Prerequisites
Ensure you have Python installed on your system. You can download it from [Python.org](https://www.python.org/).

### Install Dependencies
Run the following command to install the required libraries:
```sh
pip install opencv-python numpy
```

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/ahmedrammers/real-time-object-tracker.git
   cd real-time-object-tracker
   ```

2. Run the script:
   ```sh
   python object_track.py
   ```

3. Select an object using the bounding box that appears.
4. The system will track the object in real-time.
5. Press `q` to exit the program.

## Implementation Details
- **OpenCV Tracking Algorithm**: The system uses `TrackerCSRT_create()` by default, which provides robust tracking performance. Other tracking algorithms like KCF, MIL, and MOSSE can be used by modifying the script.
- **Bounding Box Selection**: The user selects an object in the first frame, and the tracker initializes with the selected region.
- **Real-Time Updates**: The tracker continuously updates the bounding box coordinates and overlays them on the video feed.

## Demo
A recorded demo showcasing the tracking performance can be found [here](https://drive.google.com/file/d/1c-48nCiRIDzFUVcE6s39WcCmwY9jxtGP/view?usp=sharing).

