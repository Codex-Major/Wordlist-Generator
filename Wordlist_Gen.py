from itertools import product
import sys
import time
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
color = ["red", "orange", "yellow", "blue", "green", "indigo", "violet",
         "pink", "magenta", "grey", "white", "black", "brown", "tan",
         "gold", "silver"]

sport = ["soccer", "football", "cricket", "baseball", "softball",
         "hockey", "tennis"]

adj = ["all", "one", "other", "this", "that", "more",
       "most", "first", "new", "newer", "newest", "good",
       "better", "best", "last", "own", "same", "old",
       "older", "elder", "eldest", "oldest", "little", "less",
       "lesser", "littler", "least", "littlest", "small", "smaller",
       "smallest", "big", "bigger", "biggest", "different", "more",
       "most", "next", "great", "greater", "greatest", "local", "social",
       "important","national", "high", "higher", "highest", "low", "lower",
       "lowest", "long", "longer", "longest", "first", "second",
       "third", "fourth", "fifth", "sixth", "seventh", "eighth",
       "ninth", "tenth", "left", "leftmost", "right", "rightmost",
       "large", "larger", "largest", "general", "young", "younger",
       "youngest", "political", "able", "public", "private",
       "particular", "full", "fuller", "fullest", "available", "early",
       "earlier", "earliest", "late", "later", "latest", "main", "major", "minor",
       "economic", "sure", "surest", "likely", "likelier", "likeliest",
       "unsure", "only", "clear", "clearer", "clearest", "real", "realest",
       "international", "certain", "special", "difficult", "open",
       "whole", "half", "wifi", "costly", "free", "central", "common",
       "short", "shorter", "shortest", "tall", "taller", "tallest",
       "similar", "same", "human", "necessary", "true", "truest", "single",
       "personal", "former", "financial", "foreign", "recent", "strong",
       "stronger", "strongest", "soft", "softer", "softest", "hard", "harder",
       "hardest", "various", "due", "bad", "worse", "worst", "good",
       "better", "best", "present", "royal", "poor", "rich", "wrong",
       "wrongest", "natural", "easy", "easier", "easiest", "simple",
       "simplest", "individual", "current", "legal", "modern", "final",
       "nice", "nicer", "nicest", "fine", "finest", "close", "closest",
       "total", "previous", "prime", "industrial", "happy", "happiest",
       "appropriate", "top", "bottom", "thin", "thinner", "thinnest",
       "wide", "wider", "widest", "dead", "living", "lively", "sorry", "sorriest",
       "succesful", "unsuccessful", "military", "soviet", "original",
       "basic", "complex", "aware", "popular", "professional", "direct",
       "useful", "effective", "ready", "dark", "darker", "darkest", "western",
       "northern", "western", "considerable", "cold", "chilly", "hot", "warm",
       "physical", "responsible", "complete", "medical", "heavy", "heavier",
       "heaviest", "extra", "past", "future", "essential", "male", "primary",
       "secondary", "civil", "beautiful", "obvious", "positive", "negative",
       "fair", "unfair", "senior", "nuclear", "annual", "relevant", "regional",
       "commercial", "latter", "huge", "hugest", "official", "regular", "usual",
       "additional", "active", "inactive", "powerful", "middle", "impossible",
       "domestic", "actual", "technical", "ordinary", "internal", "excellent",
       "fresh", "freshest", "rotten", "far", "farthest", "potential",
       "famous", "alone", "safe", "safest", "conservative", "formal", "proper",
       "very", "rural", "initial", "substantial", "unable", "average",
       "reasonable", "unreasonable", "strange", "stranger", "stragest",
       "light", "lighter", "lightest", "suitable", "ilove", "love", "lovely",
       "loveliest", "loving", "immediate", "equal", "quiet", "correct", "scientific",
       "expensive", "cheap", "critical", "double", "triple", "urban", "moral",
       "careful", "vital", "quick", "quickest", "afraid", "scared", "crying",
       "familiar", "family", "historical", "perfect", "daily", "apparent",
       "careful", "bloody", "bloodiest", "internal", "external", "ancient",
       "brief", "capable", "thin", "typical", "broad", "busy", "slow", "slowest",
       "narrow", "narrowest", "entire", "wonderful", "constant", "clean", "dirty",
       "ideal", "academic", "fake", "fakest", "crucial", "inner", "outer",
       "grand", "roman", "funny", "funnier", "funniest", "unique", "massive",
       "sharp", "dull", "net", "guilty", "angry", "angriest", "valuable", "temporary",
       "glad", "friendly", "sudden", "dependent", "competetive", "radical",
       "keen", "sensitive", "inside", "outside", "flat", "emotional", "healthy",
       "global", "rapid", "admin", "admministrative", "silent", "maximum",
       "minimum", "secret", "wet", "solid", "brilliant", "electronic",
       "absolute", "visual", "wooden", "firm", "electric", "chemical", "sad",
       "supreme", "leterary", "pure", "rough", "mere", "genuine", "extreme",
       "pale", "classic", "classical", "favorite", "numerous", "distinct",
       "confident", "opposite", "helpful", "tough", "stupid", "fast", "stable",
       "straight", "strategic", "outstanding", "conscious", "dominant", "cool",
       "anxious", "residential", "fit", "fittest", "impressive", "nervous",
       "accurate", "musical", "extraordinary", "honest", "precise", "visible",
       "slight", "monetary", "remote", "plain", "distant", "still", "gentle",
       "junior", "smooth", "psycho", "psychological", "violent", "structural",
       "inevitable", "round", "rounded", "roundest", "sensible", "welcome", "silly",
       "fat", "fattest", "deaf", "near", "nearest", "grateful", "pretty", "evident",
       "occasional", "pleasant", "universal", "fellow", "blind", "square",
       "loose", "tight", "creative", "medieval", "level", "ultimate", "steady",
       "intellectual", "desperate", "judicial", "revolutionary", "vulnerable",
       "imperial", "rebel", "raw", "flexible", "informal", "gross", "bitter",
       "sweet", "tangy", "sour", "spicy", "juicy", "salty", "frequent", "experimental",
       "spiritual", "intense", "historic", "rational", "acute", "prominent",
       "logical", "valid", "weekly", "generous", "random", "modest", "sleeping",
       "marginal", "identical", "nearby", "satisfactory", "marginal", "identical",
       "exact", "distinct", "distinctive", "oral", "bare", "controversial",
       "organic", "pregnant", "curious", "statistical", "urgent", "desireable",
       "exclusive", "superb", "super", "strict", "sheer", "innocent", "marine",
       "romantic", "retail", "artificial", "institutional", "magnificent",
       "biological", "convenient", "reluctant", "uncertain", "digital",
       "analog", "aggresive", "wise", "unfair", "superior", "inferior", "spare",
       "explicit", "painful", "absract", "intelligent", "unhappy", "genetic",
       "realstic", "influential", "just", "hungry", "intensive", "tropical",
       "temperate", "frozen", "boiling", "giant", "huge", "ridiculous", "parallel",
       "subtle", "subtlest", "secure", "securest", "decent", "marvellous",
       "partial", "lesser", "occupational", "vertical", "progressive",
       "continental", "excessive", "exceptional", "nasty", "elegant", "casual",
       "concrete", "crazy", "chronic", "damp", "delicate", "magic", "lonely",
       "upset", "fun", "splendid", "operational", "primitive", "neat",
       "contrary", "accessible", "adjacent", "hostile", "brave", "gay",
       "peaceful", "horrible", "dynamic", "indirect", "direct", "handsome",
       "precious", "notable", "definite", "unfortunate", "artistic", "neutral",
       "magnetic", "endless", "fierce", "mild", "loud", "ambitious", "verbal",
       "coastal", "enthusiastic", "smart", "rigid", "minimal", "mobile", "dreadful",
       "drunk", "drunken", "shiny", "poison", "poisoned"
       ]
