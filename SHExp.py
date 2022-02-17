# Modules
from glob import glob
from os import getcwd, system, path, chdir
from subprocess import run
from fnmatch import filter

# UI 
class UI:
    def Line(Character):
        for _ in range(100): print(Character, end='')
        print()                   

# Explorer
def Explorer():
    print("\n |■| Shell Explorer")    
    UI.Line('_')
    if str(glob('*')) != '[]':
        for Item in glob("*"):
            Whitespaces=''
            if path.isfile(path.abspath(Item)): 
                Type=f'{path.splitext(Item)[1]} File'.strip()
                Icon = '#'
            elif path.isdir(path.abspath(Item)):
                Type='File Folder'  
                Icon = '>' 
            if len(Item) > 50: Output=f"{Icon} {Item[:50]}... | {Type}"
            elif len(Item) < 50:
                Length=53-len(Item)
                for _ in range(Length): Whitespaces+=" "
                Output=f"{Icon} {Item}{Whitespaces} | {Type}"
            Whitespaces=''
            print(Output)
    else: print('~ |Empty Directory|')           
    UI.Line('‾')    
    print(f'Path: {getcwd()}')
    print(""" ___________       
| Go | Back |
 ‾‾‾‾‾‾‾‾‾‾‾""")

# Toolbar
def Command():
    Command = input("Command > ").strip().split(' ',1)
    match Command[0].lower():
        case 'go':
            Folder = None
            try:
                for Folder in (filter(glob('*'),f'{Command[1]}*')):
                    if path.isdir(path.abspath(Folder)):
                        Folder = Folder
                        break
                if Folder is None: Folder = Command[1]
            except: pass
            try: chdir(path.abspath(Folder))
            except: pass
        case 'back': chdir(path.abspath(path.dirname(getcwd())))
     
# Main
if __name__ == '__main__':
    while True:
        try: system('cls')
        except: system('clear')    
        Explorer()
        try: Command()
        except: exit()