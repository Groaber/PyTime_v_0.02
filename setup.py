from cx_Freeze import setup, Executable
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = "Win32GUI"  # pour application graphique sous Windows
#base = "Console" # pour application en console sous Windows

options = {
    'build_exe': {
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ],
    },
}

setup(name = "Pytime" ,
  options={"build_exe": {"packages":["pygame"],"include_files":["person.py", "obstacle.py"]}},
  version = "0.0.0.1",
  author="SONNECK",
  description = "Game" ,
  executables=[Executable('main.py',base=base)]
)
