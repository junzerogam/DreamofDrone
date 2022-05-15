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
<p align="center">
  <img width="80%" height="80%" src="/docs/img/drone/drone_architecture.PNG">
</p><br>

![Architecture](/docs/img/drone/architecture_basic_new.PNG)

- **Progress**<br>

> ✔ **LTE Module 부착** <br>

<img align="left" width="350" height="250" src="/docs/img/drone/connect_LTE_Module.jpg">
<br><br>
1. LTE Module 및 안테나 연결<br><br>
2. Sixfab 모듈 펌웨어 설치<br><br>
3. eth0, wlan0 해제 후 셀룰러 모드 동작 확인<br><br>
<br clear="left"/><br>

***
> ✔ **MAVProxy로 FC 통신하는 GCS 설정** <br>

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
<p align="center">
  <img src="docs/img/drone/MavProxy_GCS_UDP_Connect.gif">
</p>

<div align=center>MAVProxy를 사용하여 5001포트로 연결한 후 원격으로 드론을 제어하는 모습</div>

***
> ✔ **Reverse SSH 원격 접속** <br>

<p align="center">
  <img width="80%" height="80%" src="docs/img/drone/sshkey_exchange.PNG">
</p>

<div align=center>인증된 자동 ssh 로그인을 위한 인증키 생성 및 교환</div><br>

```
pi@drone:~ $ sudo ssh -f -N -T -R 2222:localhost:22 uhyeong@[routerIP] -p 5001
```
```
uhyeong@DESKTOP-R39GAN6:~$ ssh pi@localhost -p 2222
```

***
> ✔ **드론 무선 AP에 스마트 쓰레기통 연결** <br>


***
> ✔ **드론과 스마트 쓰레기통 TCP 통신** <br>


<br>향후 개발 방향..
