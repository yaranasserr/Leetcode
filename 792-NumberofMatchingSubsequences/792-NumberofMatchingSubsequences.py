    c= 0
    for word in words:
        if word in hashmap:
             if hashmap[word]:
                c+= 1
        else:
            if is_sub(word):
                c+= 1
                hashmap[word] = True
            else:
                hashmap[word] = False