#INTRO TO IT 2nd COURSE
#Расчет стоимости iPhone в кредит:
#(Предположим, что это простой кредит без процентов)

def iphone_credit_cost(iphone_price, months):
    monthly_payment = iphone_price / months
    total_cost = monthly_payment * months
    return total_cost