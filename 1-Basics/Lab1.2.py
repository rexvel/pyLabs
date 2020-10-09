def long_word(sen):
    return max(filter(lambda x: x.isalpha(), sen.split()), key=len)
test = "Turmoil has engulfed the Galactic Republic  The taxationChargoggagoggmanchauggagoggchaubunagungamaugg Republic "

mock = "Chargoggagoggmanchauggagoggchaubunagungamaugg"

def most_freq(str):
    counts = dict()
    words = str.split()


    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    counts_x = sorted(counts.items(), key=lambda kv: kv[1])
    #print(counts_x)
    return counts_x[-2]
res = long_word(test)
    
res2 = most_freq(test)
print(res)
print(res2)

