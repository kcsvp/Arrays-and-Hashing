class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_map = Counter(text)

        for each in 'balon':
            if each not in text_map:
                return 0
        
            
        return min(text_map['b'],text_map['a'],text_map['n'],text_map['l']//2,text_map['o']//2)