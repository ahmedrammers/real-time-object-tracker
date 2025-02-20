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
   git clone https://github.com/yourusername/real-time-object-tracker.git
   cd real-time-object-tracker
   ```

2. Run the script:
   ```sh
   python tracker.py
   ```

3. Select an object using the bounding box that appears.
4. The system will track the object in real-time.
5. Press `q` to exit the program.

## Implementation Details
- **OpenCV Tracking Algorithm**: The system uses `TrackerCSRT_create()` by default, which provides robust tracking performance. Other tracking algorithms like KCF, MIL, and MOSSE can be used by modifying the script.
- **Bounding Box Selection**: The user selects an object in the first frame, and the tracker initializes with the selected region.
- **Real-Time Updates**: The tracker continuously updates the bounding box coordinates and overlays them on the video feed.

## Demo
A recorded demo showcasing the tracking performance can be found [here](#) (Replace with actual link).

## License
This project is licensed under the MIT License.

## Author
[Your Name] - [Your GitHub Profile](https://github.com/yourusername)

## Contributions
Contributions are welcome! Feel free to submit a pull request or open an issue.

