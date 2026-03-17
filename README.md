# TB3_Lane_Tracking

TurtleBot3 Burger를 이용한 OpenCV 기반 실시간 차선 인식 및 주행 제어 프로젝트입니다.

## 1. 프로젝트 결과물
| 원본 데이터 및 결과 | Bird's-eye View & Histogram |
| :---: | :---: |
| ![curve](https://github.com/user-attachments/assets/841c61af-f182-4886-aebc-8ea24dfed1f4) | ![histogram](https://github.com/user-attachments/assets/68bce0c8-cbee-453d-950e-848339426d25) |

---

## 2. 프로젝트 개요 (Overview)
* **목적:** TurtleBot3 Burger의 카메라 데이터를 활용하여 실시간으로 차선을 인식하고 추적하는 자율 주행 알고리즘 구현.
* **환경:** Ubuntu 22.04, ROS 2 Humble, OpenCV 4.x.

## 3. 알고리즘 설명 (Algorithm)
* **IPM (Inverse Perspective Mapping):** 원근 변환을 통해 카메라 이미지를 상공에서 내려다보는 듯한 Bird's-eye View로 변환합니다.
* **Histogram-based Lane Detection:** 변환된 이미지의 하단 픽셀 밀도를 분석하여 차선의 시작점(Left/Right Base)을 검색합니다.
* **Sliding Window:** 검색된 시작점부터 윈도우를 쌓아 올리며 차선의 전체 곡률과 중심점을 계산합니다.
* **PID Control:** 계산된 차선 중앙값과 로봇 중심값의 오차(Error)를 바탕으로 로봇의 선속도 및 각속도(`cmd_vel`)를 제어합니다.
* **Centerline Detection):** 슬라이딩 윈도우의 연속성 단절(Discontinuity)을 감지하여 점선 형태의 중앙선을 실선과 구분하고, 차선의 소실 여부나 유효성을 판단합니다.

---

## 4. 주의사항 및 한계점 (Limitations)
> **[중요] 특정 색상 의존성**
> * 현재 알고리즘은 **검은색 차선(High Contrast Black)** 인식에 최적화되어 있습니다.
> * 그레이스케일 및 특정 임계값(Thresholding)을 사용하므로, 실제 도로의 흰색이나 노란색 차선을 인식하려면 **HSV 색상 공간 변환 및 필터링 조건 수정**이 필요합니다.

---

## 5. 실행 방법 (Usage)

### 패키지 빌드
```bash
cd ~/bot_ws_pi
colcon build --symlink-install --packages-select bot_pkg_pi
source install/setup.bash
# 터미널 1: 로봇 브링업
ros2 launch turtlebot3_bringup robot.launch.py

# 터미널 2: 차선 인식 노드 실행
ros2 run bot_pkg_pi [실행파일명]
