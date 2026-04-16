class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, path, diff):
            if diff == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > diff:
                    break

                path.append(candidates[i])
                backtrack(i + 1, path, diff - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return res