animal =["cat", "kitty", "kitten", "dog", "doggy", "puppy",  "elephant",
          "serval", "ocelot", "giraffe","caracal", "saiga", "viper",
          "macaw", "bear", "panda", "parrot", "kia", "gazel", "hiyena",
          "bird", "eagle", "margay", "ferret", "tapir", "agouti", "puffin",
          "baboon", "mandrill", "vulture", "lemur", "langur", "ringtail",
          "buzzard", "albatross", "seahorse", "cockroach", "otter",
          "racoon", "quail", "emu", "rhea", "cassowary", "barracuda",
          "owl", "alpaca", "paca", "gemsbok", "eel", "cheetah", "catfish",
          "pangolin", "crab", "bat", "walrus", "fox", "addax", "gar",
          "kangaroo", "wallaby", "chameleon", "snake", "gerbil", "hamster",
          "pig", "manatee", "lion", "tiger", "seal", "squid", "cuttlefish",
          "cod", "lobster", "crab", "orca", "civet", "seal", "fish", "shark",
          "dolphin", "whale", "penguin", "newt", "wombat", "cow", "dugong",
          "woodpecker", "toad", "frog", "bullfrog", "puffer", "boa", "krait",
          "bengal", "octopus", "dolphin", "mantaray", "manta", "ray", "manatee",
          "horse", "sheep", "chicken"
          ]

