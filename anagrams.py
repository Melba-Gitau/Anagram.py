# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(string1,string2):
     # [assignment] Add your code here
 string1="live"  
 string2="evil"
 if sorted(string1)==sorted(string2):
     print("True")
 else:
     print("False")

print:(find_anagram("live","evil"))


