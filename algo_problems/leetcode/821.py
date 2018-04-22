class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        cPosArr = [i for i, l in enumerate(S) if l == C]
        distances = [-1] * len(S)
        for i, letter in enumerate(S):
            minDistance = min([abs(i - pos) for pos in cPosArr])
            distances[i] = minDistance
        
        return distances

    def shortestToCharOnePass(self, S, C):
        lastCPos = -1
        leftPointer = 0
        
        distances = [len(S)] * len(S)

        for i, l in enumerate(S):
            if l == C:
                while leftPointer != i:
                    distances[leftPointer] = min(distances[leftPointer], i - leftPointer)
                    leftPointer += 1
                distances[i] = 0
                lastCPos = i
            else:
                if lastCPos != -1:
                    distances[i] = i - lastCPos
        return distances


