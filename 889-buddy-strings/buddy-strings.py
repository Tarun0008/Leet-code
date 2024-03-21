class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)

        counter_s = Counter(s)
        counter_goal = Counter(goal)

        if counter_s != counter_goal:
            return False
        dif = sum(a != b for a, b in zip(s, goal))

        return dif == 2
