def SearchChallaenge(strParam):
    s=''
    for i in strParam:
        if i.isalnum() :
            s+=i
    s=s.lower()
    if s==s[::-1]:
        return True
    return False
