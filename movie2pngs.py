import cv2
import numpy as np
import os
import glob
import re
from pathlib import Path
def main(path, dir, step, extension):
    movie=cv2.VideoCapture(path)
    Fs=int(movie.get(cv2.CAP_PROP_FRAME_COUNT))
    path_head=dir+'\out_'
    ext_index=np.arange(0, Fs, step)
    for i in range(Fs):
        flag, frame=movie.read()
        check=i==ext_index
        if flag==True:
            if True in check:
                if i < 10:
                    path_out=path_head+'0000'+str(i)+extension
                elif i < 100:
                    path_out=path_head+'000'+str(i)+extension
                elif i < 1000:
                    path_out=path_head+'00'+str(i)+extension
                elif i < 10000:
                    path_out=path_head+'0'+str(i)+extension                    
                else:
                    path_out=path_head+str(i)+extension
                cv2.imwrite(path_out, frame)
            else:
                pass
        else:
            pass
    return
if __name__=="__main__":
    BaseFolder= r"C:\\Users\\user\\python\\avi2exl\\movie_file"
    InputStep=input('ステップ数入力（例：100; 100ステップに1枚）: >>')
    NumStep=int(InputStep)
    path=Path(BaseFolder)
    Files=sorted(path.glob('*.*'))
    for FileName in Files:
        MovieFile=str(FileName)
        print('MovieFile', MovieFile)
        MovieName=MovieFile.split('\\')[-1].split('.')[-2]
        print('MovieName', MovieName)
        NewFolder=r"C:\\Users\\user\\python\\avi2exl\\movie_file\\pngs\\"+MovieName
        print('BaseFolder', BaseFolder)
        print('NewFolder', NewFolder)
        os.mkdir(NewFolder)
        main(MovieFile, NewFolder, NumStep, '.png')