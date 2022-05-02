<h2>9주차 회의록</h2>
<h4>회의 일시 : 2022.04.28</h4>
<h4>참석자 : 조우형, 김준영, 박중후, 유예린</h4>
<h4>회의 주제 : 진행상황 및 통신 방법 결정  </h4>

----------------------------------------------------------
<h3>-회의 내용-</h3>

 <h4>진행 상황</h4> 
  
  • 통신 팀 
  
   **LTE 모듈을 드론에 결합 완료.**
   - 결합하기 전<br>
   ![image](https://user-images.githubusercontent.com/71144019/166268348-cd7665ff-cf92-4b65-8882-4a931e2dbfa4.png)
   - 결합한 후<br>![image](https://user-images.githubusercontent.com/71144019/166268482-0ab58f15-482d-433f-8191-515c19ac1213.png)<br>  
   **USIM을 등록시켜서 LTE를 끄고 켜는 것이 가능하게 연결 완료.**<br>
   ![image](https://user-images.githubusercontent.com/71144019/166268661-ead9b15d-b9fa-4f46-8428-1af73907b916.png)<br>![image](https://user-images.githubusercontent.com/71144019/166268683-aaaa8358-4f61-4a14-873d-caece1f10c54.png)<br>
   - 문제점 :  mavproxy로 드론에 연결하려 했지만 계속 오류가 남.
        - 해결방법 : 다시 라즈베리파이 os 설치하고 , FC와 라즈베리파이를 usb로 직접 연결시켜서 해결.<br>  
 
   **라즈베리파이와 FC에 원격으로 접속 성공.**<br>
   ![image](https://user-images.githubusercontent.com/71144019/166268914-edbf3a2a-8035-4cc0-9ee8-53c328e68869.png)<br>
   **Reverse SSH 통신을 통해 드론에 원격으로 접속할 수 있도록 설정 성공.**<br>
   ![image](https://user-images.githubusercontent.com/71144019/166268968-8bec9c1b-7917-444b-9d5d-f93f52198918.png)<br>

  * 임베디드 팀
  
   - 초음파 + 무게 코드와 적외선 + 서보모터 코드를 하나의 코드로 결합.
   - 초음파 센서로 사람이 쓰레기통 주변 일정거리에 도달했을 때 쓰레기통 뚜껑이 열리도록 코드와 하드웨어 구현.
   - 무게 센서로 쓰레기가 들어가있는 무게 데이터값을 측정해오는 것 구현.


  <h3><10주차 계획></h3>
  
  - 통신 팀
   - 임베디드 팀의 코드를 받아서 소켓 통신 코드 구현.

  - 임베디드 팀
   - 쓰레기 내부에 초음파 센서 부착
   - 선 정리
   - 코드 리팩토링
   - 완성품 제작
 