noun = ["number","ladder", "axe", "account", "apple", "house", "case", "system",
         "group", "party", "company", "school", "fact", "money", "point",
         "state", "night", "water", "thing", "family", "head", "hand", "order",
         "home", "power", "country", "council", "use", "service", "room", "market",
         "problem", "court", "police", "car", "vehicle", "form", "face", "education",
         "policy", "research", "office", "offices", "body", "person", "health",
         "mother", "father", "daughter", "son", "gandpa", "grandfather", "grandma",
         "grandfather", "question", "period", "name", "book", "level", "child", "children",
         "control", "joystick", "button", "society", "door", "line", "city", "center",
         "effect", "staff", "position", "job", "man", "woman", "act", "process", "idea",
         "support", "moment", "sense", "report", "mind", "morning", "land", "range",
         "table", "back", "trade", "history", "study", "street", "committee", "rate",
         "word", "food", "experience", "result", "team", "sir", "madame", "section",
         "program", "air", "authority", "role", "reason", "price", "town", "class", "nature",
         "subject", "department", "union", "bank", "check", "member", "value", "practice", "paper",
         "date", "decision", "figure", "hammer", "screwdriver", "pliers", "wrench",
         "right", "wife", "husband", "president", "present", "gift", "university",
         "friend", "club", "quality", "guitar", "debate", "voice", "stage", "king",
         "situation", "light", "tax", "product", "production", "march", "madness",
         "month", "board", "hospital", "music", "cost", "field", "fields", "award",
         "awards", "issue", "bed", "project", "chapter", "girl", "boy", "male", "female",
         "sailor", "manager", "computer", "security", "sec", "structure", "hair", "heart",
         "force", "attention", "letter", "model", "material", "pilot", "lover", "boyfriend",
         "girlfriend", "boo", "fire", "growth", "sea", "record", "size", "space", "plan",
         "energy", "cup", "design", "pressure", "hall", "coupe", "couple", "zombie", "ice", "icey",
         "vampire", "werewolf", "hacker", "technology", "list", "contract", "wall", "county",
         "army", "hotel", "spring", "summer", "fall", "winter", "village", "hour", "garden",
         "doctor", "application", "operation", "press", "extent", "window", "shop",
         "doubt", "majority", "minority", "degree", "television", "station", "access",
         "blood", "statement", "sound", "title", "concern", "public", "software", "species",
         "spy", "spies", "glass", "lady", "answer", "earth", "responsibility", "appeal",
         "campaign", "task", "whole", "river", "stool", "chair", "sector", "baby", "speaker",
         "base", "box", "weight", "past", "safety", "character", "trouble", "principle",
         "aid", "exchange", "library", "budget", "cash", "tea", "balance", "afternoon",
         "morning", "evening", "night", "midnight", "reference", "truth", "protection",
         "turn", "reveiw", "minute", "second", "queen", "king", "lord", "kitchen", "stock",
         "student", "holiday", "career", "length", "width", "height", "ball", "bowl",
         "fork", "wire", "bottle", "penny", "quarter", "impact", "image", "justice",
         "vigilante", "race", "wine", "gas", "gasoline", "rail", "handrail", "railway",
         "train", "expression", "advantage", "wood", "tree", "banana", "grape", "cheerio",
         "foot", "corner", "step", "damage", "credit", "pain", "possibility", "speed", "strength",
         "wind", "breeze", "solution", "band", "farm", "pound", "match", "animal", "skin", "scene",
         "article", "stuff", "fear", "island", "contact", "claim", "video", "telephone",
         "cabinet", "target", "phone", "grant", "prison", "poison", "food", "text",
         "network", "aircraft", "airplane", "plane", "bridge", "star", "user", "path",
         "danger", "zone", "note", "theatre", "movie", "list", "tour", "package", "player",
         "file", "castle", "driver", "code", "silence", "gentleman", "bag", "leg", "desire",
         "palace", "engine", "lunch", "cross", "key", "milk", "cover", "breath", "sky",
         "ground", "lake", "stream", "volcano", "mountain", "valley", "motion", "sport",
         "factory", "iron", "pool", "hole", "gallery"
        ]
verb = ["writing","riding"
        ]
#====================================================================================================================================
rng = (1000)
formnumber2 = ['{:>02d}'.format(i) for i in range(rng)]
formnumber3 = ['{:>03d}'.format(i) for i in range(rng)]
formnumber4 = ['{:>04d}'.format(i) for i in range(rng)]
formnumber5 = ['{:>05d}'.format(i) for i in range(rng)]
formnumber6 = ['{:>06d}'.format(i) for i in range(rng)]
formnumber7 = ['{:>07d}'.format(i) for i in range(rng)]
formnumber8 = ['{:>08d}'.format(i) for i in range(rng)]
formnumber9 = ['{:>09d}'.format(i) for i in range(rng)]

