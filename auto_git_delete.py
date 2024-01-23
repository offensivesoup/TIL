# import glob
# import os
# import shutil

# rLst = [1,2,3,4,5,'a','b','c']
# day  = 6
# file_lst = []
# for route in rLst:
#     try:
#         if route == 2 or route == 4:
#             file_path = glob.glob(f'python_hw_{day}_{route}/.git')
#             os.rmdir(file_path[0])
#             file_path = glob.glob(f'python_ws_{day}_{route}/.git')
#             os.rmdir(file_path[0])
#         else:
#             file_path = glob.glob(f'python_ws_{day}_{route}/.git')
#             os.rmdir(file_path[0])
#         print('git이 삭제되었습니다.')
#     except Exception as ex:
#         print(ex)

# 자동으로 .git 폴더 삭제 해주는 코드.
# 현재 폴더를 기준으로 모든 폴더를 조사하여서.
# .git 폴더를 삭제한다.
    # 단, 최상위 폴더 (코드가 실행된 위치의 .git은 제외하고)

import os
import subprocess

# 현재 폴더 경로를 변수에 저장
current_folder = os.getcwd()
# 현재 폴더 및 모든 하위 폴더를 반복

for foldername, subfolders, filenames in os.walk(current_folder): # generator라는 객체 => 순회가능하다.
    # print(foldername, 'fn')
    # print(subfolders, 'sf')
    # print(filenames,  'fn')
    # 하위 폴더 목록에 .git이 있다면
    if '.git' in subfolders:
        # root 디렉토리는 제외
        if foldername == current_folder:
            continue # 아래코드 실행하지 말고, 다음 순회로 넘어가라
        # 그 외 모든 경우에 대해선
        # .git 폴더를 삭제할 것이다.
        # 삭제하려는 .git 폴더 위치를 변수에 저장하는 일이 필요하다
        git_folder_path = os.path.join(foldername, '.git')
        # 경로 : '' + '' X
        # 경로 : 'folder' + '.git' -> folder/.git
        # git_folder_path
        # rm -rf 폴더 경로
        subprocess.run(['rm','-rf',git_folder_path])
        print(f'{git_folder_path} 폴더가 삭제되었습니다.')
        

