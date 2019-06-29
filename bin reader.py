

def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                yield from chunk
            else:
                break


def get_binpos(raw_ind):
    bytePos = raw_ind//8
    inPos = raw_ind%8
    return str(bytePos) + " + " + str(inPos + 1)


def read_file(filename):
    allbytes = ''
    bytelist = []
    for b in bytes_from_file(filename):
        currentByte = format(b, '08b')
        allbytes += currentByte
        bytelist.append(currentByte)

    return allbytes, bytelist


def get_substring_list(string, minlen, maxlen):
    list = []
    i = minlen
    while i <= maxlen:
        unique_sub = []
        current_list = []
        print(maxlen - i)
        # 192 is the index of the byte where the sequence become arbitrary
        for j in range(192*8, len(string) - i + 1):
            # print(list)
            current_sub = string[j:j + i]

            starting_ind = get_binpos(j)
            ending_ind = get_binpos(j + i - 1)
            length = str(i)
            pos_record = [starting_ind, ending_ind, length]
            # print(pos_record)

            if current_sub not in unique_sub:
                unique_sub.append(current_sub)
                current_list.append([current_sub, [pos_record]])
            else:
                for k in range(len(current_list)):
                    if current_sub == current_list[k][0]:
                        current_list[k][1].append(pos_record)

        for unit in current_list:
            list.append(unit)

        i += 6
    return list


def get_substring_list_alt(string, lengthlist):
    list = []

    for i in lengthlist:
        unique_sub = []
        current_list = []
        # 192 is the index of the byte where the sequence become arbitrary
        for j in range(192 * 8, len(string) - i + 1):
            # print(list)
            current_sub = string[j:j + i]

            starting_ind = get_binpos(j)
            ending_ind = get_binpos(j + i - 1)
            length = str(i)
            pos_record = [starting_ind, ending_ind, length]
            # print(pos_record)

            if current_sub not in unique_sub:
                unique_sub.append(current_sub)
                current_list.append([current_sub, [pos_record]])
            else:
                for k in range(len(current_list)):
                    if current_sub == current_list[k][0]:
                        current_list[k][1].append(pos_record)

        for unit in current_list:
            list.append(unit)
    return list



def find_same_substring(str1, str2):
    posList = []

    return posList


def save_list(saveFilename, list):
    file = open(saveFilename, 'w')
    for record in list:
        # print(record)
        line = ''
        line += record[0]
        for pos_record in record[1]:
            line = line + '\t' + '[' \
                   + pos_record[0] \
                   + ', ' + pos_record[1] \
                   + ', ' + pos_record[2] + ']'
        line += '\n'

        file.write(line)

fileName = 'new 11.bin'
fileName2 = 'new 12.bin'

# ab = all binary string
# bl = binary list
ab_1, bl_1 = read_file(fileName)
ab_2, bl_2 = read_file(fileName2)

# print(len(ab_1))
# print(len(ab_2))

# test_str = 'abuchhhdhuiabuchheuub'
# testSS = get_substring_list(test_str, 6, len(test_str)//2)
# print(testSS)
# save_list('test.txt', testSS)
# print(len(ab_1))

# testlist = [['g', [['a','3','5'],['s','f','5']]],
#             ['y', [['y','p','p']]]]
# save_list('test.txt', testlist)

deck_length = [17]

substring_list_1 = get_substring_list_alt(ab_1, deck_length)
save_list('new_11_substring_list.txt', substring_list_1)

substring_list_2 = get_substring_list_alt(ab_2, deck_length)
save_list('new_12_substring_list.txt', substring_list_2)


# print(get_substring_list(test_str, 6, len(test_str)//2))