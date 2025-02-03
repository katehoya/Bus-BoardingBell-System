# 버스 승차벨 시스템  

***

## 제작 동기  
퇴근 시간에 강남에서 경희대학교로 올 때 양재IC 부근에서 차가 심하게 막히는 현상을 겪었습니다  
![image](https://github.com/user-attachments/assets/3c589c7c-597a-4b12-a145-26dfda7cba6b)  
제가 판단한 주요 원인으로는 양재 IC 진입 전 22296, 22298 버스 정류장이었습니다.  
정차를 하려고 1 -> 4차선으로 이동하는 버스들, 승객을 태우고 다시 주행하려 4 -> 2,3차선으로 이동하는 버스들이 마치 교착상태에 빠진 것처럼 보였습니다.
한 정류장에 수십대의 버스가 정차하는 데다가, 승용차보다 길이가 길다보니 뒤의 차들까지 체증이 심해졌습니다.  
그래서 정류장에 승차 인원, 하차 인원이 한 명도 없으면 굳이 정차를 안 해도 되지 않을까? 라는 생각이 들었습니다.   

***

## 버스 승차벨이 필요한 이유  
현재 설치된 버스 승차벨은 승객의 승차 의사를 명확히 하기 위한 용도로 설치돼 있습니다.  
그래서 주로 인적이 드문 곳이나 한적한 정류장에만 설치돼 있습니다.  
그러나 기존의 의사소통 방향이 버스 -> 승객 으로 일방향적이었던 것에 비해 양방향 의사소통이 이루어진다면 버스의 운행에 있어 큰 도움이 될 것 같다고 생각합니다.  
### 장점  
1. 승차, 하차인원이 아무도 없는 경우 무정차 통과를 할 수 있습니다
   - 교통체증 완화
   - 버스 기사의 운전 편리성  
2. 버스의 정시성 제고  
   - 승하차 인원이 없을 때 항상 무정차 통과를 해야 하는 것은 아닙니다.  
     그러나 앞 차와의 간격이 벌어졌을 때 기사님의 판단에 따라 승하차 인원이 없을 시 무정차 통과를 한다면 버스의 정시성을 제고하는 데 큰 도움이 될 것이라 생각합니다.  
3. 자율 주행 버스
   - 미래에 자율 주행 버스가 많이 도입될텐데,  
     자율 주행 버스는 각종 도로상황과 정류장 상황을 종합적으로 판단하여 주행합니다.
     이 때 정류장의 승차인원의 유무에 대한 데이터가 있다면 자율 주행 버스의 의사결정에 도움이 될 것이라 생각합니다.  
4. 명확한 승차 의사 표시
   - 승차 승객이 있음에도 명확한 표현을 하지 않아 버스가 무정차 통과를 하는 경우,
     버스 기사님이 정류장에 승객이 있는지 없는지 눈치를 보며 정류장을 빠져나가는 등의 애매한 상황을 방지할 수 있다.  

### 단점  
1. 한 승객이 여러 대의 버스를 탈 가능성이 있는 경우 승차벨을 여러 개 누르면 정확도가 낮아질 수 있습니다
    - 현재까지 예상되는 가장 중요한 문제점입니다
2. 시민 인식 부족
    - 처음엔 정류장에서 단지 기다리는 것이 아닌버스 벨을 굳이 눌러야 하는 귀찮음에 따른 승객의 불편함이 예상됩니다
      그러나 기존에 사용하던 하차벨과 동일한 디자인으로 승차벨을 설계한다면 좀 더 쉽게 시민들이 받아들일 수 있을 것이라고 생각합니다.  
      
***  

## 정류장에서 무정차 통과를 하는 버스  
데이터 출처 : https://stcis.go.kr/wps/main.do  
아래 표는 24년 11월 2일 22296, 22298 버스정류장에서 정차한 서울 버스의 시간당 승하차 인원 수를 배차 간격(시간당 버스 도착 횟수)로 나눈 것입니다.  
정류장에 정차했지만 승하차 인원이 한 명도 없는, 그런 무의미한 정차를 하는 경우가 많이 있는지 알아보기 위함입니다.  
지표가 1보다 작으면 무의미한 정차를 시간당 최소 1번이상 한다는 것을 의미합니다.
![image](https://github.com/user-attachments/assets/dd23f767-193b-4c61-b7d9-73a76745cb0f)  
 - 경기 버스를 포함한 시외버스는 제외한 지표입니다. 이들까지 합치면 무의미한 정차를 하는 버스의 수는 훨씬 많을 것으로 예상됩니다
 - 출퇴근 시간에도 승하차 인원이 한 명도 없는 경우가 꽤 있다는 것을 알 수 있습니다.
***
## 버스 한 대가 무정차 통과할 시에 교통 흐름은 어떻게 바뀔까?  
