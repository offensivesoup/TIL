import glob
import os
import shutil
rLst = [1,2,3,4,5,'a','b','c']
day  = 6
file_lst = []
for route in rLst:
    try:
        if route == 2 or route == 4:
            file_path = glob.glob(f'python_hw_{day}_{route}/.git')
            os.rmdir(file_path[0])
            file_path = glob.glob(f'python_ws_{day}_{route}/.git')
            os.rmdir(file_path[0])
        else:
            file_path = glob.glob(f'python_ws_{day}_{route}/.git')
            os.rmdir(file_path[0])
        print('git이 삭제되었습니다.')
    except Exception as ex:
        print(ex)