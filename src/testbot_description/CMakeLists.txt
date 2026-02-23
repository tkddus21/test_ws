cmake_minimum_required(VERSION 3.0.2)
project(testbot_description)

find_package(catkin REQUIRED
  urdf
  xacro
  robot_state_publisher
  joint_state_publisher
  tf
  rviz
  gazebo_ros
  gazebo_plugins
)

catkin_package()

# Install directories
install(DIRECTORY urdf launch rviz worlds scripts
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

# Install python scripts
catkin_install_python(PROGRAMS scripts/tf_broadcaster.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
