from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)
        self.food_ratings = defaultdict(int)
        self.cuisine_ratings = defaultdict(list)
        self.food_to_cuisine = {}
        for i in range(n):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]
            self.food_ratings[food] = rating
            heappush(self.cuisine_ratings[cuisine], (-rating, food))
            self.food_to_cuisine[food] = cuisine

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_ratings[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heap = self.cuisine_ratings[cuisine]
        heappush(heap, (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_ratings[cuisine]
        while heap:
            rating, food = heappop(heap)
            if self.food_ratings[food] == -rating:
                heappush(heap, (rating, food))
                return food

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
