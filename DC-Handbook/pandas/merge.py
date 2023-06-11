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


df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
'group': ['Accounting', 'Engineering',
'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
'hire_date': [2004, 2008, 2012, 2014]})

print(display('df1', 'df2', "pd.merge(df1, df2, on='employee')"))

print('='*64)

print(pd.merge(df1, df2, on='employee'))

print('='*64)

#The left_on and right_on Keywords

df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})

print(pd.merge(df1, df3, left_on="employee", right_on="name"))

print('='*64)

print(pd.merge(df1, df3, left_on="employee", right_on="name").drop('name', axis=1))
