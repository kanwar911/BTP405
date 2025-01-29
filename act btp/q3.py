def wordCount(filename):
    word_dict = {}
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            words = line.strip().split()
            for word in words:
                word = word.lower().strip(",.?!;:()[]{}\"'")  # remove punctuation
                if word:
                    if word in word_dict:
                        word_dict[word].append(line_num)
                    else:
                        word_dict[word] = [line_num]
    
    return word_dict

# Call the function with the existing file in the folder
word_counts = wordCount("sample_text.txt")

# Display the dictionary output
print(word_counts)
