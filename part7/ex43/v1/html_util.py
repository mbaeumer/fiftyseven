#!/usr/bin/python

def generate_html_tag(tag_name, isEnd, includeLineBreak):
  result = "</" + tag_name + ">"
  if not isEnd:
    result = result.replace("/", "")
  if includeLineBreak:
    result = result + "\n"
  return result

def generate_meta_tag(author):
  result = "<meta name=\"author\" content=\"" + author + "\"" "/>" + "\n"
  return result

def generate_title(title):
  result = generate_html_tag("title", False, False)
  result = result + title + generate_html_tag("title", True, True)
  return result
