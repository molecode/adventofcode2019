intcode = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,69,55,225,1001,144,76,224,101,-139,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1102,60,49,225,1102,51,78,225,1101,82,33,224,1001,224,-115,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1102,69,5,225,2,39,13,224,1001,224,-4140,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,101,42,44,224,101,-120,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,68,49,224,101,-3332,224,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,50,27,225,1102,5,63,225,1002,139,75,224,1001,224,-3750,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,102,79,213,224,1001,224,-2844,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1,217,69,224,1001,224,-95,224,4,224,102,8,223,223,1001,224,5,224,1,223,224,223,1102,36,37,225,1101,26,16,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,677,677,224,102,2,223,223,1006,224,329,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,344,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,359,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,374,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1008,677,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,7,677,226,224,102,2,223,223,1005,224,419,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,449,1001,223,1,223,108,677,677,224,102,2,223,223,1006,224,464,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,479,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,509,101,1,223,223,7,677,677,224,102,2,223,223,1006,224,524,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,539,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,569,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,584,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,599,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,614,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,644,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,659,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]

isp = 0

def get_parameter_mode(parameter_modes, isp):
    try:
        return parameter_modes[isp]
    except IndexError:
        return 0

def get_input_output(parameter_modes, isp):
    parameter_mode = get_parameter_mode(parameter_modes, 0)
    if parameter_mode == 0:
        input_one = intcode[intcode[isp+1]]
    elif parameter_mode == 1:
        input_one = intcode[isp+1]

    parameter_mode = get_parameter_mode(parameter_modes, 1)
    if parameter_mode == 0:
        input_two = intcode[intcode[isp+2]]
    elif parameter_mode == 1:
        input_two = intcode[isp+2]

    output = intcode[isp+3]

    return input_one, input_two, output

while True:
    instruction = [x for x in map(int, str(intcode[isp]))]
    op_code = int(''.join(map(str, instruction[-2:]))) 
    if op_code == 99:
        break

    parameter_modes = instruction[:-2]
    parameter_modes.reverse()

    # addition
    if op_code == 1:
        input_one, input_two, output = get_input_output(parameter_modes, isp)
        intcode[output] = input_one + input_two
        isp += 4
    # multiplication
    elif op_code == 2:
        input_one, input_two, output = get_input_output(parameter_modes, isp)
        intcode[output] = input_one * input_two
        isp += 4
    # read input
    elif op_code == 3:
        output = intcode[isp+1]
        intcode[output] = int(input('> '))
        isp += 2
    # print output
    elif op_code == 4:
        parameter_mode = get_parameter_mode(parameter_modes, 0)
        if parameter_mode == 0:
            print(intcode[intcode[isp+1]])
        elif parameter_mode == 1:
            print(intcode[isp+1])
        isp += 2
    # jump-if-true
    elif op_code == 5:
        parameter_mode = get_parameter_mode(parameter_modes, 0)
        if parameter_mode == 0:
            value = intcode[intcode[isp+1]]
        elif parameter_mode == 1:
            value = intcode[isp+1]
        if value != 0:
            parameter_mode = get_parameter_mode(parameter_modes, 1)
            if parameter_mode == 0:
                isp = intcode[intcode[isp+2]]
            else:
                isp = intcode[isp+2]
        else:
            isp += 3
    # jump-if-false
    elif op_code == 6:
        parameter_mode = get_parameter_mode(parameter_modes, 0)
        if parameter_mode == 0:
            value = intcode[intcode[isp+1]]
        elif parameter_mode == 1:
            value = intcode[isp+1]
        if value == 0:
            parameter_mode = get_parameter_mode(parameter_modes, 1)
            if parameter_mode == 0:
                isp = intcode[intcode[isp+2]]
            else:
                isp = intcode[isp+2]
        else:
            isp += 3
    # less than
    elif op_code == 7:
        input_one, input_two, output = get_input_output(parameter_modes, isp)
        if input_one < input_two:
            intcode[output] = 1
        else:
            intcode[output] = 0
        isp += 4
    # equals
    elif op_code == 8:
        input_one, input_two, output = get_input_output(parameter_modes, isp)
        if input_one == input_two:
            intcode[output] = 1
        else:
            intcode[output] = 0
        isp += 4
    else:
        print(f'Unknown Op Code => {op_code}.')
        break


print(intcode)
