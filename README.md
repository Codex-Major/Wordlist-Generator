# Codex - Wordlist Generator
# Install:
    git clone http://www.github.com/codex-Major/Wordlist-Generator

<a href="https://www.buymeacoffee.com/CodexMajor" target="_blank" style="display: inline-block;"><img src="https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-orange.svg?style=flat-square" align="center"/></a>

**Command line usage WIP.
**Currently only allows for concatenation of three args. WIP will make it flexible.

    Run as: python3 codex_v1.0.py
# Commands:

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
        (-c)heck | Checks a file for existing words and words with symbols in them.

            [!] Acceptable wordlists contain a single word in each line with no symbols.
                [?] Unacceptable Symbols: \ and "
                
------------------------------------------------------------------------------------
        [*] Args:| {this will change as more lists are added to DICTIONARY.json} |

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
