
# ROS 1, 2 and Coppeliasim Practice

## Ubuntu 18.04.6

### ROS1 : ros-melodic
### ROS2 : ros-dashing
* catkin build comands and both Python & C++
* colcon build comands and both Python & C++

### Coppeliasim 4.0.0 Educational
![cupGripping](https://user-images.githubusercontent.com/68832065/148175617-8be1b254-32cc-44bf-af6b-98055048882e.gif)

## Simpe ROS version conversion
### copy and paste below at the end of your .bashrc
### change modes by selecting ROS_V = 1 or 2 on /.bashrc

  ROS_V=1 # Select ROS Version 1 or 2

  # ROS_V값이 1이면, ROS1 관련 환경변수/Workspace/Shortcut 활성화
  if [ $ROS_V -eq 1 ]; then
    # 사용자 지정 Shortcut. 터미널에 cw, cs, cm 등을 입력하면 해당 명령이 실행됨.
    alias cw='cd ~/catkin_ws'
    alias cs='cd ~/catkin_ws/src'
    alias cm='cd ~/catkin_ws && catkin_make'

    # root directory의 ros1 Workspace와 home directory에 있는 catkin_ws를 컴퓨터가 인식하도록 함.
    source /opt/ros/melodic/setup.bash
    source ~/catkin_ws/devel/setup.bash

    # ROS1 IP 세팅 관련 환경변수 설정
    export ROS_MASTER_URI=http://localhost:11311
    export ROS_HOSTNAME=localhost

  # ROS_V값이 2이면, ROS2 관련 환경변수/Workspace/Shortcut 활성화
  elif [ $ROS_V -eq 2 ]; then
    # root directory의 ros2 Workspace와 home directory에 있는 robot_ws를 컴퓨터가 인식하도록 함.
    source /opt/ros/dashing/setup.bash
    source ~/robot_ws/install/local_setup.bash

    export ROS_DOMAIN_ID=7

    # 사용자 지정 Shortcut
    alias cw='cd ~/robot_ws'
    alias cs='cd ~/robot_ws/src'
    alias cb='cd ~/robot_ws && colcon build --symlink-install'
    alias cbs='colcon build --symlink-install'
    alias cbp='colcon build --symlink-install --packages-select'
    alias cbu='colcon build --symlink-install --packages-up-to'

    alias rt='ros2 topic list'
    alias re='ros2 topic echo'
    alias rn='ros2 node list'

    alias af='ament_flake8'
    alias ac='ament_cpplint'

    alias testpub='ros2 run demo_nodes_cpp talker'
    alias testsub='ros2 run demo_nodes_cpp listener'
    alias testpubimg='ros2 run image_tools cam2image'
    alias testsubimg='ros2 run image_tools showimage'
  fi


## Reference
* [1] https://cafe.naver.com/openrt/24065
