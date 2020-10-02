from random import choice

def get_file_lines(filename):
    
    inline = open(filename, 'r')
    lines = inline.readlines()
    
    return lines





def lines_printed_backwards(lines_list):
      
      lines_list.reverse()
      
      line_length = len(lines_list)

      for i in range(line_length):
        line_number = line_length - i
        line = lines_list[i]
        print(f"{line_number} {line} ")





def lines_printed_random(lines_list):
 
   line_length = len(lines_list)

   for i in range(line_length):
     line_random = choice(lines_list)
     print(line_random)

def lines_printed_custom(lines_list):
    line_length = len(lines_list)
    line_first_half = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    while str(line_length) in line_first_half:
        print(lines_list[1:8])
    else:
        lines_reversed = lines_list.reverse()
        print(lines_reversed)


    
# --------------------------------------
  # Notes to remember things
#
#get_file_lines = the raw lines of poem.txt
#lines_list = the listed version of the poem.txt
#line_length = the amount of lines there are (as an integer)
#line_number = the line_length - i in range of line_length
#
#
#



# --------------------------------------

poems = get_file_lines('poem.txt') 

lines_printed_backwards(poems)
lines_printed_random(poems)
lines_printed_custom(poems)









#  ^^^ Uncomment each line after your finished you defining the function.
# lines = inline.readlines()
# print_lines = print(lines.reverse())
# return print_lines





