
# fdp-data-source
file to mongoDB api

### Features
* FastAPI
* pydantic
* beanie


### project architecture
```
.
├── app                        
│   ├── __init__.py          
│   ├── main.py          
│   ├── config.py              
│   ├── database.py            
│   ├── api                    
│   │   ├── __init__.py       
│   │   ├── api.py             
│   │   ├── dependencies.py         
│   │   ├── routers          
│   │   │   ├── __init__.py
│   │   │   ├── meta.py         
│   │   │   └── item.py         
│   │   └── service
│   │       ├── __init__.py
│   │       └── item.py         
│   ├── models                  
│   │   ├── __init__.py
│   │   ├── meta.py
│   │   ├── competition.py
│   │   ├── match.py
│   │   ├── lineup.py
│   │   └── event.py
│   └── schemas                 
│       ├── __init__.py
│       └── msg.py
```

### build & deploy
```
docker build -t fdp-data-source:v0.13 .

docker run -d \ 
-p 8000:8000 \
--network fdp-net \
-v {your-data-dir}/data:/usr/src/data \
--name fdp-data-source \
fdp-data-source:v0.13
```


last update 20221120