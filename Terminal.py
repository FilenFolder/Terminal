import time
import os
import subprocess
import shutil
import ctypes
A = True
B = True
Cmd = ''
Lastcmd = ''
CPUCHECK = True


def clear():
   os.system('cls' if os.name == 'nt' else 'clear')


def on_ready():
   print('Opening...')
   time.sleep(3)
   clear()
   time.sleep(2)
   print('Terminal V1 Beta, Made by Delacc/filenfolder/yahya, inspired by command promt WINDOWS MICROSOFT')
   time.sleep(1) 
   print('Made With Python')
   time.sleep(1) 
   print('© Terminal Coperation, All have rights reserved')
   print(' ')
   

def maximize_console():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(hwnd, 3)  # 3 is SW_MAXIMIZE

import ctypes

def restore_window():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        # Restore the window to its original size
        ctypes.windll.user32.ShowWindow(hwnd, 9)  # 9 is SW_RESTORE
        # Optionally set a default window size and position
        ctypes.windll.user32.SetWindowPos(hwnd, -1, 100, 100, 800, 600, 0x0040 | 0x0001)  # Set to 800x600 window size


import ctypes

def fullscreen_console():
    # Get the console window handle
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()

    # Maximize the console window
    ctypes.windll.user32.ShowWindow(hwnd, 3)  # SW_MAXIMIZE

    # Set the window style to hide borders and taskbar
    style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)  # GWL_STYLE
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, style & ~0x00C00000)  # WS_CAPTION
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, style & ~0x00080000)  # WS_SYSMENU
    ctypes.windll.user32.SetWindowPos(hwnd, 0, 0, 0, 0, 0, 0x0001 | 0x0002 | 0x0004)  # SWP_NOMOVE | SWP_NOSIZE | SWP_NOZORDER | SWP_SHOWWINDOW

on_ready()

while A:
 import ctypes; ctypes.windll.kernel32.SetConsoleDisplayMode(ctypes.windll.kernel32.GetStdHandle(-11), 1, None)
  

 Cmd = input('>>>Terminal : ')
 if Cmd == 'show':
    LastCmd = Cmd
    Cmd = input('>')
    time.sleep(0.5)
    print(Cmd)
    LastCmd = Cmd

 elif Cmd == 'Login user_id':
    LastCmd = Cmd
    Cmd = int(input('>'))
    if Cmd == '12345678901234567890':
      LastCmd = Cmd
      print('WIP!')

    elif Cmd == '1157273511019151391':
       print('WIP!')
       LastCmd = Cmd

    else:
       LastCmd = Cmd
       print('WIP')

    
 elif Cmd == 'exit_terminal':
      LastCmd = Cmd
      leave = input('Are you sure ? (y/n): ')
      if leave == 'y':
       time.sleep(1)
       break
      elif leave == 'n':
       print('Loading...')
       print(' ')
       
      else:
       print('Please either say y/n')
       print(' ')


 elif Cmd == 'make':
      LastCmd = Cmd
      Cmd = input('>')
      if Cmd == 'folder':
          LastCmd = Cmd
          name3 = input('>>')
          import os; os.makedirs(os.path.join('C:\\Users\\User\\Desktop',name3), exist_ok=True)
          LastCmd = Cmd
          print(' ')
 
 elif Cmd == 'disk_usage':
    total, used, free = shutil.disk_usage("/")
    print(f"Total: {total // (2**30)} GiB")
    print(f"Used: {used // (2**30)} GiB")
    print(f"Free: {free // (2**30)} GiB")
    print(' ')
  
 elif Cmd == 'clear':
    clear()

 elif Cmd == 'help':
    print(' ')
    print('Looks like you need help')
    print('The commands are : ')  
    print('show : its gonna show anything you type')
    print('Login user_id : WORK IN PROGRESS AND could f*ck your whole computer up')
    print('bot.run name_id : Only creator could use it')
    print('make : it will make a folder if you type folder next (works only in Creator...)')
    print("exit_terminal : ....i shouldn't really explain it")
    print('disk_usage : yeahhh...it will just show your disk usages... :l')
    print('clear : it will clear your Output')
    print('CPU_check : is your PC slow, just type this')
    print('there are also fullscreen_on,fullscreen_off / maximize_on, maximize_off')
    print('open : it will open a file if you typed a path, it is still work in progress so it will kinda break the code :l')
    print(' ')
 
 elif Cmd == 'fullscreen_on':
    fullscreen_console()
 
 elif Cmd == 'maximize_on':
    maximize_console()

 elif Cmd == 'fullscreen_off':
    restore_window()
 
 elif Cmd == 'maximize_off':
    restore_window()
    
 elif Cmd == 'CPU_check':
    CPU = {subprocess.check_output('wmic cpu get loadpercentage', shell=True).decode}
    print(f"CPU Usage: {subprocess.check_output('wmic cpu get loadpercentage', shell=True).decode().strip().split()[1]}%, Processor: {subprocess.check_output('wmic cpu get name', shell=True).decode().strip().split('\n')[1].strip()}")
    time.sleep(1)
    if CPUCHECK:
     print(' ')
     print('if the CPU was < 30, Your CPU is good') 
     print("if your CPU was > 70, your CPU is getting higher, please end some task manager and apps, if that dosn't work, please restart your computer")
     print("if your CPU was between 30 and 70, its the normal CPU (for me...Delacc, and i have a crappy Computer)")
     print(' ')
     CPUCHECK = False

    else:
     CPUCHECK = False  
 
 elif Cmd == 'open':
    LastCmd = Cmd
    Cmd = input('>')
    LastCmd = Cmd
    open(Cmd, 'r')
 
 elif Cmd == 'txt':
    LastCmd = Cmd
    Cmd = input('>')
    LastCmd = Cmd
 elif Cmd == 'shutdown -l':
    system('shutdown \l \t 0')
    
    
 else:
    print(f'Command "',Cmd,'" Unknown...type "help" if your stuck')