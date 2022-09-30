#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
template = ''

with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()

for i in range(len(names)):
    names[i] = names[i][0: -1]

with open('./Input/Letters/starting_letter.txt') as file:
    template = file.read()

for name in names:
    with open(f'./Output/ReadyToSend/{name}.txt', mode='w') as file:
        file.write(f"{template.replace('[name]', name)}")

