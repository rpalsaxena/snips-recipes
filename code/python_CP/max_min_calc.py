def calc_max(list1):
    mx = list1[0]
    for i in range(1, len(list1)):
        if list1[i] > mx:
            mx = list1[i]
    return mx
   
   
### Print 2nd max val
for i in range(2, n):
    if list1[i] > top1:
        top2 = top1
        top1 = list1[i]
    elif list1[i] > top2 and list1[i] != top1:
        top2 = list1[i]
        
print(top2)

### Print 2nd lowest value
for i in range(2, n):
    if list1[i] < low1:
        low2 = low1
        low1 = list1[i]
    elif list1[i] < low2 and list1[i] != low1:
        low2 = list1[i]

print(low2)        


### Print N largest elements
 
ls = []
for i in range(0, N):
    ls.append(max(list1))
    list1.remove(max(list1))
    
    
