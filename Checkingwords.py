#Name: Nana Kwasi Owusu
#Date: 5th April, 2024
#Program Description: A program that reads in a text file and prints out any word that is not found in the spelling dictionary.

import spellchecker

def get_file():
    while (True):
        selected_file = input('Enter the name of the file to read: ')
        try:
            f = open(selected_file,'r')
            return f
        except:
            print('Could not open file.')
            
      
if __name__ == "__main__":
    print('Welcome to Text File Spellchecker.')
    inspected_file = get_file()
    lines = inspected_file.readlines()
    checker = spellchecker.Spellchecker('english_words.txt')
    passed_words = 0
    failed_words = 0
    
    for count,i in enumerate(lines):
        for word in i.split():
            if checker.check(word) == False:
                print(f'Possible Spelling Error on line {count+1}: {word}')
                failed_words +=1
            else:
                passed_words +=1
    
    print(f'{passed_words} passed spell checker.')
    print(f'{failed_words} failed spell checker.')
    print(f'{(passed_words)/(passed_words+failed_words) * 100 :.2f}% of the words passed.')
    inspected_file.close()
                
    
        
    
    
    
            