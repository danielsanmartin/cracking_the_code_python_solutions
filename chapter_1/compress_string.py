def compress_string(s) -> str:
    output = []

    if len(s) <= 2:
        return s
    
    count = 1
    for i in range(1,len(s)):
        
        if s[i] != s[i-1]:
            output.append(s[i-1])
            output.append(str(count))
            count = 1

            if i == len(s)-1:
                output.append(s[i])
                output.append(str(count))            
        else:
            count += 1
            if i == len(s)-1:
                output.append(s[i])
                output.append(str(count)) 
    

    return ( ''.join(output) if len(output) < len(s) else s)


assert compress_string('a') == 'a'
assert compress_string('aabbbc') == 'aabbbc'
assert compress_string('abb') == 'abb'
assert compress_string('abbbbbb') == 'a1b6'
assert compress_string('abbbccccccd') == 'a1b3c6d1'