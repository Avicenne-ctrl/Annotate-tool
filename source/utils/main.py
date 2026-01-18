from source.utils.agent import call_mistral_agent
from source.utils.prompt import user_prompt
from source.utils.tools import extract_structured_spire_content, main_annotator, save_file

from spire.doc import *
from spire.doc.common import *

import os
import logging

def main(file_bytes: bytes, file_name: str, query: str):
    """Main function to annotate a file

    Args:
        file_bytes (bytes): bytes file content
        file_name (str): name of the file
        query (str): query of the user regarding the file
    """
    try:
        save_file(file_bytes, file_name)
        
        doc = Document()
        doc.LoadFromFile(file_name)
        
        full_content = extract_structured_spire_content(doc)
        
        if full_content:
            user_query = user_prompt(query, full_content)
            
            mistral_resp = call_mistral_agent(user_query)
            main_annotator(doc, mistral_resp)
        
        os.remove(file_name)
        # Save the document
        doc.Close()
        
    except Exception as e:
        logging.error(f"[Main workflow] Issue occurs: {str(e)}")