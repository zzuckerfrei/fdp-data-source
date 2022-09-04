
# fdp-data-source

FastAPI, pymongo


### project architecture
```
.
├── app                        # "app" is a Python package
│   ├── __init__.py          
│   ├── main.py                # "main" module, e.g. import app.main
│   ├── config.py              # config
│   ├── database.py            # database
│   ├── api                    # package for api
│   │   ├── __init__.py       
│   │   ├── api.py             # router를 묶는 파일. 최종적으로 main에서 이 파일만 불러옴
│   │   ├── dependencies.py    # "dependencies" module, e.g. import app.dependencies. 여기에 get_db()로 session(client)생성한 것 받아오기     
│   │   └── routers          
│   │       ├── __init__.py
│   │       ├── meta.py        # dir 카운트, 목록
│   │       └── item.py        # path param으로 데이터타입구분, 
│   ├── models                 # package for DTO 
│   │   ├── __init__.py
│   │   ├── meta.py
│   │   └── item.py
```
last update 20220903