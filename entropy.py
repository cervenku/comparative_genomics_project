import math

def getColumnEntropy(colStr, N):
    all_aa = list(set(colStr))
    if len(all_aa) == 1:
        return 0
    prob = []
    for aa in all_aa:
        prob.append(colStr.count(aa) / N)
    entropy = 0
    for p in prob:
        entropy += p*math.log(p,2)
    return -entropy

num_seq = 25
alignment = ['']*num_seq  # this will store alignment from each line
entropy = [] # this will be the result
countSeq = True 

j = 0

with open("protein_msa.aln",'r',encoding = 'utf-8') as f:
    for n, line in enumerate(f):
        if(line[:7] != 'CLUSTAL' and line[0] != '\n'): #skips first lines
            if(line[0] != ' '):
                if(j == 25):
                    j = 0
                alignment[j] = (line.split('     ')[1].replace('\n','').replace(' ', ''))
                j += 1
            else: # conservation symbols
                columns = ['']*len(alignment[0])
                
                # get symbols in each column
                for seq in alignment:
                    for i in range(0, len(seq) - 1):
                        columns[i] += seq[i]
                        
                # get entropy
                for colStr in columns:
                    
                    if('-' in colStr):
                        entropy.append(0)
                    else:
                        # calculate entropy
                        entropy.append(getColumnEntropy(colStr, num_seq))

with open("entropy.txt",'w',encoding = 'utf-8') as f:
    for val in entropy:
        f.write(str(val) + '\n')