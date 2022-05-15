# Smart Trash Can data collection system for Drone
드론의 스마트 쓰레기통 데이터 수집 시스템<br>
- Team : DoD<br>
- Contributors : 조우형, 김준영, 박중후, 유예린<br>

## 🗑 Smart Trash Can
- **Spec**
  - **Hardware** - Raspberry Pi 4 8GB
  - **OS** - Raspbian OS
  - **Sensor 1** - 초음파 센서 HC-SR04
  - **Sensor 2** - 무게 센서 HX-711
  - **Sensor 3** - 서보 모터 SG-90

회로도<br>
알고리즘 도표<br>
작동 자료<br>

## 🚁 Drone
- **Spec**
  - **FC** - AutoPilot Pixhawk 4
  - **Server** - Raspberry Pi 3 B+
  - **Server OS** - Linux-5.10.103 with debian-10.12
  - **LTE Module** - SixFab EG25-G (Global)
  - **GCS OS** - Ubuntu 18.04.5 on Windows

- **Architecture**
![Architecture](/docs/img/drone/architecture_basic.PNG)

- **Progress**
<br>
<img align="left" width="350" height="250" src="/docs/img/drone/connect_LTE_Module.jpg">
<br><br>
1. LTE Module 및 안테나 연결<br><br>
2. Sixfab 모듈 펌웨어 설치<br><br>
3. eth0, wlan0 해제 후 셀룰러 모드 동작 확인<br><br>
<br clear="left"/><br>

***
<br>
<img align="left" src="docs/img/drone/port_forwading.png">
1. 5001 포트포워딩 설정<br><br>
2. 드론은 5001 포트를 통해 GCS와 통신한다.<br><br>
<br clear="left"/><br>

```
pi@drone:~ $ sudo apt update
pi@drone:~ $ sudo apt upgrade
pi@drone:~ $ sudo pip install future pyserial dronekit MAVProxy
pi@drone:~ $ sudo apt install screen python-wxgtk4.0 python-lxml
```
```
pi@drone:~ $ mavproxy.py --master /dev/ttyACM0 --out [routerIP]:5001
```

<img align="center" src="docs/img/drone/MavProxy_GCS_UDP_Connect.gif">







<br>
아키텍처 과정 설명<br>
3. reverse SSH 설정<br>
4. 쓰레기통 드론 AP연결<br>
5. TCP 통신<br>
결과물 사진 or GIF<br>
향후 개발 방향
