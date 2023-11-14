import ast, re

def remove_comments_and_docstrings(code):
    # Remove single-line comments and strings that are used as comments
    code = re.sub(r'(?m)^\s*(#.*|\'[^\']*\'|"[^"]*")\s*$', '', code)
    
    # Remove multi-line comments and docstrings
    code = re.sub(r'(?s)(\'\'\'.*?\'\'\')|(""".*?""")', '', code)
    return code

def regular(code):
    return ast.unparse(ast.parse(code))

def regularize(code):
    code = regular(code)
    code = remove_comments_and_docstrings(code)
    return code

def get_stmt_list(code):
    return code.split('\n')