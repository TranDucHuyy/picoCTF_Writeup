def heximal_to_ascii(heximal_str):
    heximal_values = heximal_str.split()
    ascii_result = ""
    for heximal in heximal_values:
        ascii_result += chr(int(heximal,16))
    return ascii_result

heximal_input = "31 34 33 31 31 36 36 33 39 34 32 37 30 39 36 37 34 38 36 37 31 32 32 32 30 38 32 31 34 39 30 31 39 37 30 36 35 30 34 39 36 37 38 38 31 35 31 32 33 39 35 32 30 39 37 31 36 32 33 34 31 31 37 31 32 39 37 37 31 31 39 36 36 30 34 35 34 30 33 37 36 37 38 34 30 38 37 34 31 35 30 31"
ascii_output = heximal_to_ascii(heximal_input)
print (ascii_output)