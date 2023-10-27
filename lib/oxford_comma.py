def oxford_comma(items):
    if(len(items)>2):
        items[-1] = 'and '+ items[-1]
        return ', '.join(items)
    elif(len(items)==1):
        return ''.join(items)
    else:
        items[-1] = 'and '+ items[-1]
        return ' '.join(items)

print(oxford_comma(["fiddleheads", "okra", "kohlrabi"]))