## 가상환경 설정

- 왜 하나요?
  " 현재 프로젝트 위한 환경 설정 위해서

- 어떻게 하나요?


```bash
# 대체로 폴더명은 venv 로 작성한다.
$ python -m venv {폴더 명}
# 가상환경을 활성화 (mac 사용자는 Scripts -> bin)
$ source venv/Scripts/Activate
# 사용할 외부 라이브러리 설치
$ pip install requests
# 패키지 목록 확인
$ pip list
# 활성화된 가상환경에 설치된 패키지 목록만 기록
$ pip freeze > requirements.txt
# 가상환경 종료
$ deactivate
# requirements.txt 에 기록된 패키지 설치 해당 파일을 읽어서 설치해줌
$ pip install -r requirements.txt
```

