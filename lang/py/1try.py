l=['A','B','C','D','E','F','G','H','I']

def p():
    print('''
                 |      |    
               {} |   {}  |  {} 
            _____|______|______
                 |      |    
               {} |   {}  |  {} 
            _____|______|_____
                 |      |    
               {} |   {}  |  {} 
                 |      |    
    '''.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8]))

p()