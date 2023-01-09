class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        h = 0
        m = damage[0]

        for d in damage:
            if d>m:
                m = d
            h += d
        h -= min(armor, m)

        return h+1
