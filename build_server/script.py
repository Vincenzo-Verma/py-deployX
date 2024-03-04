import os
import dotenv
 
os.system(" ")
def init():
    _home = os.system("cd ~")
    _cwd = os.getcwd()
    if _cwd != '/home/__output':
        os.system("cd ~/__output")
    os.system(f'''git clone {GIT_URL} && cd "$(basename "$_" .git)" && npm install && npm run build''')
    print(os.getcwd())


if  __name__ == '__main__':
    print("Exexuting Script.py")
