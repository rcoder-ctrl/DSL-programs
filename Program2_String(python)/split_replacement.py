def splitting(statement):
    i=0
    words=[]
    while i<len(statement):
        if statement[i]==" ":
            words.append(statement[:i-1])
            statement=statement[i+1:]
            i=0
        else:
            i=i+1
    return words