def convertInputString():
    rawInput = input("\nPlease enter a word, phrase, or a sentence \nto check if it is a palindrome: ") 
    rawString = rawInput.lower() 
    rawList = list(rawString) 
    return rawList

def stripAnalphabetics(dirtyList): 
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
    for character in analphabeticList: 
        if character in dirtyList: 
            dirtyList.remove(character) 
            return stripAnalphabetics(dirtyList)
    return dirtyList 

def runPalindromeCheck(straightList):
    reversedList = straightList[::-1] 
    if reversedList == straightList: 
        return "The text you have entered is a palindrome!" 
    else: 
        return "The text you have entered is not a palindrome." 

def main(): 
    print("\nPalindrome checker") 
    originalList = convertInputString()  
    originalList = stripAnalphabetics(originalList) 
    palindromeCheck = runPalindromeCheck(originalList)
    print(palindromeCheck)

main() 