#def type(str):
 #   for char in str:
  #      time.sleep(.001)
   #     sys.stdout.write(char)
    #    sys.stdout.flush()

def open_file(_fileName):
    rng = input("Set integer's max(Default=1000): ")
    with open(_fileName, 'w') as f_out:
        type("Please wait while I write your file...")
        for c in product(color):
            print(''.join(c), file=f_out)

def Cmd():
    print("LOADING...\n")
    time.sleep(2)
    print("Enter the name of the file you'd like to create for your wordlist.\n")
    print("If a file with that name already exists, it will be overwritten.\n")
    print("Please refrain from using numbers in your filename.\n")
    fileName = "/wordlists/"+input("> ")
    """numbers = ['{:>03d}'.format(i) for i in range(999)]"""
    print()
    print("Please enter the rule arguments in the order you would like to apply them to your wordlist.\n")
    print()
    print("Rule args:| color / adjective / animal / noun / verb / number / formnumber |\n")
    print()
    print("'number' will write a number as: 1\n")
    print("while 'formnumber2' will write as: 01 ; and 'formnumber9' will write as: 000000001\n")
    print()
    print("For example:\n")
    print("            color, animal, formnumber3 | #1,646,352 words\n")
    print("            #Writes things like: redshark001 or greentiger999\n")
    print("          or\n")
    print("            noun, noun, formnumber2 | #22,498,789 words\n")
    print("            #Writes things like: roomservice02 or waterdamage999\n")
    print("          or\n")
    print("            adj, noun, number | #256,383,360 words\n")
    print("            #Writes things like: posionapple2 or ancientpalace123\n")
    args = input("> ")
    
    #split = args.split(', ')
    #print(len(split))

    for lsts in args:
        rng = input("Set integer's max(Default=1000): ")
        with open(fileName, 'w') as f_out:
            type("Please wait while I write your file...")
            for c in product(args):
                print(''.join(c), file=f_out)
            

    if "color" in args:
        rng = input("Set integer's max(Default=1000): ")
        with open(fileName, 'w') as f_out:
            type("Please wait while I write your file...")
            for c in product(color):
                print(''.join(c), file=f_out)

    if "color, number" in args:
        rng = input("Set integer's max(Default=1000): ")
        with open(fileName, 'w') as f_out:
            type("Please wait while I write your file...")
            for c in product(color, number):
                print(''.join(c), file=f_out)
    
    if "color, animal, formnumber2" in args:
        rng = input("Set integer's max(Default=1000): ")
        with open(fileName, 'w') as f_out:
            type("Please wait while I write your file...")
            for c in product(color, animal, formnumber2):
                print(''.join(c), file=f_out)
                
    if "color, animal, formnumber3" in args:
        rng = input("Set integer's max(Default=1000): ")
        with open(fileName, 'w') as f_out:
            type("Please wait while I write your file...")
            for c in product(color, animal, formnumber3):
                print(''.join(c), file=f_out)

    if "color, animal, number" in args:
        rng = input("Set integer's max(Default=1000): ")
        with open(fileName, 'w') as f_out:
            type("Please wait while I write your file...")
            for c in product(color, animal, number):
                print(''.join(c), file=f_out)

    if "formnumber9" in args:
        rang = input("Set integer's max(Default=1000): ")
        rng = rang
        with open(fileName, 'w') as f_out:
            type("Please wait while I write your file...")
            for c in product(formnumber9):
                print(''.join(c), file=f_out)

    if "noun, noun, formnumber2" in args:
        rng = input("Set integer's max(Default=1000): ")
        with open(fileName, 'w') as f_out:
            type("Please wait while I write your file...")
            for c in product(noun, noun, formnumber2):
                print(''.join(c), file=f_out)

    if "adj, noun, formnumber2" in args:
        rng = input("Set integer's max(Default=1000): ")
        with open(fileName, 'w') as f_out:
            type("Please wait while I write your file...")
            for c in product(adj, noun, formnumber2):
                print(''.join(c), file=f_out)

    if "adj, noun, formnumber3" in args:
        rng = input("Set integer's max(Default=1000): ")
        with open(fileName, 'w') as f_out:
            type("Please wait while I write your file...")
            for c in product(adj, noun, formnumber3):
                print(''.join(c), file=f_out)

                

    type("All finished!\n")
    time.sleep(1)
    type("Killing this program...\n")
    time.sleep(1)
    quit()
#-------------------------------------------------------------------------------
Cmd()
