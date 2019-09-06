#! python3
#write a function that takes a list of lists of strings
    #and displays it in a well-organized column right-justified

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0]*len(table)
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            if len(table[i][j]) > colWidths[i]:
                colWidths[i] = len(table[i][j])
    for i in range(0, len(table[0])):
        for j in range(0, len(table)):
            print(str(table[j][i]).rjust(colWidths[j],' '), end=" ")
        print('\n')
    
printTable(tableData)
