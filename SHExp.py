# Modules
from glob import glob
from os import getcwd, system, path, chdir
from fnmatch import filter
from platform import system as OS

# Force CWD
chdir(getcwd())

# UI 
class UI:
    def Line(Character):
        for _ in range(75): print(Character, end='')
        print()                   

# Explorer
def Explorer():
    print("\n Shell Explorer")    
    UI.Line('=')
    if str(glob('*')) != '[]':
        for Item in glob("*"):
            Whitespaces = ''
            if path.isfile(path.abspath(Item)): 
                Type = f'{path.splitext(Item)[1]} File'.strip()
                Icon = '#'
            elif path.isdir(path.abspath(Item)):
                Type = 'File Folder'  
                Icon = '>' 
            if len(Item) > 50: Output=f"{Icon} {Item[:50]}... | {Type}"
            elif len(Item) < 50:
                Length=53-len(Item)
                for _ in range(Length): Whitespaces += ' '
                Output=f"{Icon} {Item}{Whitespaces} | {Type}"
            Whitespaces = ''
            print(Output)
    else: print('~ |Empty Directory|')           
    UI.Line('=')    
    print(f'\nPath: {getcwd()}\n')
    print("[ Go | Back ]\n")

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
        case 'back': 
            try:
                for _ in range(int(Command[1])):
                    chdir(path.abspath(path.dirname(getcwd())))
            except: chdir(path.abspath(path.dirname(getcwd())))       
     
# Main
if __name__ == '__main__':
    while True:
        if OS() == 'Windows': system('cls')
        else: system('clear')    
        Explorer()
        try: Command()
        except: exit()