def connectedCell(matrix):
    max_count = 0
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 1:
                region_cell_count = region_cells(matrix, row, col)
                max_count = max(max_count, region_cell_count)
    return max_count

def region_cells(grid, row, col):
    if any([row<0, col<0, row>=len(grid), col>=len(grid[0])]):
        return 0
    if grid[row][col] == 0:
        return 0

    cell_count = 1
    grid[row][col] = 0

    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if any([r!=row, c!=col]):
                cell_count += region_cells(grid, r, c)

    return cell_count