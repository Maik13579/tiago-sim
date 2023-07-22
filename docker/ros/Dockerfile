ARG ROS_DISTRO=noetic

FROM ros-base-image:$ROS_DISTRO

WORKDIR /root/catkin_ws

RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils \
    libv4l-dev \
    libv4l2rds0 \
    git \
    wget \
    vim \
    locales \
    dpkg \
    ssh \
    curl \
    aptitude \
    g++ \
    gcc \
    openvpn \
    gnupg \
    bash-completion \
    vim-gtk3 \
    nano \
    psmisc \
    ccache \
    gdb \
    qtcreator \
    htop \
    man \
    meld \
    silversearcher-ag \
    terminator \
    tig \
    valgrind \
    iputils-ping \
    ipython3 \
    python-is-python3 \
    python3-scipy \
    python3-wstool \
    python3-networkx \
    python3-pip  \
    python3-vcstool \
    python3-rosinstall \
    python3-catkin-tools \
    ros-noetic-actionlib-tools \
    ros-noetic-moveit-commander \
  && rm -rf /var/lib/apt/lists/* \
  && wget https://raw.githubusercontent.com/pal-robotics/tiago_tutorials/noetic-devel/tiago_public-noetic.rosinstall \
  && vcs import src < tiago_public-noetic.rosinstall

ARG ROSDEP_IGNORE="urdf_test omni_drive_controller orocos_kdl pal_filters libgazebo9-dev pal_usb_utils speed_limit_node camera_calibration_files pal_moveit_plugins pal_startup_msgs pal_local_joint_control pal_pcl_points_throttle_and_filter current_limit_controller hokuyo_node dynamixel_cpp pal_moveit_capabilities pal_pcl dynamic_footprint gravity_compensation_controller pal-orbbec-openni2 pal_loc_measure pal_map_manager ydlidar_ros_driver"

RUN apt-get update && rosdep install --from-paths src --ignore-src -y --rosdistro noetic --skip-keys="${ROSDEP_IGNORE}"

#Get the latest version of the object-map-server
WORKDIR /tmp
RUN git clone --branch feature-grid_map https://github.com/Maik13579/object-map-server.git \
    && mkdir -p /root/python \
    && cp -r object-map-server/python /root/python/object-map-server \
    && cp -r object-map-server/ros/* /root/catkin_ws/src/ \
    && mkdir /maps \
    && cp -r object-map-server/example/robocup_2023 /maps/robocup_2023 \
    && rm -rf object-map-server

#Build python package
WORKDIR /root/python/object-map-server
RUN python3 setup.py bdist_wheel sdist && pip3 install -e .

RUN pip3 install --upgrade scipy

#Build catkin workspace
WORKDIR /root/catkin_ws
RUN bash -c "source /opt/ros/noetic/setup.bash \
    && catkin_make -DCATKIN_ENABLE_TESTING=0 -j $(expr `nproc` / 2) \
    && echo 'source /root/catkin_ws/devel/setup.bash' >> ~/.bashrc"