function loadDoc() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.setRequestHeader('', '');

    // onreadystatechange 이벤트 핸들러 작성
    xmlHttp.onreadystatechange = function() {
        // 서버상에 문서가 존재하고 요청한 데이터의 처리가 완료되어 응답할 준비가 완료되었을 때
        if(this.status == 200 && this.readyState == this.DONE) {
            // 응답받은 데이터를 (내가 <script>로 들어가있는) HTML 파일의 'text' 라는 id를 가진 태그에 쏜다
                //document.getElementById("text").innerHTML = xmlHttp.responseText;
            alert("데이터 전송 완료!");
        }
    };

    xmlHttp.open("POST", "/rank", true); // 요청을 초기화 (true로 지정시 비동기로 실시간 응답받음)
    xmlHttp.send(); // 요청을 서버로 보냄 (xmlHttp 인스턴스가 자기 자신의 state를 바탕으로 서버에 비동기 요청 전송)
    // 비동기로 전송된 요청은 events 를 사용해 응답받음. 나중에 꺼내서 쓰면 됨 (예: responseText)
}

// 비동기 프로그래밍은 작성하려면 머리가 터지지만, 약간의 시스템 이해와 문법적 꼼수로 우리도 쉽게 사용할 수 있다.
// open, send, onreadystatechange 등이 "비동기로 동작한다"는 것을 명심해야 함 (필요할 때마다 호출되어 작동함)
// 일종의 프레임워크처럼 생각해도 괜찮다.
