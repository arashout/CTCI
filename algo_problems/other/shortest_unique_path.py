import sys;

class CustomNode:
    def __init__(self, Title, Parent):
        self.Title = Title
        self.Parent = Parent
        self.Children = []
        
        if Parent is not None:
            Parent.Children.append(self)
    
    def Find(self, path):
        if path == self.Title:
            return self
        
        for child in self.Children:
            if (child.Title==path.split('/')[1]):
                return child.Find(path.split('/', 1)[1])

def Main():
    root = CustomNode("Root", None)
    userData = CustomNode("UserData", root)
    ud_browser = CustomNode("Browser", userData)
    ud_word = CustomNode("Word", userData)
    priv = CustomNode("Private", userData)
    priv_word = CustomNode("Word", priv)
    
    windows = CustomNode("Windows", root)
    programs = CustomNode("Programs", root)
    notepad = CustomNode("Notepad", programs)
    prog_word = CustomNode("Word", programs)
    prog_browser = CustomNode("Browser", programs)
    
    custom1 = CustomNode("Custom1", root)
    custom2 = CustomNode("Custom2", custom1)
    custom3 = CustomNode("Custom3", custom2)

    RunTests(root, custom1, custom2, custom3);

def TestGetShortestUniqueQualifier(root, targetAbsPath, expected):
    try:
        output = GetShortestUniqueQualifier(root, root.Find(targetAbsPath))
    except ValueError as e:
        print(e)
        output = "exception"

    if output == expected or (expected is None and output == ""):
        print("Succeeded for " + targetAbsPath)
    else:
        print("Failed for " + targetAbsPath + ": Failed with [" + ("" if output is None else output) + "] rather than [" + ("" if expected is None else expected) + "]")

def RunTests(root, custom1, custom2, custom3):

    #They are unique
    TestGetShortestUniqueQualifier(root, "Root", "Root")
    TestGetShortestUniqueQualifier(root, "Root/Programs", "Programs")
    TestGetShortestUniqueQualifier(root, "Root/Programs/Notepad", "Notepad")
	    
    #They have duplicate names
    TestGetShortestUniqueQualifier(root, "Root/Programs/Browser", "Programs/Browser")
    TestGetShortestUniqueQualifier(root, "Root/UserData/Browser", "UserData/Browser")

    #Root has a duplicate name
    custom1.Title = "a"
    custom2.Title = "b"
    custom3.Title = "Root"
    TestGetShortestUniqueQualifier(root, "Root/a/b/Root", "b/Root")

    #Edge cases
    custom1.Title = "Root"
    custom2.Title = "b"
    custom3.Title = "c"
    TestGetShortestUniqueQualifier(root, "Root/Root", "Root/Root")

    custom1.Title = "a"
    custom2.Title = "a"
    custom3.Title = "a"
    TestGetShortestUniqueQualifier(root, "Root/a", "Root/a")
    TestGetShortestUniqueQualifier(root, "Root/a/a", "Root/a/a")
    TestGetShortestUniqueQualifier(root, "Root/a/a/a", "a/a/a")

    custom1.Title = "Root"
    custom2.Title = "UserData"
    custom3.Title = "Word"
    TestGetShortestUniqueQualifier(root, "Root/Root/UserData/Word", "Root/Root/UserData/Word")

    TestGetShortestUniqueQualifier(root, "Root", "/Root")
    TestGetShortestUniqueQualifier(root, "Root/UserData/Word", "/Root/UserData/Word")

def GetShortestUniqueQualifier(root, target):
    def findAll(n, current_path, _found):
        if current_path == '':
            parent_path = ''
        else:
            parent_path = current_path + '/'
        if n.Title == target.Title:
            _found[n] = parent_path + n.Title

        for c in n.Children:
            findAll(c, parent_path + n.Title, _found)
        
        return _found

    def reduce(_found, i):
        if len(_found) == 1:
            return i - 1
        
        split_target = _found[target].split('/')
        if len(split_target) < i:
            return i
            
        target_fragment = _found[target].split('/')[-i]
        to_remove = {}

        for n, ab_path in _found.items():
            path_split = ab_path.split('/')
            if i > len(path_split):
                to_remove[n] = True
            else:
                if path_split[-i] != target_fragment:
                    to_remove[n] = True
        
        for n in to_remove.keys():
            _found.pop(n)
        
        return reduce(_found, i + 1)

    found = findAll(root, '', {})
    if len(found) == 1:
        return target.Title

    target_abs_path = found[target]
    split_path = target_abs_path.split('/')

    j = reduce(findAll(root, '', {}), 1)
    t = len(split_path)
    s = t - j
    if s == -1:
        return target_abs_path

    shortest = '/'.join(split_path[s:])
    return shortest


Main()
