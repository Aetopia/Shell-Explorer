from glob import glob
from os import getcwd, path, chdir
from fnmatch import filter
from subprocess import run

def Main():
    run('cls', shell=True)
    for _ in range(100): print('=', end='')
    print() 
    if str(glob('*')) != '[]':
        for Item in glob("*"):
            Whitespaces = ''
            if path.isfile(path.abspath(Item)): 
                Type = f'{path.splitext(Item)[1]} File'.strip()
                Icon = '#'
            elif path.isdir(path.abspath(Item)):
                Type = 'File Folder'  
                Icon = '>' 
            if len(Item) > 70: Output=f"{Icon} {Item[:70]}... | {Type}"
            elif len(Item) < 70:
                Length=73-len(Item)
                for _ in range(Length): Whitespaces += ' '
                Output=f"{Icon} {Item}{Whitespaces} | {Type}"
            Whitespaces = ''
            print(Output)
    else: print('~ |Empty Directory|')           
    for _ in range(100): print('=', end='')
    print() 
    print('\nDrives:', end='')
    for Drive in range(96,123):
        if path.exists(path.abspath(f'{chr(Drive)}:/')):
            print(f' {path.abspath(f"{chr(Drive)}:/")}'.title(), end='')
    print()        
    print(f'\nPath: {path.abspath(getcwd())}\n')
    print("[ Go | Back | Path | Exit ]\n")
    Command = input("-> ").strip().split(' ',1)
    match Command[0].lower():
        case 'go':
            Folder = None
            try:
                for Folder in (filter(glob('*'), f'{Command[1]}*')):
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
        case 'path':
            try:
                print()
                for Item in (filter(glob('*'), f'{Command[1]}*')):
                    if path.isdir(path.abspath(Item)): Icon = '>'
                    elif path.isfile(path.abspath(Item)): Icon = '#' 
                    print(f'{Icon} "{path.abspath(Item)}"') 
                print()    
                run('pause', shell = True) 
            except: pass
        case 'exit': exit(0)  
                   
if __name__ == '__main__':
    chdir(getcwd())
    while True:
        try: Main()
        except: exit(1)
