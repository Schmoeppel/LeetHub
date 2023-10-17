class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        idx = 0
        while True:
            if idx >= len(senate):
                idx = 0
            #print(senate)
            if senate[idx] == "R":
                delete_idx = senate.find("D",idx+1)
                if delete_idx == -1:
                    delete_idx = senate.find("D")
                if delete_idx != -1:
                    senate = senate[:delete_idx] + senate[delete_idx+1:]
                    idx += 1
                else:
                    return "Radiant"
            elif senate[idx] == "D":
                delete_idx = senate.find("R",idx+1)
                if delete_idx == -1:
                    delete_idx = senate.find("R")
                if delete_idx != -1:
                    senate = senate[:delete_idx] + senate[delete_idx+1:]
                    idx += 1
                else:
                    return "Dire"
