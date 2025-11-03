my_text = input("Enter a text: ").lower()
vowels =  0

for char in my_text:
    if char in 'aeiou':
        vowels += 1
print("Number of vowels:", vowels)