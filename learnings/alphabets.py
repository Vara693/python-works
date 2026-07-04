def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    lines = []
    for i in range(size):
        left = alpha[size-1:i:-1]  # descending part
        center = alpha[i]          # middle letter
        right = alpha[i+1:size]    # ascending part
        row = '-'.join(left + center + right)
        lines.append(row.center(4*size-3, '-'))  # width calculation

    full_design = lines[::-1] + lines[1:]
    print('\n'.join(full_design))

# Example
print_rangoli(5)



def merge_the_tools(s, C):
    poCe = []
    sam = []
    ralph = 0
    alpha = 0
    for ch in s:
        poCe.append(ch)
    for i in range(0,len(poCe),C):
        ralph = poCe[i:i+C-1]
        sam.append(ralph)
    labo = []
    for j in range(len(sam)):
        alpha = set(sam[j])
        labo.append(alpha)
    for f in labo:
        print(f)
        
  
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)