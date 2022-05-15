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
  - LTE Module 부착<br>
  <p align="center">
    <img src="/docs/img/drone/connect_LTE_Module.jpg">
  </p>


아키텍처<br>

아키텍처 설명<br>
결과물<br>
향후 개발 방향
