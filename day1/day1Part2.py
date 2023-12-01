word_to_number = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def convert_to_numbers(input_string):
    word = ''
    startIndex = 0
    i = 0
    replace_string = ''
    while (i < len(input_string)):

        word += input_string[i]
        #print(f"word is : {word}")

        if input_string[i].isdigit():
            if(len(word) == 1):
                replace_string = replace_string + str(input_string[i])
                #print(f"replace is : {replace_string}")
            startIndex += 1
            i = startIndex - 1
            word = ''
        
        else:

            # Does this word mean a number (words from 3 letters to 5 letters range can form a number)
            if (len(word) > 2 and len(word) < 6 ):
                if word in word_to_number:
                    # Replace words representing numbers with their numerical value
                    #print(f"word replaced is : {word} with {word_to_number.get(word)}")
                    #replace_string = replace_string.replace(word, word_to_number.get(word))
                    replace_string = replace_string + str(word_to_number.get(word))
                    startIndex += 1
                    word = ''
                    i = startIndex - 1
                    #print(f" word is {word} replace is : {replace_string}")

                elif  i == len(input_string)-1:
                    startIndex += 1
                    i = startIndex - 1
                    word = ''

            elif len(word) < 3:
            # Do Nothing
                pass
            else:
                startIndex += 1
                i = startIndex - 1
                word = ''

        i += 1
    #print(f"The string after replacing words with numbers: {replace_string}")
    return replace_string


#input_strings = 'jfive637ffqdnjfjseven76'

#converted_string = convert_to_numbers(input_strings)
#print(f"The string after converted_string  with numbers: {converted_string}")

