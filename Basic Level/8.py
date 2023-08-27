def fis_btw_coor(x1,x2,y1,y2):
    return (((x2-x1)**2)-((y2-y1)**2))**.5
    
distance = fis_btw_coor(7,4,2,2)
print(int(distance))
