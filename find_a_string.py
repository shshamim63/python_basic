def count_substring(string, sub_string):
    status=False
    occur=0
    for i in range((len(string)-len(sub_string)+1)):
        status=False
        if string[i]==sub_string[0]:
            status=True
            for j in range(len(sub_string)):
                if string[i+j]==sub_string[j]:
                    status=status and True
                else:
                    status=False
        if status==True:
            occur+=1
    return occur

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)