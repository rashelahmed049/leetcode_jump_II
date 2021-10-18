def jump(a):
    farthest=current=jump = 0
    for i in range(len(l)):
        farthest  = max(farthest,a[i]+i)
        
        if current==len(a)-1:
            break
        if i==current:
            current = farthest
            jump+=1
        
        
    return jump
    
    
l=[2,3,1,1,4]
print(jump(l))
