#!/usr/bin/python
import os
from html_util import generate_html_tag
from html_util import generate_meta_tag
from html_util import generate_title

def write_content_to_file(file_name, title, author):
  file = open(file_name, "w")
  file.write(generate_html_tag("html", False, True))
  file.write(generate_html_tag("head", False, True))
  file.write(generate_title(title))
  file.write(generate_meta_tag(author))
  file.write(generate_html_tag("head", True, True))
  file.write(generate_html_tag("html", True, True))
  
  file.close()

def create_folder(folder_name):
  if not os.path.exists(folder_name):
    os.makedirs(folder_name)
  else:
    print("ERROR: The folder already %s already exists!" % (folder_name))
