
with open('testFiles\Excel_datas\RawData.txt', 'r') as file, open('testFiles\Excel_datas\OutPut.txt', 'w') as output:

    for line in file:
        numbers = line.split()
        first_four = numbers[3:7]
        output.write('\t'.join(first_four) + '\n')

print("done!")