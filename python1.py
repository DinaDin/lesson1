def get_summ(one, two, delimiter='&'):
    one_s = str(one)
    two_s = str(two)
    result = '{}{}{}'.format(one_s,delimiter,two)
    return(result)
res = get_summ("Learn","Python"," ")
print(res.upper())
