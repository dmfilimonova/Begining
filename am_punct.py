#3724650756252
#3,724,650,756,252

n = input()

def format_my(n):
    if len(n) < 4:
        return n
    else:
        n = n[::-1]
        c = 0
        new = []
        
        for i in range(len(n)):
            new.append(n[i])
        k = len(new) // 3
        for i in range(len(new) + k):
            if c == 3:
                new.insert(i, ",")
                c -= 3
            else:
                c += 1
        new = new[::-1]
        if new[0] != ',':
            return new
        else:
            new.remove(new[0])
            return new


    
print(''.join(format_my(n)))


