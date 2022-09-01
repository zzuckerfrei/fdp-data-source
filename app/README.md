
# fdp-data-source

FastAPI, pymongo


### project architecture
```
.
├── app                        # "app" is a Python package
│   ├── __init__.py          
│   ├── main.py                # "main" module, e.g. import app.main
│   ├── config.py              # config파일
│   ├── api                    # package for api
│   │   ├── __init__.py       
│   │   ├── api.py             # router를 묶는 파일. 최종적으로 main에서 이 파일만 불러옴
│   │   ├── dependencies.py    # "dependencies" module, e.g. import app.dependencies. 여기에 get_db()로 session(client)생성한 것 받아오기     
│   │   └── routers          
│   │       ├── __init__.py   
│   │       ├── event.py       # "event" submodule, e.g. import app.api.routers.event
│   │       ├── lineup.py      # "lineup" submodule, e.g. import app.api.routers.lineup
│   │       ├── match.py       # "match" submodule, e.g. import app.api.routers.match
│   │       └── three-sixty.py # not yet
│   ├── schemas                # package for DTO 
│   │   ├── __init__.py
│   │   ├── event.py
│   │   ├── lineup.py
│   │   ├── match.py
│   │   └── three-sixty.py     # not yet
│   └── db                     # package for db session manage
│       ├── __init__.py
│       └── session.py         # client생성
```
last update 20220830