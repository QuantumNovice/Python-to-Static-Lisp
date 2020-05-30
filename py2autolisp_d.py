import subprocess
import re


class LISPit:
    def __init__(self):
        self.LISP = ''
        self.raw = []

    def print(self, string):
        self.raw.append( '(print "{}")'.format(string) )


    @property
    def run(self):
        """
        Runs LISP in CLISP
        """
        fd = open('temp.lsp','w')
        self.LISP = '\n'.join([i for i in self.raw])
        fd.write(self.LISP)
        fd.close()
        return  subprocess.check_output('clisp temp.lsp').decode('utf-8')


a = LISPit()
for i in range(10):
    a.print('hello')
    
print(a.run)    
print(a.LISP)




