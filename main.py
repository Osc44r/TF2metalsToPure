def pureConvert(refs,recs,scraps):
    scrap = 0.11
    reclaimed = 0.33
    refined = 1

    if scraps > 2:
        if scraps%3 == 0:
            recs = recs+scraps/3
            scraps = 0

        if scraps%3 == 1:
            recs = recs+(scraps-1)/3
            scraps = 1
        if scraps%3 == 2:
            recs = recs+(scraps-2)/3
            scraps = 2

    if recs > 2:
        if recs%3 == 0:
            refs = refs+recs/3
            recs = 0
        if recs%3 == 1:
            refs = refs+(recs-1)/3
            recs = 1
        if recs%3 == 2:
            refs = refs+(recs-2)/3
            recs = 2

    pure = round(refs*refined+recs*reclaimed+scraps*scrap,2)
    return pure

print(pureConvert(11,66,22)) #example

    
