def list_reversion(list):
    """This function returns a list with reversed order

    Parameters
    ----------
    list : list
        List on which the reversion is applied.
    """     
    
    # create an empty list
    reversed_list=[]
    # iterate through elements of the input list
    for i in range(len(list)+1):
    
        # invert elements and append them to new list
        reversed_list.append(list[-i])
    
    # get rid of the first element of the new list, because it is a duplicate
    reversed_list = reversed_list[1:]
    
    return reversed_list