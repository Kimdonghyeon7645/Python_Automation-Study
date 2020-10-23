from school_assignment.write_hwp_file import *
from school_assignment.read_md_files import *

if __name__ == '__main__':
    summary_file_names = get_files_name()
    summary_file_contents = get_files_text(summary_file_names)
    write_hwp_file(summary_file_contents)
    print("프로그램이 정상 종료되었습니다... ^^7")
