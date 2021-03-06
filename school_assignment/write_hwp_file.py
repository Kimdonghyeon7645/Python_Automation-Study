import win32com.client as win32  # 한/글 열기 위한 모듈
# import win32gui  # 한/글 창을 백그라운드로 숨기기 위한 모듈


def write_hwp_file(content_list: list):
    hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")  # 한/글 열기
    hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")
    hwp.Open(r"C:\Users\user\Documents\Python_Automation-Study\school_assignment\date_source\java_summary_text.hwp")

    field_list = [i for i in hwp.GetFieldList().split("\x02")]  # 한/글 안의 누름틀 목록 불러오기
    hwp.Run('SelectAll')  # Ctrl-A (전체선택)
    hwp.Run('Copy')  # Ctrl-C (복사)
    hwp.MovePos(3)  # 문서 끝으로 이동

    print(f'총 {len(content_list)-1}행 추출, 복사를 시작합니다.')
    for i in range(len(content_list)-1):
        hwp.Run('Paste')  # Ctrl-V (붙여넣기)
        hwp.MovePos(3)  # 문서 끝으로 이동

    for page in range(len(content_list)):  # 한/글 모든 페이지를 전부 순회
        for field in field_list:  # 모든 누름틀 순회
            hwp.PutFieldText(f'{field}{{{{{page}}}}}',  # f"{{{{{page}}}}}"는 "{{1}}"로 입력된다. {를 출력하려면 {{를 입력
                             content_list[page])  # hwp.PutFieldText("index{{1}}") 식으로 실행


if __name__ == '__main__':
    from school_assignment.read_md_files import *
    from school_assignment.edit_content import *

    write_hwp_file(edit_content(get_files_text(get_files_name())))
