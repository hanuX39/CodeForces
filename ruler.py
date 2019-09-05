def draw_line(central_length, label = None):
    line = '-'*central_length
    if label:
        line += ' ' + label
    print(line)

def draw_interval(central_length):
    if central_length > 0:
        draw_interval(central_length-1)
        # print('********')
        draw_line(central_length)
        # print('***')
        draw_interval(central_length-1)

def ruler(num_inches, length):
    draw_line(length,'0')
    for inch in range(1,1+num_inches):
        draw_interval(length-1)
        draw_line(length, str(inch))

ruler(3,5)