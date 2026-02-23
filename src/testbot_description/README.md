# TurtleBot2 + YDLiDAR + RGB Camera 모델 설정 완료 ✅

## 📂 디렉토리 구조
```
testbot_description/
├── CMakeLists.txt
├── package.xml
├── urdf/
│   ├── testbot.urdf.xacro          # 기본 로봇 모델
│   └── testbot_gazebo.urdf.xacro   # Gazebo 시뮬레이션 플러그인
├── launch/
│   ├── display.launch               # RViz 시각화
│   ├── testbot.launch               # 기본 launch 파일
│   └── gazebo.launch                # Gazebo 시뮬레이션
├── rviz/
│   └── testbot.rviz                 # RViz 설정
├── worlds/
│   └── testbot_world.world          # Gazebo World
├── scripts/
│   └── tf_broadcaster.py            # TF Broadcaster
└── meshes/                          # (선택사항) 메시 파일
```

## 🔧 로봇 구성

### 하드웨어
- **Base**: TurtleBot2 (원형, 0.33m 지름, 0.11m 높이)
- **Wheels**: 2개의 주행 바퀴 (continuous joints)
- **Caster**: 1개의 캐스터 휠
- **LiDAR**: YDLiDAR (laser_link, 상단 중앙)
- **Camera**: RGB 카메라 (camera_link, 전방)
- **IMU**: 관성 센서 (imu_link)
- **Top Plate**: 상판

### 프레임 구조
```
odom
 └─ base_link
    ├─ wheel_left_link
    ├─ wheel_right_link
    ├─ caster_wheel_link
    ├─ top_plate_link
    │  ├─ laser_link
    │  ├─ camera_link
    │  │  └─ camera_optical_frame
    │  └─ (IMU는 base_link에 연결)
    └─ imu_link
```

## 🚀 실행 방법

### 1️⃣ RViz 시각화
```bash
cd ~/test_ws
source devel/setup.bash
roslaunch testbot_description display.launch
```

**RViz에서 확인:**
- Fixed Frame: `base_link`
- Display 탭에서 RobotModel 활성화
- 로봇 모델과 센서 시각화 확인

### 2️⃣ Gazebo 시뮬레이션
```bash
cd ~/test_ws
source devel/setup.bash
roslaunch testbot_description gazebo.launch
```

**Gazebo에서 확인:**
- 로봇이 자동으로 스폰됨
- 벽으로 둘러싼 환경 로드
- 카메라, LiDAR, IMU 센서 활성

### 3️⃣ 로봇 제어
```bash
# 새 터미널에서
roslaunch testbot_description gazebo.launch gui:=false  # GUI 없이 실행

# 또 다른 터미널에서 로봇 움직이기
rostopic pub -1 /cmd_vel geometry_msgs/Twist -- '[0.5, 0, 0]' '[0, 0, 0.2]'
```

### 4️⃣ TF 확인
```bash
rosrun tf view_frames  # TF 트리 다이어그램 생성
rosrun rqt_tf_tree rqt_tf_tree  # GUI로 TF 트리 보기
```

### 5️⃣ 센서 확인
```bash
# LiDAR 스캔 확인
rostopic echo /scan

# 카메라 이미지 확인
rosrun image_view image_view image:=/camera/image_raw

# IMU 데이터 확인
rostopic echo /imu
```

## 📊 사용 가능한 토픽

| 토픽 | 타입 | 설명 |
|------|------|------|
| `/cmd_vel` | Twist | 로봇 속도 명령 |
| `/odom` | Odometry | 로봇 위치 정보 |
| `/scan` | LaserScan | LiDAR 스캔 데이터 |
| `/camera/image_raw` | Image | RGB 카메라 영상 |
| `/camera/camera_info` | CameraInfo | 카메라 보정 정보 |
| `/imu` | Imu | IMU 센서 데이터 |
| `/tf` | TF | 좌표계 변환 |

## 🎯 Gazebo 플러그인

### 활성화된 플러그인
1. **Differential Drive Controller**: `cmd_vel` 토픽으로 바퀴 제어
2. **Laser Scanner Plugin**: `/scan` 토픽으로 LiDAR 데이터 발행
3. **Camera Plugin**: `/camera/image_raw`, `/camera/camera_info` 토픽 발행
4. **IMU Sensor Plugin**: `/imu` 토픽 발행

## ✏️ 커스터마이징

### URDF 수정
- [testbot.urdf.xacro](urdf/testbot.urdf.xacro): 로봇 구조 수정
- [testbot_gazebo.urdf.xacro](urdf/testbot_gazebo.urdf.xacro): Gazebo 물리 설정

### launch 파일 커스터마이징
- [display.launch](launch/display.launch): RViz 설정 변경
- [gazebo.launch](launch/gazebo.launch): Gazebo 월드 변경

### Python 스크립트 수정
- [tf_broadcaster.py](scripts/tf_broadcaster.py): TF 발행 로직 수정

## 🔍 문제 해결

### "resource not found" 에러
- `devel/setup.bash` 소싱했는지 확인
- `catkin_make` 다시 실행

### Gazebo가 느린 경우
- `gazebo.launch`에서 `paused:=true` 옵션 추가
- GPU 가속 확인

### RViz에서 로봇이 안 보이는 경우
- Fixed Frame을 `base_link`로 설정
- TF Prefix 확인 (비어있어야 함)

## 📚 참고자료
- [ROS URDF 튜토리얼](http://wiki.ros.org/urdf)
- [Gazebo 튜토리얼](http://gazebosim.org/tutorials)
- [ROS TF 설명서](http://wiki.ros.org/tf)
