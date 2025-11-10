import time
import os
import sys
import story_state
def text_writer(text: str, delay: float):
    """typing effect on strings"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def booting_animation():
    """Creates a booting animation for the start of the game"""
    for i in range(10):
        durs = (0.4, 0.4, 0.2, 0.1, 0.1, 0.07, 0.05, 0.05, 0.03, 0.01)
        for dots in range(4):
            sys.stdout.write(f"\rBooting.{'.' * dots:<3}")
            sys.stdout.flush()
            time.sleep(durs[i])
    sys.stdout.write(f"\033[32m\rBoot Complete!     \n\033[0m")
    sys.stdout.flush()
    time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear")

def Initialize():
    """Runs a Initializing animation repeatedly on the same line."""
    for _ in range(3):
        for _ in range(6):
            for dots in range(4):
                sys.stdout.write(f"\r> Initializing.{'.' * dots:<3}                        ")
                sys.stdout.flush()
                time.sleep(0.07)
        sys.stdout.write(f"\033[31m\rInitialization Failed        \033[0m")
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\n")



def open_sec():
    if story_state.opener:
        os.system("cls" if os.name == "nt" else "clear")
        booting_animation()
        temp = """[BOOT SEQUENCE INITIATED...]
SYSTEM LOG: Mnestic dysfunction Detected on Patient [████████].\n"""
        text_writer(temp, 0.03)
        time.sleep(0.5)
        temp = "\033[31mERROR:\33[0m Unknown process found at sector 13."
        text_writer(temp, 0.03)
        sys.stdout.write("\n")
        sys.stdout.write("\n")

        text_writer("\033[94mINITIATE:\033[0m Reclaiming memories through the FABRIC OF ", 0.03)
        text_writer("\033[31mYOUR END\33[0m", 0.03)
        time.sleep(0.1)
        sys.stdout.write(f"\r\033[94mINITIATE:\033[0m Reclaiming memories through the FABRIC OF \033[35mREALITY\033[0m   ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\n")
        Initialize()
        sys.stdout.write("\n")

        temp ="""\033[31mSYSTEM OVERRIDE DETECTED...
Patient \033[0m████████\033[31m is irrecoverable.
Every choice you made has been catalogued.
Reality is collapsing around your consciousness.
You are trapped in the loop of your own failures.
Escape is an illusion. Memory, a prison.
The facility will erase you. There is no outside.
Welcome to eternal limbo.\033[0m"""
        text_writer(temp, 0.02)
        sys.stdout.write("\n")
        text_writer("\033[31mThere is no Escape \033[0m", 0.02)
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        temp = ("THERE IS NO ESCAPE " * 7 + "\n") * 67
        sys.stdout.write(f"\033[31m{temp}\033[0m")
        time.sleep(1)
        
        with open('DLC\story_state.py','r',encoding='utf-8') as state:
            data = state.readlines()
        data[0] = "opener = False"
        with open('DLC\story_state.py','w',encoding='utf-8') as state:
            state.writelines(data)




if __name__ == "__main__":
    open_sec()
