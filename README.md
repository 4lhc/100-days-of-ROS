# \#100DaysOfROS

---

## Progress
<p align="center">
 <a href='https://github.com/4lhc/100-days-of-ROS/blob/main/img/gen_streak.py'>
 <img width="600" src="img/streak.png">
 </a>
</p>

---

## Goals
 - Improve ROS1 and `roscpp` proficiency.
 - Learn ROS2.
 - Learn to create gazebo plugins.
 - Sensor Fusion and SLAM with ROS.
 - Build a ROS enabled AMR



### Day 0:
**Tasks**
 - Setup noetic & foxy
 - Setup neovim for ROS development
    - Tried to get [vim-ros](https://github.com/taketwo/vim-ros/tree/master) working.
    - Autocompletion with neovim and LSP

 **Progress**
  - Autocompletion with neovim 0.5 failed. Will look at other options.

---
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
  - Tried out various console commands.
  - Created a launch file to visualize the robot in rviz - [commit](https://github.com/4lhc/AMR_omnibot/commit/e5f286d3e7b4aee20e390257876a56f43ea80b9c)

---
### Day 2:
**Tasks**
  - Watch [Programming for Robotics (ROS) Course 2](https://www.youtube.com/watch?list=PLE-BQwvVGf8HOvwXPgtDfWoxd4Cc6ghiP&v=jYqDnuxTwK8&feature=youtu.be)
    - Initialization of the nodes
    - NodeHandles

**Progress**
  - Learned
  [`ros::init()`](http://wiki.ros.org/roscpp/Overview/Initialization%20and%20Shutdown) and its various invocations.
  - Learned about different types of [`NodeHandles`](http://wiki.ros.org/roscpp/Overview/NodeHandles)
  - Learned  about various [Logging](http://wiki.ros.org/roscpp/Overview/Logging) macros
  - [commit](https://github.com/4lhc/ROS-Learn/commit/de332e37361db77c22a53e2b7f0a70b36157ac3c)

--- 
### Day 3:
**Tasks**
  - Watch [Programming for Robotics (ROS) Course 2](https://www.youtube.com/watch?list=PLE-BQwvVGf8HOvwXPgtDfWoxd4Cc6ghiP&v=jYqDnuxTwK8&feature=youtu.be)
    - Subscribers and Publishers
    - ROS parameter server.

**Progress**
  - Edit `CmakeLists.txt` to create multiple nodes.
  - Created subscriber and publisher [nodes](https://github.com/4lhc/ROS-Learn/tree/master/noetic_test_ws/src/test_pkg_1/src)
  - Learned [`rosparam`](http://wiki.ros.org/roscpp/Overview/Parameter%20Server) syntax.
  - Misc:
    - Setup ROS Qt Creator
    [plug-in](https://ros-qtc-plugin.readthedocs.io/en/latest/)
    - Fixed neovim LSP completion.
    - Got [vim-ros](https://github.com/taketwo/vim-ros/tree/master) working in noetic

---
### Day 4:
**Tasks**
  - Watch [Programming for Robotics (ROS) Course 3](https://youtu.be/_GgHFuib_LU?list=PLE-BQwvVGf8HOvwXPgtDfWoxd4Cc6ghiP&t=696)
    - [URDF](http://wiki.ros.org/urdf/Tutorials/Building%20a%20Visual%20Robot%20Model%20with%20URDF%20from%20Scratch)

**Progress**
  - Created a basic urdf (visual only) for 3-wheeled [omnibot](https://github.com/4lhc/AMR_omnibot/blob/master/src/omnibot_description/urdf/omnibot.urdf). 

---
### Day 5:
**Tasks**
  - [Xacro](http://wiki.ros.org/xacro)

**Progress**
  - Created macros for wheel link and joints - [omnibot](https://github.com/4lhc/AMR_omnibot/blob/master/src/omnibot_description/urdf/omnibot.urdf).

---
### Day 6:
**Tasks**
  - Watch [Programming for Robotics (ROS) Course 3](https://youtu.be/_GgHFuib_LU?list=PLE-BQwvVGf8HOvwXPgtDfWoxd4Cc6ghiP)
    -[TF](https://wiki.ros.org/tf2)

**Progress**
  - Tried out different cmd line `tf` tools.
    - `tf_monitor`, `tf_echo` and `view_frames`
  - [Quaternion Basics](https://wiki.ros.org/tf2/Tutorials/Quaternions)
    - Tested different quaternion operations -- Creating quaternion from rpy,
    rotations and conversion between `tf2::Quaternion` and `geometry_msgs::Quaternion`
  - Started writing a `tf2_static_broadcaster`
  - [Today's Work](https://github.com/4lhc/ROS-Learn/tree/master/noetic_test_ws/src/tf_pkg)

---
### Day 7:
**Tasks**
  - tf2

**Progress**
  - Wrote tf2 broadcaster.
    - [`tf2_ros::TransformBroadcaster`](http://docs.ros.org/en/jade/api/tf2_ros/html/c++/classtf2__ros_1_1TransformBroadcaster.html)
    - Creating callback functions for `/odom` topic
    - [Today's Work](https://github.com/4lhc/ROS-Learn/tree/master/noetic_test_ws/src/tf_pkg)

---
### Day 8:
**Tasks**
  - Today I planned to finish adding lidar and meshes to the robot urdf. But
  spend too much time on freecad trying to fix the origin of an imported wheels. 

**Progress**
  - Created meshes for
  [`omnibot_description`](https://github.com/4lhc/AMR_omnibot/tree/master/src/omnibot_description/meshes) urdf geometry.

---
### Day 9:
**Tasks**
  - Start work on CAD model 

**Progress**
  - Created base and started assembly.
  - Fix origin errors with meshes

  <p align="left">
        <img width="200" src="img/freecad_omnibot.png">
  </p>

---
### Day 10:
**Tasks**
  -  Watch [Programming for Robotics (ROS) Course 4](https://www.youtube.com/watch?v=feXC7aQrkeM&list=PLE-BQwvVGf8HOvwXPgtDfWoxd4Cc6ghiP&index=4)
    - Create a service file
    - Write a service client in `roscpp`

**Progress**
  - Created a service client and service message. 
  - Had trouble with empty service request [TODO]
  - [Today's Work](https://github.com/4lhc/AMR_omnibot/tree/master/src/omnibot_teleop/src)

**Note**
  - Designing the omnibot model requires a sizeable chunk of time,
  which I'm lacking this week. Hence, I decided to resume learning `roscpp` and
  put the robot design on hold for the week. The current CAD model is for
  visualization only and it is not what something I want it to be. 

---
### Day 11:
**Tasks**
  - Continue with [ROS
  Services](http://wiki.ros.org/roscpp/Overview/Services#Service_definitions.2C_request_messages_and_response_messages)
    - Write a service server in `roscpp`

**Progress**
  - Created a service server.
  - Learned to create persistent connections to services
  - Different callback types that can be used for the ServiceServer: Functions, Class
  Methods and Functors
  - Create headers to pass meta information about the client.
  - [Today's Work](https://github.com/4lhc/AMR_omnibot/tree/master/src/omnibot_teleop/src)

---
### Day 12:
**Tasks**
  - Learn [Timers](http://wiki.ros.org/roscpp/Overview/Timers)

**Progress**
  - Created a Timer callbacks of different flavours - Function, class methods.
  - Explored various members of `struct TimerEvent` - `last_expected`,
  `last_real` etc
  - [Today's Work](https://github.com/4lhc/ROS-Learn/blob/master/noetic_test_ws/src/test_pkg_1/src/test_pkg_1_timer_node.cpp)

---
### Day 13:
**Tasks**
  - Learn [Clock](http://wiki.ros.org/Clock) &
  [Time](http://wiki.ros.org/roscpp/Overview/Time)
  - Learn [Callbacks & Spinning](http://wiki.ros.org/roscpp/Overview/Callbacks%20and%20Spinning)

**Progress**
  - Learned about `ros::Time`, `ros::Duration` and `ros::Rate` examples.
  - Use `WallTime`, `WallDuration` and `WallRate` when wall-clock is needed.
  - Use `Timers` over `Rate`.
  - `Rate` tries to maintain rate for a loop.
  - Learned about single threaded spinners and experimented with `ros::spin()`
  and `ros::spinOnce()`
  - Found couple of good sources to learn more about ROS callbacks and spinners
    - [Do Timers run in different threads?](https://answers.ros.org/question/367223/do-timers-run-in-different-threads-roscpp/?answer=367455#post-id-367455)
    - [ROS Spinning, Threading,
    Queuing by Kohei Otsuka](https://levelup.gitconnected.com/ros-spinning-threading-queuing-aac9c0a793f)

