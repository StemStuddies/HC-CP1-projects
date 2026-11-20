#hunter card, flexible calculator
import math

def calc(*numbers, oper="sum"):
    if oper == "sum":
        return(sum(*numbers))
    elif oper == "average":
        return(sum(*numbers)/len(*numbers))
    elif oper == "max":
        return(max(*numbers))
    elif oper == "min":
        return(min(*numbers))
    elif oper == "product":
        return(math.prod(*numbers))


