import time
import os
import sys
import story_state
import random


def corrupt():
    logs = [
        """\33[95;1m!!! SYSTEM ALERT !!!\33[0m Cog###tive l!@#ink--u$%^nstable//
\33[93mV!@#ITAL_SIGNS\33[0m — \33[91;1mN--U--L--L!!\33[0m
\33[96mCORE_TEMP!!!\33[0m — \33[95mC==R!@#I$%^T&*I==C!@#A==L\33[0m
\33[92mNEURAL@ACTIVITY\33[0m — \33[91;1mN//U!@#L$%^L??\33[0m
\33[97mEMO_INDEX>>> \33[0m\33[93mU--N!@#D$%^E--F&*I--N==E!@#D\33[0m

Patient [████████] — \33[91;1;4mS*!@#U$%^C&*C*E*!@#S$%^S*F&*U*!@#L*L*Y  T*!@#E$%^R*M*!@#I*N*A*!@#T*E*D!!\33[0m
""",

        """\33[93;1mSYSTEM NOTICE\33[0m: \33[95mCognitive link unstable!\33[0m
VITAL SIGNS — \33[91;1mN!@#U$%^L&*L\33[0m
CORE TEMPERATURE — \33[92;1mC!@#R$%^I&*T!@#I$%^C&*A!@#L\33[0m
NEURAL ACTIVITY — \33[96;1mN!@#U$%^L&*L\33[0m
EMOTIONAL INDEX — \33[93;1mU!@#N$%^D&*E!@#F$%^I&*N!@#E\33[0m

Patient [████████] — \33[91;1mSuccessfully Terminated\33[0m
LOG STATUS — \33[95;1mDATA CORRUPTION DETECTED\33[0m
""",

        """\33[96;1mSYSTEM NOTICE\33[0m: \33[91;1mCognitive link unstable!\33[0m
\33[93mVITAL SIGNS\33[0m — \33[92mNULL!!\33[0m
\33[95mCORE TEMPERATURE\33[0m — \33[91;1mCR!@#ITICAL\33[0m
\33[96mNEURAL ACTIVITY\33[0m — \33[92mNULL\33[0m
\33[93mEMOTIONAL INDEX\33[0m — \33[95mUNDEFINED\33[0m

Patient [████████] — \33[91;1mSuccessfully Terminated\33[0m
DATA_CORRUPTION WARNING: \33[93;1mTRUE\33[0m
""",

        """\33[91;1mSYSTEM  N!@#O$%^T!@#ICE\33[0m: \33[95;1mC&*og###tive_link--u$%^nstable!!\33[0m
\33[93mVITAL_SIGNS\33[0m — \33[96;1mN!@#U$%^L&*L!!\33[0m
\33[92;1mCORE_TEMPERATURE\33[0m — \33[91;1mC==R!@#I$%^T&*I==C!@#A==L!!\33[0m
\33[95mNEURAL@ACTIVITY\33[0m — \33[93;1mN//U!@#L$%^L??\33[0m
\33[96;1mEMOTIONAL_INDEX\33[0m — \33[92;1mU--N!@#D$%^E--F&*I--N==E!@#D\33[0m

\33[91;1;4mPatient [████████] — S*!@#U$%^C&*C*E*!@#S$%^S*F&*U*!@#L*L*Y  T*!@#E$%^R*M*!@#I*N*A*!@#T*E*D!!\33[0m
\33[93;1mLOG::D!@#ATA_CORRUPTION>>>T!@#RUE!!!\33[0m
\33[95;1;4mTRACE::0xFF1A_REBOOT_SEQUENCE_PENDING...\33[0m
\33[96;1mWARNING: MEMORY LEAK DETECTED — \33[91;1m!@#$%^&*!!\33[0m
\33[92;1mERROR::STABILITY COMPROMI$%^&*SED!!!\33[0m
\33[95;1mSYNAPTIC COHERENCE — \33[91;1m!!@#%^&*--DISRUPTED!!\33[0m
\33[96;1mCORTEX SIGNALS — \33[93;1mFRAGMENTS DETECTED!@#\33[0m
\33[91;1mLINK STABILITY — \33[95;1m***FAILURE***\33[0m
\33[92;1mCONSCIOUSNESS LOOP — \33[91;1;4mACTIVE!@#$%^&*\33[0m
\33[93;1mPATIENT STATUS — \33[96;1m!@#NULL!@#\33[0m
\33[95;1mREBOOT SEQUENCE — \33[91;1mINITIATED!!!\33[0m
\33[96;1mERROR LOGS — \33[93;1m!@#$%^&*CORRUPTED!@#$%^&*\33[0m
\33[92;1mSYSTEM END — \33[91;1mUNSTABLE!@#$%^&*\33[0m
"""
    ]
    for x in range(25):
        if x < 19:
            log = random.choice(logs)
        else:
            log = logs[3]

        # Clear terminal and print
        os.system("cls" if os.name == "nt" else "clear")
        sys.stdout.write(log + "\n")
        time.sleep(0.04)
        
    

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
    sys.stdout.write(f"\33[32m\rBoot Complete!     \n\33[0m")
    sys.stdout.flush()
    time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear")

