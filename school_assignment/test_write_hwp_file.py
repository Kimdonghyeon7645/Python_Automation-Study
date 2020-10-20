import win32com.client as win32  # 한/글 열기 위한 모듈
# import win32gui  # 한/글 창을 백그라운드로 숨기기 위한 모듈


hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")  # 한/글 열기
# hwnd = win32gui.FindWindow(None, '빈 문서 1 - 한글')  # 한/글 창의 윈도우핸들값을 알아내서
# win32gui.ShowWindow(hwnd, 0)  # 한/글 창을 백그라운드로 숨김
hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")  # 보안모듈 적용(파일 열고닫을 때 팝업이 안나타남)
hwp.Open(r"C:\Users\user\Documents\Python_Automation-Study\school_assignment\date_source\test.hwp")  # 수정할 한/글 파일 열기

field_list = [i for i in hwp.GetFieldList().split("\x02")]  # 한/글 안의 누름틀 목록 불러오기
print(field_list)
hwp.Run('SelectAll')  # Ctrl-A (전체선택)
hwp.Run('Copy')  # Ctrl-C (복사)
hwp.MovePos(3)  # 문서 끝으로 이동

count = int(input("몇 페이지를 복사할 것인가요?"))
content = input("무엇을 입력할 것인가요?")
print('페이지 복사를 시작합니다.')

for i in range(count-1):
    hwp.Run('Paste')  # Ctrl-V (붙여넣기)
    hwp.MovePos(3)  # 문서 끝으로 이동
    print(f"{i}페이지 복사 완료")

for page in range(count):  # 한/글 모든 페이지를 전부 순회하면서,
    for field in field_list:  # 모든 누름틀에 각각,
        hwp.MoveToField(f'{field}{{{{{page}}}}}')  # 커서를 해당 누름틀로 이동(작성과정을 지켜보기 위함. 없어도 무관)
        hwp.PutFieldText(f'{field}{{{{{page}}}}}',  # f"{{{{{page}}}}}"는 "{{1}}"로 입력된다. {를 출력하려면 {{를 입력.
                         content)  # hwp.PutFieldText("index{{1}}") 식으로 실행될 것.

# hwp.Save()  # 한/글 파일(award_result.hwp)을 저장하고,
# hwp.Quit()  # 한/글 종료. (저장하지 않고 종료하는 방법은 7강에서~)
