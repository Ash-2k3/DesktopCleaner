from ast import Pass
import os
from pathlib import Path
from collections import UserList
import shutil

def get_current_working_directory() -> Path:
           return Path.cwd()

def get_file_names():
           return os.listdir(pwd)

def put_in_img_dir(file):
           Pass

def put_in_doc_dir(file):
           pwd = get_current_working_directory()
           docFilePath = pwd / 'S-Docs'

           if not os.path.exists(docFilePath):
                      os.mkdir('S-Docs')

           shutil.move(str(pwd / file), str(docFilePath))
                      

if __name__ == '__main__':
           pwd = get_current_working_directory()
           files = get_file_names()

           for file in files:
                      path = pwd / file

                      if os.path.isdir(path):
                                 continue                 

                      if '.png' in file:
                                put_in_img_dir(file)
                      elif file.endswith('.pdf'):
                                 put_in_doc_dir(file)
                      elif file.endswith('.txt'):
                                 put_in_doc_dir(file)
 
