import json
from itertools import product
import platform
import sys
import os
####################################################################
DICTIONARY = open('DICTIONARY.json')
words = json.load(DICTIONARY)
wtypes=""
for i in words:
    wtypes=wtypes+":"+i
newF = None
rdF = None
Lin = None
rng = 1000
####################################################################
def setnums():
    words["number"]=["placeholder"]
    words["formnumber2"]=["placeholder"]
    words["formnumber3"]=["placeholder"]
    words["formnumber4"]=["placeholder"]
    words["formnumber5"]=["placeholder"]
    words["formnumber6"]=["placeholder"]
    words["formnumber7"]=["placeholder"]
    words["formnumber8"]=["placeholder"]
    words["formnumber9"]=["placeholder"]
words["number"]=[str(i) for i in range(rng)]
words["formnumber2"]=['{:>02d}'.format(i) for i in range(rng)]
words["formnumber3"]=['{:>03d}'.format(i) for i in range(rng)]
words["formnumber4"]=['{:>04d}'.format(i) for i in range(rng)]
words["formnumber5"]=['{:>05d}'.format(i) for i in range(rng)]
words["formnumber6"]=['{:>06d}'.format(i) for i in range(rng)]
words["formnumber7"]=['{:>07d}'.format(i) for i in range(rng)]
words["formnumber8"]=['{:>08d}'.format(i) for i in range(rng)]
words["formnumber9"]=['{:>09d}'.format(i) for i in range(rng)]
if platform.system() == 'Windows':
    clr = lambda: os.system('cls')
    os.system('color 04')
elif platform.system() == 'Linux':
    clr = lambda: os.system('clear')
def bnrO():
    sys.stdout.write("""
             
                       /)        (
             _________/')         ) 
            ()______ /'/         () 
             \ ~~~~~|' \        |--|
              \~~~~~\\' /\\       |  |           
      {==}     \~~~~~/   \      |  |            
     /    \     \_________\     '--'             
     |____|      ()_________)

__________________________________________codex.py__
""")
def bnrC():
    sys.stdout.write("""
    (\       
    ('\                          
     \\'\                        
     / '|                        
     \ '/                       |--|
       \                        |  |           
      {==}       __________     |  |            
     /    \     ()_________)    '--'             
     |____|      ()_________)

__________________________________________codex.py__
""")  
def mnu():
    sys.stdout.write("""
____________________________________________________
[$] Menu:

    (m)enu - Displays this menu.

    (b)anner - Displays the banner.
    
    (h)elp - Displays help and examples.
    
    (w)rite - Write a new file. (.txt/.rtf/.csv)

    (c)heck - Check a file for existing/improper words and remove them.
    
    (a)dd - Add words from a file (.txt/.rtf/.csv) to a new or existing list.

    (e)xit - Exits this tool.
    """)
