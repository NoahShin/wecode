git branch 라고 명령어를 치면, 
내가 해당하는건 별 표시 뜨고, 내가 지금 어디 브랜치인지 알려준다.
. (내가 어디 브랜치에 있는지 자주 확인해주는 습관을 가지는게 좋다.
그러면 이제 로컬에 마스터(메인)이 생겼다, 
이제 여기 기준으로 feature/branch 를 만들어준다 
(feature/브랜치 이름 <<feature는 컨밴션 개념 ,,, git branch 이름 (ex. git branch feature/readme 
(feature/ 앞에 붙히는게 컨밴션,,?!)

깃이 무엇을 관리 하는 프로그램인가! 버젼관리
git checkout feature/readme 라고 뜬다.
내 브랜치에서 내 폴더를 만들고, 거기다 작업하고
git add. ( .은 여기있는거 싹다)
git status ( 뭐가 바뀌는지 확인)
git commit 하고
git push origin 브랜치이름,,,, 하면 내 브랜치가 github으로 올라간다.
10.1 git pull request
github에서 merge를 해주면 내 로컬 브랜치는 이제 존재 이유가 없어서 지워도 된다 (나중에 헷갈리니까 지우자)
오리진에서 머지된것을 받고 싶을때 git pull origin main, 오리진에서 마스터로 땡긴다.
땡겨진 제일 최신 코드들이 내 로컬에 잇고 그것에서 작업 그리고
중요 개념... 내 feature/readme (로컬)에 있는걸 내 로컬 마스터로 가져오진 않는다.
피쳐를 푸쉬해서 위로 올리고, 머지하고, pull origin main 해서 로컬 마스터로 가져온다. (한바퀴 도는,,)
많은 작업같지만, 변동사항만 트래킹해서 옮긴다.
