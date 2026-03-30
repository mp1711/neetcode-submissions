class Solution:
    def romanToInt(self, s: str) -> int:

        roman_map = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }

        n = len(s)
        num = 0
        i = 0
        while i<n: 
            if i<n-1 and s[i]+s[i+1] in roman_map: 
                num += roman_map[s[i] + s[i+1]]
                i+=1
            else: 
                num += roman_map[s[i]]
            i+=1
        
        return num

        