def clihlp():
    sys.stdout.write("""
[?] Commands:\n
        (-h)elp | Gives this output.
------------------------------------------------------------------------------------
        (-w)rite | Writes a new File with the specified wordtypes.
            
            [?] If no path is given, the new text file is created in the same
                 directory that this script resides in.
              
                E.g.: 
                    -w /path/to/any/dir/newFilename.rtf color:animal:formnumber3
                    -w /wordlists/newFilename.txt color:noun:formnumber3
                    -w newFilename.txt verb:noun:number

            [?] If you wish to write one word, or two appended words, leave empty parameters.
                
                E.g.: [*] These all write the same thing
                    -w newFilename.txt number:: 
                    -w newFilename.txt :number:
                    -w newFilename.txt ::number

------------------------------------------------------------------------------------
        (-a)dd | Adds words from a specified file to the script's wordlists.
            
            [!] Files must have each line contain a single word.
            [!] If a word has " or \\ in it, this script will try to remove it.
                
                Acceptable:
                            word1
                            word2
                            word3
                            word4
                            word5

                Unacceptable:
                            "word1"
                            \word

            [!] Add can only add from one file at a time.

                E.g.: -a /path/to/wordlist/Words.txt <wordtype>
                    -a verbs.txt verbs
                    -a nouns.txt nouns

------------------------------------------------------------------------------------
        (-c)heck | Checks a file for words with unacceptable symbols and existing words.

            [!] Acceptable wordlists contain a single word in each line with no symbols.
                [?] Unacceptable Symbols: \\ and "
                                    
""")
def hlp():
    sys.stdout.write("""
____________________________________________________
[*] Args:| {} |

            [*] color - I.e. ["red", "yellow", "blue"]

            [*] adjective - I.e. ["small", "shiny", "pretty"]

            [*] animal - I.e. ["cat", "dog", "fish"]

            [*] noun - I.e ["banana", "race", "car"]

            [*] verb - I.e. ["jump", "run", "swim"]
                [*] "ing" is added to the end of most verbs

            [*] number - I.e. [""]

            [*] formnumber2 - I.e. [00, 01, 02, 03]

            [*] formnumber3 - I.e. [000, 001, 002, 003]
            
            [*] formnumber4 - I.e. [0000, 0001, 0002, 0003]
            (and so on... 9 max.)

[?] E.g.:\n 
            [?] color:animal:formnumber3  - #1,646,352 words.
                [*]Writes things like: redshark001 or greentiger999.

            [?] noun:noun:formnumber2  - #22,498,789 words.
                [*]Writes things like: roomservice02 or waterdamage999.

            [?] adj:noun:number  - #256,383,360 words.
                [*]Writes things like: poisonapple2 or ancientpalace123.

            [?] :number: will write one decimal: 1 ;

            [?] :formnumber2: - will write two decimals: 01 ;

            [?] :formnumber4: - #9999 integers.
                [*] Writes four-digit pins.

            [?] :formnumber9: - will write nine decimals: 000000001
            
""".format(wtypes))
def wrt():
    sys.stdout.write("[!] Writing a new file!\n")
    sys.stdout.write("""
____________________________________________________
[!] Enter the name of the file you'd like to create for your wordlist.
    [!*] If a file with that name already exists, it will be overwritten.
    [!*] Please refrain from using numbers in your filename.\n""")

    newF = input("[->] Filename-> ")
    sys.stdout.write("\n [!] Please enter the arguments in the order you would like to apply them to your wordlist.\n")
    sys.stdout.write("[*] Args:| color : adjective : animal : noun : verb : number : formnumber2-9 |\n")
    sys.stdout.write("[!] Please split your args with : like... 'color:animal:formnumber3'")
    args = input("[->] Args-> ")
    arg1, arg2, arg3 = args.split(':')
    rng = 1000
    rng = int(input("[->] Set integer's max (Default=1000)-> "))
    with open(newF, 'w') as f_out:
        sys.stdout.write("[*] Please wait while I write in "+newF+".\n")
        for c in product(words[arg1],words[arg2],words[arg3]):
            print(''.join(c), file=f_out)
    sys.stdout.write("[*] All finished!\n")
    ans = input("[?] Return to the menu? y/n-> ")
    if ans=="y" or ans=="yes":
        mnu()
    if ans=="n" or ans=="no":
        sys.stdout.write("[!] Exiting!")
        ext()
