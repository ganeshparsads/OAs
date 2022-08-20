
# Python program for the above approach
def printSubStrings(input_str):
    key_map = {
        "a": 1,
        "b": 1,
        "c": 2
    }
 
    # First loop for starting index
    for i in range(len(input_str)):
        subStr = "";
 
        # Second loop is generating sub-String
        for j in range(i,len(input_str)):
            subStr += input_str[j];
            print(subStr + "");

printSubStrings("asdf")
