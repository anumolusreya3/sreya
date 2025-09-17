def freq_char(str):
    freq={}
    for i in str:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
str="akhilakolli"
print(freq_char(str))