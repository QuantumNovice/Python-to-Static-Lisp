import subprocess
import re
def run(lspcode):
    """
    Runs LISP in CLISP
    """
    fd = open('temp.lsp','w')
    fd.write(lspcode)
    fd.close()
    return  subprocess.check_output('clisp temp.lsp')

def py2lsp(pyline):
    if 'print' in pyline:
        pyline = pyline.replace('print','')
        pyline = list(pyline)
        pyline.insert(1, 'print ')
        pyline = ''.join([i for i in pyline])
        pyline = pyline.replace("'", "\"")
    if '=' in pyline:
        pyline = pyline.split('=')
        pyline = '(setq {} {})'.format(pyline[0], pyline[1])
        
    print(pyline)
    return pyline

def python2lisp(pycode):
    lines = pycode.split('\n')
    lspcode = []
    for line in lines:
        print('Py:', line)
        lspcode.append(py2lsp(line))
    return '\n'.join([i for i in lspcode])

lspcode = '''
(print "hello")
(print (+ 1 1 1 1))
'''
#run(lspcode)

pycode = '''
print('Hello World')
print("Hey Man")
x=1
print('x is :')
print(x)
1+1
'''
lspcode = python2lisp(pycode)
print("LISP:",lspcode)
print('LISP OUTPUT:')
print(run(lspcode).decode('utf-8'))
