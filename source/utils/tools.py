from spire.doc import *
from spire.doc.common import *
import logging

def get_paragraphs(doc, section_n: int, paragraph_n: int):
  """
  Get document paragraph 

  Args:
    doc: Spire document object
    section_n: Section number
    paragraph_n: Paragraph number

  Returns:
    Spire paragraph object
  """
  try:
    section = doc.Sections.get_Item(section_n)
    paragraph = section.Paragraphs.get_Item(paragraph_n)
    return paragraph
  
  except Exception as e:
    logging.error(f"[Get paragraph] error while retrieving paragraph: {str(e)}")
    return None

def extract_structured_spire_content(doc) -> str:
  """
  Extract text from docx with spire structure

  Args:
    doc: Spire document object

  Returns:
    str: Text content of the document
  
  """
  content = ""
  
  try:
    logging.info(f"[Extract doc content] Extracting content of the file")
    for section_n in range(doc.Sections.Length):
      section = doc.Sections.get_Item(section_n)

      for paragraph_n in range(section.Paragraphs.Length):
        para = section.Paragraphs.get_Item(paragraph_n)

        content += f"Section number: {section_n}, paragraph number: {paragraph_n}, content: " + para.Text + "\n"

  except Exception as e:
    logging.error(f"[Extract doc content] Failed extracting content of the file: {str(e)}")
  
  return content

def add_comment(doc, paragraph, comments: str, id_comments: int, author: str = "Annotator-tool") -> None:
  """
  Add comment to a spire paragraph

  Args:
    doc : spire document object
    paragraph: Spire paragraph object
    comments (str): conmment content
    id_comments (int): comment id
    author (str): comment author

  Returns:
    None
  
  """
  try:
    # Add a comment to the paragraph
    comment = paragraph.AppendComment(comments)

    # Set the author of the comment
    comment.Format.Author = author

    # Create a comment start mark and an end mark and set them as the start and end marks of the created comment
    commentStart = CommentMark(doc, CommentMarkType.CommentStart)
    commentEnd = CommentMark(doc, CommentMarkType.CommentEnd)
    commentStart.CommentId = comment.Format.CommentId
    commentEnd.CommentId = comment.Format.CommentId

    # Insert the comment start mark and end mark at the beginning and end of the paragraph respectively
    paragraph.ChildObjects.Insert(id_comments, commentStart)
    paragraph.ChildObjects.Add(commentEnd)
    
  except Exception as e:
    print(f"[Tools] issue while adding comments")


def save_file(file_bytes: bytes, temp_file_name: str) -> str:
  with open(temp_file_name, "wb") as fb:
    fb.write(file_bytes)


def main_annotator(doc, agent_comments: dict):
  """
  Main annotator function

  Args:
    doc : File bytes
    agent_comments (dict): Agent comments

  Returns:
    None
  """

  for comment in agent_comments:
    para_n = comment["paragraph_number"]
    sec_n = comment["section_number"]
    content = comment["content"]
    id_comment = para_n + sec_n

    para = get_paragraphs(doc, sec_n, para_n)
    
    if para is not None:
      add_comment(doc, para, content, id_comment)
    
