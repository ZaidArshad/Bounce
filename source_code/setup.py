import sys
from cx_Freeze import setup, Executable

setup(
    name = "Bounce",
    executables = [Executable("bounce.py",icon = "gameicon.ico",base = "Win32GUI")]
    )