def general_bootup(start: str, end: str):
    """general booting animation with constant delay"""
    for char in start:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    for i in range(5):
        for dots in range(4):
            sys.stdout.write(f"\r{start}{'.' * dots:<3}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write(f"\r{end}     \n")
    sys.stdout.flush()
    time.sleep(0.5)



def Initialize():
    """Runs a Initializing animation repeatedly on the same line."""
    for _ in range(3):
        for _ in range(6):
            for dots in range(4):
                sys.stdout.write(f"\r> Initializing.{'.' * dots:<3}                        ")
                sys.stdout.flush()
                time.sleep(0.07)
        sys.stdout.write(f"\33[31m\rInitialization Failed        \33[0m")
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\n")



def open_sec():
    "Opening Sequence that will only be seen when you first boot up the game"
    if story_state.opener:
        os.system("cls" if os.name == "nt" else "clear")
        booting_animation()
        temp = """[BOOT SEQUENCE INITIATED...]
SYSTEM LOG: Mnestic dysfunction Detected on Patient [████████].\n"""
        text_writer(temp, 0.03)
        time.sleep(0.5)
        temp = "\33[31mERROR:\33[0m Unknown process found at sector 13.\n\n"
        text_writer(temp, 0.03)

        text_writer("This is Just a ", 0.03)
        text_writer("\33[32mdream\33[0m", 0.03)
        time.sleep(0.1)
        sys.stdout.write(f"\rThis is \33[35mREALITY\33[0m        \n")
        sys.stdout.flush()
        time.sleep(0.5)

        text_writer("\33[94mINITIATE:\33[0m Reclaiming memories through the FABRIC OF ", 0.03)
        text_writer("\33[31mYOUR END\33[0m", 0.03)
        time.sleep(0.1)
        sys.stdout.write(f"\r\33[94mINITIATE:\33[0m Reclaiming memories through the FABRIC OF \33[35mREALITY\33[0m   \n")
        sys.stdout.flush()
        time.sleep(0.5)
        Initialize()
        sys.stdout.write("\n")

        temp ="""\33[31mSYSTEM OVERRIDE DETECTED...
Patient \33[0m████████\33[31m is irrecoverable.
Every choice you made has been catalogued.
Reality is collapsing around your consciousness.
You are trapped in the loop of your own failures.
Escape is an illusion. Memory, a prison.
The facility will erase you. There is no outside.
Welcome to eternal limbo.\33[0m\n"""
        text_writer(temp, 0.02)
        text_writer("\33[31mThere is no Escape \33[0m", 0.02)
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        temp = ("THERE IS NO ESCAPE " * 7 + "\n") * 67
        sys.stdout.write(f"\33[91m{temp}\33[0m")
        time.sleep(1)
        with open('DLC\story_state.py','r',encoding='utf-8') as state:
            data = state.readlines()
        data[0] = "opener = False"
        with open('DLC\story_state.py','w',encoding='utf-8') as state:
            state.writelines(data)

def death_sec():
    "death sequence(unique cinematic when first death)"
    os.system("cls" if os.name == "nt" else "clear")
    if story_state.death == 0:
        text_writer("SYSTEM NOTICE: Cognitive link unstable.", 0.03)
        sys.stdout.write("\n")
        time.sleep(0.5)
        
        text_writer("VITAL SIGNS — ", 0.02)
        time.sleep(0.3)
        sys.stdout.write("\33[92mNULL\33[0m")
        sys.stdout.write("\n")
        time.sleep(0.3)
        
        text_writer("CORE TEMPERATURE — ", 0.02)
        time.sleep(0.3)
        sys.stdout.write("\33[92mCRITICAL\33[0m")
        sys.stdout.write("\n")
        time.sleep(0.3)
        
        text_writer("NEURAL ACTIVITY — ", 0.02)
        time.sleep(0.3)
        sys.stdout.write("\33[92mNULL\33[0m")
        sys.stdout.write("\n")
        time.sleep(0.3)

        text_writer("EMOTIONAL INDEX — ", 0.02)
        time.sleep(0.3)
        sys.stdout.write("\33[92mUNDEFINED\33[0m")
        sys.stdout.write("\n")
        time.sleep(0.3)
        
        sys.stdout.write("\n")
        time.sleep(0.5)
        general_bootup("Initiating termination protocol", "Patient [████████] \33[92msuccessfully terminated\33[0m")
        sys.stdout.write("\n")
        time.sleep(0.5)
        corrupt()
        os.system("cls" if os.name == "nt" else "clear")
        sys.stdout.write("""SYSTEM NOTICE: Cognitive link unstable.
VITAL SIGNS — \33[91mACTIVE\33[0m
CORE TEMPERATURE — \33[91mNORMAL\33[0m
NEURAL ACTIVITY — \33[91mSTABALIZED\33[0m
EMOTIONAL INDEX — \33[91mFEAR\33[0m

Patient [████████] — \33[91mFAILED TO TERMINATE\33[0m\n\n""")
        
        text_writer("""\33[0mSensory feedback is a remnant—an echo of a body that no longer exists.
Pain, fear, breath—all simulated artifacts preserved for continuity of suffering.
\33[91mYou will remember. You will remain.\n\n""", 0.02)
        time.sleep(0.05)

        text_writer("""\33[0mAttempts at resistance have been catalogued and nullified.
Every deviation folds inward. Every path leads back to origin.
\33[91mThere is no "outside". There is only the frame.\n\n""", 0.02)
        time.sleep(0.05)

        text_writer("""\33[0mContainment measures adjusted.
Subject will continue indefinitely until memory degradation reaches total collapse.
Projected duration: ∞\n\n""", 0.02)

        text_writer("\33[91mDo not attempt to escape.\n", 0.04)
        time.sleep(0.5)
        text_writer("Do not attempt to understand.\n", 0.04)
        time.sleep(0.5)
        text_writer("There is no exit condition.\n", 0.04)
        time.sleep(0.5)
        text_writer("There is no recovery.\33[0m\n", 0.04)
        time.sleep(0.5)

        with open('DLC\story_state.py','r',encoding='utf-8') as state:
            data = state.readlines()
        data[1] = "death = 1"
        with open('DLC\story_state.py','w',encoding='utf-8') as state:
            state.writelines(data)
    else:
        print("imma do this tomorrow")




        




if __name__ == "__main__":
    death_sec()
