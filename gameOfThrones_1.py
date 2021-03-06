"""========================================================================================================================

King Robert has 7 kingdoms under his rule. He gets to know from a raven that the Dothraki are going to wage a war against him soon. But, he knows the Dothraki need to cross the narrow river to enter his dynasty. There is only one bridge that connects both sides of the river which is sealed by a huge door.

door

The king wants to lock the door, so that, the Dothraki can't enter. But, to lock the door he needs a key that is an anagram of a certain palindrome string.

The king has a list of words. Help him figure out if any anagram of the words can be a palindrome or not?

Input Format 
A single line which contains the input string

Constraints 
1<=length of string <= 10^5 Each character of the string is a lowercase english letter.

Output Format 
A single line which contains YES/NO in capital letter of english alphabet.

Sample Input : 01

aaabbbb
Sample Output : 01

YES
Explanation 
A palindrome permutation of the given string is bbaaabb. 

Sample Input : 02

cdefghmnopqrstuvw
Sample Output : 02

NO
Explanation 
You can verify that the given string has no palindrome permutation. 

Sample Input : 03

cdcdcdcdeeeef
Sample Output : 03

YES
Explanation 
A palindrome permutation of the given string is ddcceefeeccdd .

========================================================================================================================"""

def is_pal_possible(string):
    if len(string) == 1:
        return "YES"
    else:
        pal = "YES"
        if len(string) % 2 == 0:
            for i in set(string):
                if string.count(i) % 2 != 0:
                    pal = "NO"
                    break 
        else:
            counter = 0
            for i in set(string):
                if string.count(i) % 2 != 0:
                    counter += 1
                    if counter > 1:
                        pal = "NO"
                        return pal
                        break
        return pal
                        
                        
           

def main():
    string = raw_input()
    print is_pal_possible(string)

    
    
if __name__ == "__main__":
	main()
