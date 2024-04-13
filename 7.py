message="ven ga"
ch_to_dots={'V':'..','E':'.$$','N':'.,.','G':',,..','A':'..#'}
v=""
for i in message:
    if i.upper()!=" ":
        v+=ch-ch_to_dots[i]+" "
    elif i==" ":
        v+="   "
print(v)


