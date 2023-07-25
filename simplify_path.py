'''Given a string path, which is an absolute path (starting with a slash 
'/') to a file or directory in a Unix-style file system, convert it to the 
simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, 
a double period '..' refers to the directory up a level, and any multiple 
consecutive slashes (i.e. '//') are treated as a single slash '/'. For 
this problem, any other format of periods such as '...' are treated as 
file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory 
to the target file or directory (i.e., no period '.' or double period 
'..')
Return the simplified canonical path.'''

import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.split(r'/{1,}', path)
        path = [x for x in path if len(x) >= 1]
        print(path)
        ans = []
        for directory in path:
            if directory == '.':
                continue
            elif directory == '..'  :
                if len(ans)>0:
                    ans.pop()
            else:
                ans.append(directory)
        print(ans)
        ans = '/'.join(ans)
        return f'/{ans}'
