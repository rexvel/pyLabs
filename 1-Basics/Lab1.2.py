def long_word(sen):
    return max(filter(lambda x: x.isalpha(), sen.split()), key=len)
test = "Turmoil has engulfed the Galacticgarlic Republic  The test test test test Republic "

mock = "Chargoggagoggmanchauggagoggchaubunagungamaugg"

def most_freq(str):
    l = str.split()
    d = {}
    for i in l:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i]+1
    print(d)
    return d
res = long_word(test)
    
res2 = most_freq(test)
print(res)
print(res2)

