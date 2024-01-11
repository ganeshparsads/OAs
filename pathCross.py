def isPathCrossing(path):
    path_crossed = set()
    
    x = 0
    y = 0
    
    path_crossed.add((x,y))
    
    for i in list(path):
        if i == 'E':
            x += 1
        elif i == 'W':
            x -= 1
        elif i == 'N':
            y += 1
        else:
            y -= 1
        

        if (x, y) in path_crossed:
            print("here")
            return True
        
        path_crossed.add((x,y))

        print((x,y))
        print(path_crossed)
        
    return False

print(isPathCrossing("NESWW"))
