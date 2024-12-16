class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = set('aeiou')  # Set of vowel letters for quick lookup
        max_vowels = 0
        current_vowels = 0
        
        # First, count the number of vowels in the first window of length k
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        
        max_vowels = current_vowels
        
        # Now, slide the window across the string and update the count of vowels
        for i in range(k, len(s)):
            # Remove the vowel count of the character that's sliding out of the window
            if s[i - k] in vowels:
                current_vowels -= 1
            # Add the vowel count of the new character that's sliding into the window
            if s[i] in vowels:
                current_vowels += 1
            # Update the maximum number of vowels found
            max_vowels = max(max_vowels, current_vowels)
        
        return max_vowels
            
            