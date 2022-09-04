from db import client


def get_client():
    return client.get_client()


# 삭제?
# def get_session():
#     return get_client().start_session(causal_consistency=True)


'''
mongoDB는 강제로 session close하지 않고 저절로 닫히도록 두는 것이 효과적이라고 함
일단 클라이언트 생성만 하고 개발..
# https://stackoverflow.com/questions/41607517/do-i-need-to-close-pymongo-session

def get_db() -> Generator:
    try:
        db = get_session()
        print("111111")
        print(db)
        yield db
    finally:
        db.close()
'''