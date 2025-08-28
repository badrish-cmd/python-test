def char_count(s):
    count={}
    for i in s:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i]=1
    return count 
print("the result is",char_count("hello"))