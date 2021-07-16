# snake-game

[플레이해보기](https://codepsy-2001.github.io/snake-game/)

방향키로 녹색 뱀을 조작하고 흰색 먹이를 먹으세요. 자기 자신과 부딪치거나, 세계 경계에 닿으면 몸길이가 초기화됩니다. 몸을 최대한 길게 늘려보세요!


#### 완전히 구현된 기능

- Snake, Food, Game 객체화
  - 물리엔진/렌더러 분리
  - SnakeBody 객체와 Snake 분리
  - Iterable 메소드 적용 (충돌감지, 뱀 이동 등)
  - 객체지향 충돌감지 및 
  - 하드코딩, 전역변수 최소화
- 창 크기 변경 감지, 반응형 웹 디자인
- Snake.control() 책임과 Snake.keyPressed() 책임 분리
  - 현재 방향과 정반대로 선회해서 어이없이 죽는 현상 방지
- 배경음 및 효과음 재생


#### 애매하게 구현된 기능

- Control 관련 객체화, 책임 분리
  - ↑→를 한 프레임 안에 입력시, ↑를 한칸 실행한 후 →를 실행하는 기능 (선입력)
  - 아예 keyPressed()를 쌓아놓고 스택을 만들어서 control()에 전해주는 구현 필요


#### 구현이 필요한 기능

- 웹소켓을 활용한 온라인 멀티플레이