import os
import glob

from config import settings


class ItemModelFinder:
    def __init__(self):
        pass

    def __call__(self, data_type: str):
        return settings.DATA_TYPE[data_type][0]


item_model = ItemModelFinder()


class FileFinder:
    def __int__(self):
        pass

    def __call__(self, data_type):  # 여기서 받는 param은 query param임
        return get_method_by_data_type(data_type)


file_list = FileFinder()


def get_method_by_data_type(data_type):
    result = list()
    folder_path = settings.FILE_DIR[data_type]

    if data_type == "match":
        for sub_folder in get_folder_names(folder_path):
            result.extend(get_file_names(sub_folder))

    result.extend(get_file_names(folder_path))

    return sorted(list(set(result)))


def get_file_names(folder_path, pattern="*.json"):
    """
    :param folder_path:
    :param pattern:
    :return:
    """
    lst_files = glob.glob(folder_path + "/" + pattern)
    lst_searched = []

    for x in lst_files:
        if os.path.isfile(x):
            lst_searched.append(x)

    return lst_searched


def get_folder_names(folder_path):
    """
    :param folder_path:
    :return:
    """
    lst_files = glob.glob(folder_path + "/" + "*")
    lst_searched = []

    for x in lst_files:
        if os.path.isdir(x):
            lst_searched.append(x)

    return lst_searched


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
