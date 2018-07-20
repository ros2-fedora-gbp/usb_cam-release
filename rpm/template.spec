Name:           ros-melodic-usb-cam
Version:        0.3.6
Release:        0%{?dist}
Summary:        ROS usb_cam package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/usb_cam
Source0:        %{name}-%{version}.tar.gz

Requires:       ffmpeg-devel
Requires:       ros-melodic-camera-info-manager
Requires:       ros-melodic-image-transport
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
Requires:       v4l-utils
BuildRequires:  ffmpeg-devel
BuildRequires:  ros-melodic-camera-info-manager
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-image-transport
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs

%description
A ROS Driver for V4L USB Cameras

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Jul 20 2018 Russell Toris <rctoris@wpi.edu> - 0.3.6-0
- Autogenerated by Bloom

