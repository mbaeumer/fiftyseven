#!/usr/bin/python
from input_util import get_yes_no_answer
from input_util import get_string_value
from file_util import create_folder
from file_util import write_content_to_file

def main():
  print_title()
  site_name = get_string_value("What is the site´s name?")
  author = get_string_value("What is the author´s name?")
  create_js = get_yes_no_answer("Do you want a folder for js? (y/n)")
  create_css = get_yes_no_answer("Do you want a folder for css? (y/n)")
  print("Required js: ", create_js)
  print("Required css: ", create_css)
  create_folder("app")
  if create_js:
    create_folder("app" + "/js")
  if create_css:
    create_folder("app" + "/css")

  write_content_to_file("app/index.html", "my title", author)
      
def print_title():
  print("Exercise 43: Web site generator")
  print("")

if __name__ == '__main__':
  main()
