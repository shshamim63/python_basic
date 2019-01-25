def merge_the_tools(string, k):
    # your code goes here
    for i in range(int(len(string) / k)):
	    temp = ''
	    for c in string[i * k : (i + 1) * k]:
		    if c in temp:
			    continue
		    temp += c
	    print (temp)
string, k = input(), int(input())
merge_the_tools(string, k)