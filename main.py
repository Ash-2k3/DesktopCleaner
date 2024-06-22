from ast import Pass
import os
from pathlib import Path

def get_current_working_directory():
           Pass

def get_file_names():
           Pass

def put_in_img_dir():
           Pass

def put_in_doc_dir():
           Pass

if __name__ == '__main__':
           pwd = Path.cwd()
           files = os.listdir(pwd)

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
 
