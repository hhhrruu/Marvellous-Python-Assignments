def prime(no):
    chk =0 
    for i in range(2,no):
        if no % i == 0:
            chk =1 
            break
        

    if chk == 0  :
        return True
    else:
        return False                   


