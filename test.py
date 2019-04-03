"""
ここに解答コードを書いてください
"""

def dictionary_data(data):
    dict_data = {}
    for line in data[:-1]:
        dict_data[line.rstrip('\n').split(':')[0]] = line.rstrip('\n').split(':')[1]
    return dict_data

def sort_dict_data(data):
    return dict(sorted(dictionary_data(data).items()))

def fizzbuzz_extension(sorted_data, number):
    answer_str = ''
    keys = list(sorted_data.keys())
    values = list(sorted_data.values())
    for i in range(len(keys)):
        if int(number) % int(keys[i]) == 0:
            answer_str += values[i]
    if answer_str== '':
        return number
    else:
        return answer_str

if __name__ == '__main__':
    data = open('input.txt', mode='r').readlines()
    print(fizzbuzz_extension(sort_dict_data(data), data[-1].rstrip('\n')))
