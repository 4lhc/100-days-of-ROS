# 100 Days Of ROS 

## I will do ROS development for the next 100 days. 
I will be using ROS C++ client library. My previous attempt with rospy
without the 100 days challenge can be found [here](https://github.com/4lhc/ROS-Learn)

## Goals
 - Improve ROS1 proficiency
 - Learn ROS2
 - Learn to create gazebo plugins
 - Sensor Fusion and SLAM with ROS 



### Day 0:
**Tasks**
 - Setup noetic & foxy
 - Setup neovim for ROS development
    - Tried to get [vim-ros](https://github.com/taketwo/vim-ros/tree/master) working.
    - Autocompletion with neovim and LSP

 **Progress**
  - Autocompletion with neovim 0.5 failed. Will look at other options.

### Day 1:
**Tasks**
  - Refresher: Watch [Programming for Robotics (ROS) Course 1](https://www.youtube.com/watch?v=0BxVPCInS3M)
    - ROS architecture and philosophy
    - ROS master and nodes
    - Topics and messages
    - Console commands
    - Catkin workspace and build system
    - Launch files
    - Gazebo

**Progress**
  - Tried out various console commands
  - Created a launch file to visualize the robot in rviz - [commit](https://github.com/4lhc/AMR_omnibot/commit/e5f286d3e7b4aee20e390257876a56f43ea80b9c)

### Day 2:
**Tasks**
  - Watch [Programming for Robotics (ROS) Course 2](https://www.youtube.com/watch?list=PLE-BQwvVGf8HOvwXPgtDfWoxd4Cc6ghiP&v=jYqDnuxTwK8&feature=youtu.be)

**Progress**
  - Learned
  [ros::init()](http://wiki.ros.org/roscpp/Overview/Initialization%20and%20Shutdown) and its various invocations.
  - Learned about different types of [NodeHandles](http://wiki.ros.org/roscpp/Overview/NodeHandles)
  - Learned  about various [Logging](http://wiki.ros.org/roscpp/Overview/Logging) macros

