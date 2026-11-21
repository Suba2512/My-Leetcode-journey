class Solution(object):
    def sortTheStudents(self, score, k):
        m = len(score)
        for i in range(m):
            best_idx = i
            for j in range(i + 1, m):
                if score[j][k] > score[best_idx][k]:
                    best_idx = j
            score[i], score[best_idx] = score[best_idx], score[i]
        return score