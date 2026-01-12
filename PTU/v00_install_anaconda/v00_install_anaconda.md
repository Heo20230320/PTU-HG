폴더명 :v00_install_anaconda
파일명 : v00_install_anaconda.md

검색 > 시스템환경변수설정 > 환경변수 > 시스템변수 > Path >
4가지 항목 추가 : anaconda3 / bin / Library / Scripts


윈도우에서 아나콘다를 설정하는 데 필요한 명령어는 다음과 같습니다:
가상환경 생성: conda create -n myenv python=3.8 (여기서 myenv는 원하는 환경 이름, python=3.8는 원하는 파이썬 버전을 지정합니다.) 
1
가상환경 활성화: conda activate myenv (여기서 myenv는 생성한 가상환경 이름입니다.) 
1
가상환경 비활성화: conda deactivate (여기서 myenv는 생성한 가상환경 이름입니다.) 
1
패키지 설치: conda install package_name (여기서 package_name은 설치할 패키지 이름입니다.) 
1
패키지 업데이트: conda update package_name (여기서 package_name은 설치된 패키지 이름입니다.) 
1
패키지 제거: conda uninstall package_name (여기서 package_name은 제거할 패키지 이름입니다.) 
1

이 명령어들을 사용하여 아나콘다에서 다양한 패키지를 설치하고 관리할 수 있습니다. 아나콘다의 기본적인 사용법에 대한 자세한 내용은 아나콘다 공식 웹사이트나 관련 자료를 참조하시기 바랍니다. 
1