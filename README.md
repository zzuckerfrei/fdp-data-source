
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
│   │   ├── routers          
│   │   │   ├── __init__.py
│   │   │   ├── meta.py        # 
│   │   │   └── item.py        # 
│   │   └── service
│   │       ├── __init__.py
│   │       └── item.py        # 
│   ├── models                 # package for DTO 
│   │   ├── __init__.py
│   │   ├── meta.py
│   │   ├── competition.py
│   │   ├── match.py
│   │   ├── lineup.py
│   │   └── event.py
│   └── schemas                 # 
│       ├── __init__.py
│       └── msg.py
```

### build & deploy
```
docker build -t fdp-data-source:v0.12 .

docker run -d \                                                                                            ✔  fdp-pypack 
-p 8000:8000 \
--network fdp-net \
-v {your-data-dir}/data:/usr/src/data \
--name fdp-data-source \
fdp-data-source:v0.12
```


last update 20221031