import pandas as pd
import numpy as np

if __name__ == '__main__':
    
    class display(object):
        def __init__(self, *args):
            self.args = args
        def _repr_html_(self):
            return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                             for a in self.args)
        def __repr__(self):
            return '\n\n'.join(a + '\n' + repr(eval(a))
                               for a in self.args)

# One - to - One Joins

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
'group': ['Accounting', 'Engineering',
'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
'hire_date': [2004, 2008, 2012, 2014]})

print(display('df1', 'df2'))

print('='*64)

df3 = pd.merge(df1, df2)
print(df3)

print('='*64)

# Many - to - One Joins

df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
'supervisor': ['Carly', 'Guido', 'Steve']})
print(display('df3', 'df4', 'pd.merge(df3, df4)'))

print('='*64)

print(pd.merge(df3, df4))

print('='*64)

# Many-to-Many Joins

df5 = pd.DataFrame({'group': ['Accounting', 'Accounting',
'Engineering', 'Engineering', 'HR', 'HR'],
'skills': ['math', 'spreadsheets', 'software', 'math',
'spreadsheets', 'organization']})
print(display('df1', 'df5', "pd.merge(df1, df5)"))

print('='*64)

print(pd.merge(df1, df5))






