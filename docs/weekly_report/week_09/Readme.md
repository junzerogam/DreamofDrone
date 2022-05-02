<h2>9주차 회의록</h2>
<h4>회의 일시 : 2022.04.28</h4>
<h4>참석자 : 조우형, 김준영, 박중후, 유예린</h4>
<h4>회의 주제 : 진행상황 및 통신 방법 결정  </h4>

----------------------------------------------------------
<h3>-회의 내용-</h3>

 <h4>진행 상황</h4> 
  
  • 통신 팀 
  
   **LTE 모듈을 드론에 결합 완료.
   - 결합하기 전 : ![image](https://user-images.githubusercontent.com/71144019/166268348-cd7665ff-cf92-4b65-8882-4a931e2dbfa4.png)
   - 결합한 후 : ![image](https://user-images.githubusercontent.com/71144019/166268482-0ab58f15-482d-433f-8191-515c19ac1213.png)
   **USIM을 등록시켜서 LTE를 끄고 켜는 것이 가능하게 연결 완료.
   ![image](https://user-images.githubusercontent.com/71144019/166268661-ead9b15d-b9fa-4f46-8428-1af73907b916.png)![image](https://user-images.githubusercontent.com/71144019/166268683-aaaa8358-4f61-4a14-873d-caece1f10c54.png)
   - 문제점 :  mavproxy로 드론에 연결하려 했지만 계속 오류가 남.
        - 해결방법 : 다시 라즈베리파이 os 설치하고 , FC와 라즈베리파이를 usb로 직접 연결시켜서 해결.
   - **라즈베리파이와 FC에 원격으로 접속 성공.
   ![image](https://user-images.githubusercontent.com/71144019/166268914-edbf3a2a-8035-4cc0-9ee8-53c328e68869.png)
   - **Reverse SSH 통신을 통해 드론에 원격으로 접속할 수 있도록 설정 성공.
   ![image](https://user-images.githubusercontent.com/71144019/166268968-8bec9c1b-7917-444b-9d5d-f93f52198918.png)

  • 임베디드 팀
  
   - 초음파 센서와 무게코드를 결합하여 작동 성공.
   - 적외선 센서와 서보모터 코드를 결합하여 작동 성공.
   - 




  <h3><중간고사 이후 추후 계획></h3>
  
  • 통신 팀
   1. mavlink로 드론 비행 코드 제작/ 구현.
   2. LTE모듈 드론에 장착 및 세팅.
   3. 소켓통신 프로그래밍와 임베디드 코드와 결합.

  • 임베디드 팀
   1. 데이터 가공 알고리즘 제작.
   2. 상시코드 동작 구현 목표와 스마트 쓰레기통 하드웨어 제작.
 

