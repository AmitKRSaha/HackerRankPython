def count_substring(string, sub_string):
    count = 0
    for x in range(0, len(string)):
        if x + len(sub_string) <= len(string) and string[x: x + len(sub_string)] == sub_string:
            count = count + 1
            
    print(count)