def chk():
    sys.stdout.write("[?] Would you like to check for... \n    (b)adlines or (e)xisting words?\n")
    sys.stdout.write("\n[!] Be sure to check for badlines BEFORE checking for existing words.\n")
    check=input("[->] b/e -> ")
    def existing():
        rdF = input("[->] File to read -> ")
        fileIn = open(rdF, 'r')
        Lines = fileIn.readlines()
        sys.stdout.write("\n[?] What type of words are these?\n")
        sys.stdout.write("[*] {}\n".format(wtypes))
        wt=input("[->] Wordtype -> ")
        lcount=0
        bcount=0
        blines=[]
        for word in words[wt]:
            for line in Lines:
                lcount+=1
                if line.strip("\n")==word:
                    bcount+=1
                    blines.append(lcount)
                    sys.stdout.write("FOUND EXISTING WORD: {}".format(word))
            if lcount==len(Lines):
                lcount=0
        if bcount==0:
            sys.stdout.write("[*] All done!\n")
            sys.stdout.write("[*] No duplicate words found. Heading back to the menu.\n")
            mnu()
        sys.stdout.write("Existing words: {}".format(bcount))
        sys.stdout.write("line #s: {}".format(blines))
        sys.stdout.write("[?] Would you like to remove the {} existing words?".format(bcount))
        ans = input("[->] y/n -> ")
        if ans=='y':
            sys.stdout.write("[*] Working...\n")
            fileOut=rdF
            with open(fileOut, 'wt') as f_out:
                for i in blines:
                    del Lines[i-1]
                for line in Lines:
                    f_out.write(line)
                sys.stdout.write("[*] All done!\n")
                sys.stdout.write("\n[?] Would you like to check another?\n")
                ans1 = input("[->] y/n -> ")
                if ans1=="y":
                    chk()
                if ans1=="n":
                    mnu()
        if ans=='n':
            ext()
    def badlines():
        rdF = input("[->] File to read -> ")
        fileIn = open(rdF, 'r')
        Lines = fileIn.readlines()
        lcount=0
        bcount=0
        for line in Lines:
            lcount+=1
            if "\\" in line or '"' in line:
                bcount+=1
        sys.stdout.write("[!] Found {} BAD lines out of {} lines!\n".format(bcount,lcount))
        if bcount >= 1:
            sys.stdout.write("[!?] Would you like to fix {} bad lines from {}?\n".format(bcount,rdF))
            ans = input("[->] y/n -> ")
            if ans == "y":
                fileOut = rdF
                sys.stdout.write("[!] Fixing {} bad lines in {}.\n".format(bcount,rdF))
                with open(fileOut, 'wt') as f_out:
                    for line in Lines:
                        ostr= line
                        symbols ="\\\""
                        nstr = ostr
                        for c in symbols:
                            nstr = nstr.replace(c,"")
                        print(''.join(nstr.strip("\n")), file=f_out)
                sys.stdout.write("[!] Fixed {} bad lines out of {} lines.\n".format(bcount,lcount))
            if ans == "n":
                mnu()
            else:
                mnu()
        if bcount < 1:
            sys.stdout.write("[*] Everything looks acceptable in {}.\n".format(rdF))
            ans=input("[->] Would you like to check another? y/n-> ")
            if ans=="y":
                chk()
            if ans=="n":
                mnu()
            else:
                sys.stdout.write("\n[?] Umm. Not too sure what you meant. Heading back to the menu...")
                mnu()
    if check=='b':
        badlines()
    if check=='e':
        existing()
    sys.stdout.write("[!] No such check command!\n")
    chk()
def add():
    sys.stdout.write("[*] Adding some new words...\n")
    sys.stdout.write("[!] Please make certain you (c)heck your wordlist!\n   This will remove any existing words or words that might not be suitable.\n")
    rdF = input("[->] File to read -> ")
    sys.stdout.write("Wordtypes: {}".format(wtypes))
    sys.stdout.write("[!] Please use a singular wordtype.\n")
    wt = input("[->] What type of words are these? -> ")
    wtc=0
    for wtype in words:
        if wt == wtype:
            wtc+=1
            sys.stdout.write("\n[!] Adding new words to {}.\n".format(wt))
            sys.stdout.write("[*] Reading {} ...\n".format(rdF))
            with open(rdF, 'r') as rfile:
                sys.stdout.write("[*] Writing...\n")
                for wrd in rfile:
                    words[wt].append(wrd.strip("\n"))
            setnums()
            json.dump(words, open ('DICTIONARY.json','w'))
            sys.stdout.write("[!] All done!")
            sys.stdout.write("[!] Your words have been digested and added to {}.\n".format(wt))
            sys.stdout.write("[?] Would you like to add some more words?\n")
            ans1=input("[->] y/n -> ")
            if ans1=='y':
                add()
            if ans1=='n':
                mnu()
            else:
                sys.stderr.write("\n[?] Umm. Not too sure what you meant. Heading back to the menu...")
                mnu()
    if wtc==0:
        sys.stderr.write("\n[*] '{}' is NOT an existing wordtype!\n".format(wt))
        sys.stdout.write("[!] Are you sure you want to create a new wordtype?\n")
        ans=input("[->] y/n ->")
        if ans=='y':
            words[wt]=[]
            sys.stdout.write("\n[*] Reading {} ...\n".format(rdF))
            with open(rdF, 'r') as rfile:
                sys.stdout.write("[*] Writing...\n")
                for wrd in rfile:
                    words[wt].append(wrd.strip("\n"))
            setnums()
            json.dump(words, open ('DICTIONARY.json','w'))
            sys.stdout.write("[!] All done!\n")
            sys.stdout.write("[!] Your words have been digested and added to {}.\n".format(wt))
            sys.stdout.write("[?] Would you like to add some more words?\n")
            ans1=input("[->] y/n -> ")
            if ans1=='y':
                add()
            if ans1=='n':
                mnu()
            else:
                sys.stderr.write("[?] Umm. Not too sure what you meant. Heading back to the menu...")
                mnu()
        if ans=='n':
            mnu()
