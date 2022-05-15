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
1. LTE Module 및 안테나 연결<br><br>
2. Sixfab 모듈 펌웨어 설치<br><br>
3. eth0, wlan0 해제 후 셀룰러 모드 동작 확인<br><br>
<br clear="left"/>




<br>
아키텍처 과정 설명<br>
1. ~~모듈 설치~~<br>
2. MavProxy로 FC 통신<br>
3. reverse SSH 설정<br>
4. 쓰레기통 드론 AP연결<br>
5. TCP 통신<br>
결과물 사진 or GIF<br>
향후 개발 방향
