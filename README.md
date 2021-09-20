# WordlistGen.py

This python tool is capable of creating massive wordlists, and expanding its own vocabulary with other wordlists.

**Command line usage WIP.

[?] Commands:

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
