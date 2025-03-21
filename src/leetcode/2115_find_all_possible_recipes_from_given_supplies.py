from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        g = defaultdict(list)
        in_degree = defaultdict(int)
        n = len(recipes)
        for i in range(n):
            recipe = recipes[i]
            for ing in ingredients[i]:
                g[ing].append(recipe)
                in_degree[recipe] += 1

        ans = []
        recipes = set(recipes)
        visited = set()
        q = deque(supplies)
        while q:
            supply = q.popleft()
            if supply in visited:
                continue
            visited.add(supply)
            if supply in recipes:
                ans.append(supply)
            for descendant in g[supply]:
                in_degree[descendant] -= 1
                if in_degree[descendant] == 0:
                    q.append(descendant)

        return ans
