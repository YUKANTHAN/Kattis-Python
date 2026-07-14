text = input()
letters = [text[0]]
letters +=[text[i+1] for i in range(len(text)-1) if text[i] == "-" and text[i+1].isalpha()]
print("".join(letters))  # Output: ['d', 'g']
