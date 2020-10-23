import os
from typing import List
import shutil  # 파일복사용 모듈
import win32com.client as win32  # 한/글 열기 위한 모듈
# import win32gui  # 한/글 창을 백그라운드로 숨기기 위한 모듈
import time

java_md_file_path = r"C:\Users\user\Documents\Python_Automation-Study\school_assignment\date_source\java"


def get_files_name() -> list:
    file_list: List[str] = os.listdir(java_md_file_path)
    file_list.remove("11. 기본 API 클래스")
    lesson_10_list: List[str] = os.listdir(java_md_file_path + r"\11. 기본 API 클래스")
    file_list.extend(["11. 기본 API 클래스\\" + name for name in lesson_10_list])
    file_list.sort()
    return file_list


def get_files_text(name_list: list) -> list:
    text_list: List[str] = []
    for name in name_list:
        with open(java_md_file_path + "\\" + name, 'rt', encoding="utf-8") as f:
            text_list.append(f.read())
    return text_list


if __name__ == '__main__':
    file_names = get_files_name()
    print(*file_names, sep="\n")
    print(*get_files_text(file_names), sep="\n")
