class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        last_r = None
        sol = ''
        dot_count = 0
        for i,c in enumerate(dominoes):
            if c == 'L':
                if last_r == None:
                    sol += 'L'*(dot_count + 1)
                else:
                    print(dot_count,last_r)
                    sol += 'R'*(dot_count//2)
                    if dot_count%2 == 1:
                        sol += '.'
                    sol += 'L'*(dot_count//2 + 1)
                last_r = None
                dot_count = 0
            elif c == 'R':
                if dot_count > 0:
                    if last_r:
                        sol += 'R'*dot_count
                    else:
                        sol += '.'*dot_count             
                sol += 'R'
                last_r = True
                dot_count = 0
            else:
                dot_count+=1

        if dot_count > 0:
            if last_r:
                sol += 'R'*dot_count
            else:
                sol += '.'* dot_count


        return sol

                

        