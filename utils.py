
letters = 'abcdefghijklmnopqrstuvwxyz'


def delete_letter(word):
    
    delete_l = []
    split_l = [] 

    split_l = [(word[:i], word[i:]) for i in range(len(word)+1)]
    delete_l = [L + R[1:] for L, R in split_l if R]
 
    return delete_l



def switch_letter(word):
    
    switch_l = []
    split_l = []

    split_l = [(word[:i], word[i:]) for i in range(len(word)+1)]
    switch_l = [L + R[1] + R[0] + R[2:] for L, R in split_l if len(R) >= 2]

    return switch_l



def replace_letter(word):
    replace_l = []
    split_l = []
    
    split_l = [(word[:i], word[i:]) for i in range(len(word)+1)]
    temp_l = [L + letter + R[1:] for L, R in split_l if R for letter in letters]
    replace_set = set(temp_l)
    replace_set.discard(word)

    replace_l = sorted(list(replace_set))
     
    return replace_l



def insert_letter(word):

    insert_l = []
    split_l = []
    
    split_l = [(word[:i], word[i:]) for i in range(len(word)+1)]
    insert_l = [L+i+R for L,R in split_l for i in letters]
 
    return insert_l



def edit_one_letter(word, allow_switches = True):

    edit_one_set = set()
    
    replace_l = replace_letter(word)
    insert_l = insert_letter(word)
    delete_l = delete_letter(word)
    
    if allow_switches:
        switch_l = switch_letter(word)
    else:
        switch_l = []
        
    total_l = replace_l + insert_l + delete_l + switch_l
    
    edit_one_set = set(total_l)

    return edit_one_set



def edit_two_letters(word):

    edit_two_set = set()
    
    edit_one = edit_one_letter(word)
    total = []
    for i in edit_one:
        total.extend(list(edit_one_letter(i)))
        
    edit_two_set = set(total)
    
    return edit_two_set



def get_corrections(word, probs, vocab, n):
    
    suggestions = []
    n_best = {}
    
    if word in vocab:
        suggestions.append(word)
    one_edit = edit_one_letter(word)
    for i in one_edit:
        if i in vocab:
            suggestions.append(i)
    two_edit = edit_two_letters(word)
    for j in two_edit:
        if j in vocab:
            suggestions.append(j)
            
    suggestions = suggestions[:n]
    
    for l in suggestions:
        n_best[l] = probs[l]
        
    n_best = {k: v for k, v in sorted(n_best.items(), key=lambda item: item[1], reverse=True)}
    

    return n_best