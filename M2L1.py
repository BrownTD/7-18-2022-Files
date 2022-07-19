#Using Dependency and package managers
#Agile Software Development
#user story As a... I want... So that
#    [type of user] [goal]   [benefit]
#acceptance criteria

#Filter the Qualifying Loans

def filter_max_loan_size()
    loan_size_approval_list=[]

    for bank in bank_list:
        if loan_amount<= int(bank[1]):
            loan_size_approval_list.append(bank)
    return loan_size_approval_list