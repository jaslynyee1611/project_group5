# import Path from pathlib into filetouch.py
from pathlib import Path

def create(files):
    """
    this function will create a file with the name as the paranthesis
    """
    # create a file with the assigned file as the parenthesis of the function 
    fp_write = Path.cwd() / files
    # use .touch() to create the files into the file path, fp_write 
    fp_write.touch()
    