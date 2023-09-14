from collections import defaultdict
from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        all_food = set()
        all_tables = set()
        orders_from_tables = defaultdict(lambda: defaultdict(int))
        for order in orders:
            table = order[1]
            all_tables.add(table)
            for food in order[2:]:
                all_food.add(food)
                orders_from_tables[table][food] += 1
        all_food = list(all_food)
        all_food.sort()
        ans = [["Table"] + all_food]
        all_tables = [int(table) for table in all_tables]
        all_tables.sort()
        all_tables = [str(table) for table in all_tables]
        for table in all_tables:
            ans.append([table] + [str(orders_from_tables[table][food]) for food in all_food])
        return ans


s = Solution()
print(s.displayTable([["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
                      ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]))
print(s.displayTable(
    [["James", "12", "Fried Chicken"], ["Ratesh", "12", "Fried Chicken"], ["Amadeus", "12", "Fried Chicken"],
     ["Adam", "1", "Canadian Waffles"], ["Brianna", "1", "Canadian Waffles"]]))
print(s.displayTable([["Laura", "2", "Bean Burrito"], ["Jhon", "2", "Beef Burrito"], ["Melissa", "2", "Soda"]]))
