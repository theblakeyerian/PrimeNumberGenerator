#written by blake yerian, 8-1-2023
def primecounting(maxtime):
    allcounters = [[1,1]]
    for globaltime in range(2,maxtime):  
        if not any([x[1] == 0 for x in allcounters]):
            allcounters.append([globaltime,globaltime])         
        allcounters = [[counter[0], counter[1] if counter[1] != 0 else counter[0]] for counter in allcounters] 
        allcounters = [[x[0], x[1] - 1] for x in allcounters]  
        allcounters[0][1] = 1 
    return [element[0] for element in allcounters]
