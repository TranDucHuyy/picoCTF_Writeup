def binary_to_ascii(binary_str):
    # Split the binary string into individual binary numbers
    binary_values = binary_str.split()
    # Stored final result of character ascii after convert from binary number 
    ascii_result = ""
    for binary in binary_values:
        # Convert each binary to an ascii character and add it to the result string
        ascii_result += chr(int(binary,2))
    return ascii_result

binary_input = "01110011 01110101 01100010 01101101 01100001 01110010 01101001 01101110 01100101"
ascii_output = binary_to_ascii(binary_input)
print(ascii_output)
