import os
import subprocess
import time

class Outils:
    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def clear_console_better():
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

    @staticmethod
    def pause(secondes: int):
        time.sleep(secondes)


print("Extinction dans 2 secondes")

Outils.pause(2)

Outils.clear_console_better()
