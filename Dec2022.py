#sriharsha kocherla
grid = [[0, 77, 32, 403, 337, 452], [5, 23, -4, 592, 445, 620],
        [-7, 2, 357, 452, 317, 395], [186, 42, 195, 704, 452, 228],
        [81, 123, 240, 443, 353, 508], [57, 33, 132, 268, 492, 732]]

# moving is
# bottom is front
# left is left
# top is back
# right is right
# front is top
# back is bottom

# moving down
# top is front
# left is left
# bottom is back
# right is right
# back is top
# front is bottom

# moving left
# front is front
# top is left
# back is back
# bottom is right
# right is top
# left is bottom

# moving right
# front is front
# bottom is left
# back is back
# top is right
# left is top
# right is bottom


def dfs(row, col, front, left, back, right, top, bottom, path):
  score = grid[row][col]
  path.append(str(row) + "," + str(col))
  N = len(path)

  if row == 5 and col == 5:  # return answer
    # print die values for fun
    print(front, left, back, right, top, bottom)
    return path

  # move up; row + 1
  if row + 1 < len(grid):
    if not front:  # if next top is not defined
      tmp = (grid[row + 1][col] - score) / N
      ans = dfs(row + 1, col, bottom, left, top, right, tmp, back, path)
      if ans != []:  # end found in this path
        return ans
    else:
      if score + front * N == grid[row + 1][col]:  # if valid move with die
        ans = dfs(row + 1, col, bottom, left, top, right, front, back, path)
        if ans != []:  # end foundx in this path
          return ans

  # move down; row - 1
  if row - 1 >= 0:
    if not back:  # going to be top next
      tmp = (grid[row - 1][col] - score) / N
      ans = dfs(row - 1, col, top, left, bottom, right, tmp, front, path)
      if ans != []:
        return ans
    else:
      if score + back * N == grid[row - 1][col]:
        ans = dfs(row - 1, col, top, left, bottom, right, back, front, path)
        if ans != []:
          return ans

  # move left; col + 1
  if col + 1 < len(grid[0]):
    if not right:  # going to be top next
      tmp = (grid[row][col + 1] - score) / N
      ans = dfs(row, col + 1, front, top, back, bottom, tmp, left, path)
      if ans != []:
        return ans
    else:
      if score + right * N == grid[row][col + 1]:
        ans = dfs(row, col + 1, front, top, back, bottom, right, left, path)
        if ans != []:
          return ans

  # move right; col - 1
  if col - 1 >= 0:
    if not left:  # going to be top next
      tmp = (grid[row][col - 1] - score) / N
      ans = dfs(row, col - 1, front, bottom, back, top, tmp, right, path)
      if ans != []:
        return ans
    else:
      if score + left * N == grid[row][col - 1]:
        ans = dfs(row, col - 1, front, bottom, back, top, left, right, path)
        if ans != []:
          return ans

  path.pop()
  return []


# die value being None means unknown; python stuff
passed = dfs(0, 0, None, None, None, None, None, None, [])

seen = set(passed)  # check if element in passed in O(1) time
# sum up values not passed
total = 0
for row in range(len(grid)):
  for col in range(len(grid[0])):
    if str(row) + "," + str(col) not in seen:
      total += grid[row][col]

print(passed)  # path for fun
print(total)  # final answer
