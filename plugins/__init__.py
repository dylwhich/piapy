import os

# Import all .py files in this directory and invoke init() on them.
for file_ in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    fileext= os.path.splitext(file_)[1].replace(".","").lower()
    filename= os.path.splitext(file_)[0]
    if fileext == "py":
        mod = __import__(filename, globals(), locals())
