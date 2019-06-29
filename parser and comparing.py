def extract_list(filename):
    list = []
    Ulist = []
    file = open(filename,'r')

    for line in file:
        i = 0
        while i in range(len(line)):
            t_count = 0
            if line[i] == '\t' and t_count == 0:
                # it now reads the substring
                substring = line[0:i - 1]
                writeline = [substring, line[i+1:-1]]
                break

            i+=1
        Ulist.append(substring)
        list.append(writeline)

    return list, Ulist


def comparison(List1, Ulist1, List2, Ulist2):
    matchList = []
    for i in range(len(Ulist1)):
        count = len(Ulist1) - i
        if count%1000 == 0:
            print(count)
        for j in range(len(Ulist2)):
            if Ulist1[i] == Ulist2[j]:
                match = [List1[i][1],List2[j][1]]
                matchList.append(match)
                break

    file = open('match_result.txt', 'w')
    for item in matchList:
        file.write(str(item) + '\n')


print("start extracting list 1")
list1, ulist1 = extract_list('new_11_substring_list.txt')
print("list 1 extraction completed")
print("start extracting list 2")
list2, ulist2 = extract_list('new_12_substring_list.txt')
print("list 2 extraction completed")

print("start comparison")
comparison(list1, ulist1, list2, ulist2)
