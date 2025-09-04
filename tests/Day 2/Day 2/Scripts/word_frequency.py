user_input = input("enter the sentence:")
sentence = user_input.lower().split(" ")
empty_dict = {}
for word in sentence:
    if word in empty_dict:
        empty_dict[word] += 1
    else:
        empty_dict[word] = 1
print(empty_dict)


