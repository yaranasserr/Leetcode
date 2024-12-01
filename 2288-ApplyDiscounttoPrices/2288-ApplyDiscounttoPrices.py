class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        def check(s):
            for i in s:
                if i.isalpha() or i == '$':
                    return False
            return True
        
        
        split_sentence = sentence.split()
                
        for i in range(0 , len(split_sentence)):
            if split_sentence[i][0] == '$' and len(split_sentence[i]) > 1:
                if check(split_sentence[i][1:]):
                    split_sentence[i] = split_sentence[i][0] + str("{0:.2f}".format(float(split_sentence[i][1:]) - (float(split_sentence[i][1:])*(discount / 100))))
        
        sentence = ""
        for i in split_sentence:
            sentence += i + " "
        
        sentence = sentence.strip()
        return sentence    