def ext():
    if not newF == None:
        newF.close()
    if not rdF == None:
        rdF.close()
    if platform.system() == 'Windows':
        os.system('color')
    bnrC()
    sys.exit('\n[!] Exiting this program.\n')
################################################################################
def lin():
    Lin = input("[->] Menu -> ")
    if "write" in Lin or Lin == 'w':
        try:
            clr()
            wrt()
            lin()
        except KeyError:
            clr()
            sys.stderr.write("[!] No list for one or more of the defined wordtypes.\n")
            wrt()
            lin()
        except KeyboardInterrupt:
            clr()
            sys.stderr.write("[!] Ctrl+C Interrupt.\n")
            ext()
    if "help" in Lin or Lin == 'h':
        try:
            clr()
            clihlp()
            hlp()
            lin()
        except KeyboardInterrupt:
            clr()
            sys.stderr.write("[!] Ctrl+C Interrupt.\n")
            ext()
    if "menu" in Lin or Lin == 'm':
        try:
            clr()
            bnrO()
            mnu()
            lin()
        except KeyboardInterrupt:
            clr()
            sys.stderr.write("[!] Ctrl+C Interrupt.\n")
            ext()
    if "banner" in Lin or Lin == 'b':
        try:
            clr()
            bnrO()
            lin()
        except KeyboardInterrupt:
            clr()
            sys.stderr.write("[!] Ctrl+C Interrupt.\n")
            ext()
    if "add" in Lin or Lin == 'a':
        try:
            clr()
            add()
            lin()
        except KeyboardInterrupt:
            clr()
            sys.stderr.write("[!] Ctrl+C Interrupt.\n")
            ext()
    if "check" in Lin or Lin == 'c':
        try:
            clr()
            chk()
            lin()
        except KeyboardInterrupt:
            clr()
            sys.stderr.write("[!] Ctrl+C Interrupt.\n")
            ext()
    if "exit" in Lin or Lin == 'e' or Lin == 'x':
        try:
            clr()
            ext()
        except KeyboardInterrupt:
            clr()
            sys.stderr.write("[!] Ctrl+C Interrupt.\n")
            ext()
    else:
        clr()
        sys.stderr.write("[!] No such command.\n")
        mnu()
        lin()
##################################################################################
if __name__ == "__main__":
    try:
        if (len(sys.argv) > 1):
            cmdargs = sys.argv[1:]
            if "-w" in cmdargs[0:]:
                try:
                    if "-r" in cmdargs[0:]:
                         rng = input("[->] Set integer's max (Default=1000)-> ")
                    print(cmdargs)
                    print(cmdargs.index("-w"))
                    widx = cmdargs.index("-w")
                    print(cmdargs[widx+1])
                    newF = cmdargs[widx+1]
                    print(cmdargs[widx+2])
                    arg1, arg2, arg3 = cmdargs[widx+2].split(":")
                    print(arg1)
                    print(arg2)
                    print(arg3)
                    with open(newF, 'w') as f_out:
                        sys.stdout.write("[*] Please wait while I write in {}.\n".format(newF))
                        for c in product(words[arg1],words[arg2],words[arg3]):
                            print(''.join(c), file=f_out)
                    sys.stdout.write("[*] All finished!\n")
                    newF.close()
                except KeyError:
                    sys.stderr.write("[!] No list for one or more of the defined wordtypes.\n")
                    clr()
            if "-h" in cmdargs[0:]:
                clr()
                clihlp()
            if "-a" in cmdargs[0:]:
                clr()
                add()
        else:
            clr()
            bnrO()
            mnu()
            lin()

    except KeyboardInterrupt:
        clr()
        sys.stderr.write("[!] Ctrl+C Interrupt.\n")
        DICTIONARY.close()
        ext()
