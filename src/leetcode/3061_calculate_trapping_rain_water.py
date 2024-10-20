import pandas as pd


def calculate_trapped_rain_water(heights: pd.DataFrame) -> pd.DataFrame:
    n = len(heights['height'])
    left_max = [0] * n
    right_max = [0] * n
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights['height'][i - 1])
    for i in reversed(range(n - 1)):
        right_max[i] = max(right_max[i + 1], heights['height'][i + 1])
    trapped_water = 0
    for i in range(n):
        trapped_water += max(min(left_max[i], right_max[i]) - heights['height'][i], 0)
    return pd.DataFrame({'total_trapped_water': [trapped_water]})


data = [[1, 0], [2, 1], [3, 0], [4, 2], [5, 1], [6, 0], [7, 1], [8, 3], [9, 2], [10, 1], [11, 2], [12, 1]]
df = pd.DataFrame(data, columns=['id', 'height']).astype({'id': 'Int64', 'height': 'Int64'})
print(calculate_trapped_rain_water(df))
