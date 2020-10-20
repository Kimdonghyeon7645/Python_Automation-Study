import os
from typing import List

java_md_file_path = r"C:\Users\user\Documents\Python_Automation-Study\school_assignment\date_source\java"


def get_files_name() -> list:
    files_list: List[str] = os.listdir(java_md_file_path)
    lesson_10_list: List[str] = os.listdir(java_md_file_path + r"\11. 기본 API 클래스")
    files_list.extend(lesson_10_list)
    files_list.sort()
    return files_list


if __name__ == '__main__':
    print(*get_files_name(), sep="\n")
