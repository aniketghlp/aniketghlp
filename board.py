# Writing program for a square or rectangle shaped playing board

# below function is for the shape
def DrawBoard(row,column):
    output = True
    if row <=15 and column <=146: #maximum limit for row and column values
        for r in range (1,row+1):
         if r == 1 or r == row:   # for extreme row values printing the * values
          for c in range(1,column+1):
            if c != column:       # for all columns till 2nd last using print on same line
             print("*",end="")
            else:
               print("*")         #for last column print with end line.
         else:                    # for other row values printing "|" and " ".
            for c in range(1,column+1):
             if c == 1:
              print("|",end="")   # for all columns till 2nd last using print on same line
             elif c == column:
                print("|")        #for last column print with end line.
             else:
                print(" ",end="") 
    else:
        output = False       
    return print( row, "and", column, "are",output, "values")

DrawBoard(10,20)  # calling function with values in limit
DrawBoard(15,146) # calling function with max values
DrawBoard(16,5)   # calling function with row value out of range
DrawBoard(10,150) # calling function with column value out of range

#co = "**************************************************************************************************************************************************"
#print(len(co))
