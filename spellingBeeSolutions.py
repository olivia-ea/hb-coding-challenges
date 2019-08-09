def spellingBeeSolutions(wordlist, puzzles):

    #store each letter of word in hashtable

    #APPLE, PLEAS, PLEASE
    #AELWXYZ, AELPXYZ, AELPSXY, SAELPXY, XAELPSY
    #[0, 1, 3, 2, 0]

    # wordlist_dict = {}
    # puzzle_dict = {}

    wordlist_set = []
    puzzle_set = []
    combo_lst = []


    #for letter in wordList:
        #wordList[letter] = wordList.get(letter, 0) + 1

    #make a set and have each word be a 

    # [{a,p,l,e}, {p,l,e,a,s}, {p,l,e,a,s,e}]

    # check if 

    #for letter in puzzles:
        #puzzles[letter] = puzzles.get(letter, 0) + 1


    for word in wordlist:
        wordlist_set.append(set(word))

    for word in puzzles:
        puzzle.set.append(set(word))


    count = 0
    for i in wordlist_set:
        for j in puzzle_set:
            if i.issubset(j):
                counter += 1 
        combo_lst.append(counter)
        counter = 0

    return combo_lst




            # a:1, p:2, l:1, e:1
            # a:1 


    # check if wordlist_dict.keys is a subset of puzzles.keys 







