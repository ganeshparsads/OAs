

# Python program to move every character
# K times ahead in a given string
 
 
def replace_characters(string, k):
   
    # Convert the string to a list of characters
    char_list = list(string)
    new_char_list = []
     
    # Iterate over each character in the list
    for i in range(len(char_list)):
        ascii_val = (ord(char_list[i]) - ord('a') + k) % 26 + ord('a')
        new_char_list.append(chr(ascii_val))

        if char_list[i] == 'z':
            ascii_val = (ord(char_list[i]) - ord('a') + k) % 26 + ord('b')
            new_char_list.append(chr(ascii_val))

    # Convert the list of characters back to a string
    return "".join(new_char_list)


# driver code     
str = "abczy"
k = 2
 
print(replace_characters(str, k))

