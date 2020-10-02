

def get_file_lines(filename):
    inline = open('poem.txt', 'r')
    lines = inline.readlines()
    poem = inline.read()
    inline.close()
    return lines

print(get_file_lines('poem.txt'))
poems = get_file_lines('poem.txt')

def lines_printed_backwards(lines_list):
    line = len(poems)
    number = 0
    for i in poems
        if number < line:
            number += 1
            num_plus_line = number + 


    
        

print(lines_printed_backwards(poems))

# lines = inline.readlines()
# print_lines = print(lines.reverse())
# return print_lines






# inline = open('poem.txt', 'r')
# poem = inline.read()
# print(poem)
# inline.close()






# lines_reverse = []
#     inline = open('poem.txt', 'r')
#     for line in lines_list:
#         if line == lines_list[0]:
#             lines_reverse.append(line)
#         else:
#             lines_reverse.insert(0, line)
#     for line in lines_reverse:
#         print(line)    