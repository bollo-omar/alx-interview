def canUnlockAll(boxes):
    """
The 'canUnlockAll' function determines if all the boxes can be opened.
It performs a breadth-first search (BFS) starting from the initial box (box 0).
Each box is represented as a list of keys that can open other boxes.
The function uses a 'visited' list to track the visited boxes.
The BFS explores each box and marks them as visited if a key opens a new box.
If all boxes have been visited, the function returns True.
Otherwise, it returns False if there is at least one unvisited box.
"""
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        curr_box = queue.pop(0)
        
        for key in boxes[curr_box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
