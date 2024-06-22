from ast import Pass
import os
from pathlib import Path
from collections import list

def get_current_working_directory() -> Path:
           return Path.cwd()

def get_file_names() -> list[str]:
           return os.listdir(pwd)

def put_in_img_dir():
           Pass

def put_in_doc_dir():
           Pass

if __name__ == '__main__':
           pwd = get_current_working_directory()
           files = get_file_names()

           for file in files:
                      path = pwd / file

                      if os.path.isdir(path):
                                 continue                      

                      if '.png' in file:
                                put_in_img_dir()
                      elif file.endswith('.pdf'):
                                 put_in_doc_dir()
                      elif file.endswith('.txt'):
                                 put_in_doc_dir()
 
