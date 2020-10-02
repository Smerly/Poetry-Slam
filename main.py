from random import choice

def get_file_lines(filename):
    # Joi: Instead of passing 'poem.txt', use the param filename
    inline = open(filename, 'r')
    lines = inline.readlines()
    # Joi: You do not need the line below (line 8) 
    return lines


def lines_printed_backwards(lines_list):
      # Step 1: Look up how to reverse a list using .reverse()
      lines_list.reverse()
      # Step 2: Measure the length of the list
      line_length = len(lines_list)

      for i in range(line_length):
        line_number = line_length - i
        line = lines_list[i]
        print(f"{line_number} {line} ")

# TODO:
def lines_printed_random(lines_list):

  # Btw, for this function you do not have to print the line number this time. only for line_printed_backwards you needed the line number.
 
  line_length = len(lines_list)

  for i in range(line_length):
    line_random = choice(lines_list)
    print(line_random)

    
# --------------------------------------
  # Notes to remember things
#get_file_lines = the raw lines of poem.txt
#lines_list = the listed version of the poem.txt
#line_length = the amount of lines there are (as an integer)
#line_number = the line_length - i in range of line_length
#
#
#



# --------------------------------------
# TODO:
# def lines_printed_custom(lines_list):


poems = get_file_lines('poem.txt') 

lines_printed_backwards(poems)
lines_printed_random(poems)
# lines_printed_custom(poems)

#  ^^^ Uncomment each line after your finished you defining the function.
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