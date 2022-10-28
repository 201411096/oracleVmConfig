1. 수정이 필요한 부분
insertDummyData_linux.py의 password, dsn 수정 필요

2. 파일 구조
--oracle
	--project_insertDummyData
		--insertDummyData.Dockerfile
		--insertDummyData_linux.py
		--pip-requirements.txt
		--instantclient // 리눅스 버전확인
			--instantclient_21_8
				--network
					--admin // wallet 파일들을 복붙해둔 위치

3. command
- cd ~/oracle/project_insertDummyData
- sudo docker build --no-cache -f insertDummyData.Dockerfile -t insert_dummydata_app . &
- ctrl + p -> ctrl + q -> ctrl + c    // 컨테이너를 종료시키지 않고 빠져나오기
