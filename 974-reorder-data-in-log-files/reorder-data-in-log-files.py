class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # seperate letter from digit logs 
        letters = []
        digits = []
        for l in logs :
            content= l.split()[1]
            if content.isdigit():
                digits.append(l)
            else:
                letters.append(l)

        # sort letter logs by content 
        sorted_letters = sorted(letters, key=lambda log: (log.split()[1:], log.split()[0]))
        return sorted_letters + digits 


        