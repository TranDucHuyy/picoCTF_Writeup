def decimal_to_ascii(decimal_str):
    octal_values = decimal_str.split()
    ascii_result = ""
    for octal in octal_values:
        ascii_result += chr(int(octal,8))
    return ascii_result

octal_input = "146 141 154 143 157 156" 
ascii_output = decimal_to_ascii(octal_input)
print(ascii_output)