# Title: Lockboxes

## Description:
The Lockboxes folder contains solutions to a problem involving locked boxes. In this problem, you are given a certain number of locked boxes. Each box is sequentially numbered from 0 to n - 1 and may contain keys to other boxes. The task is to write a method, `canUnlockAll(boxes)`, that determines whether it is possible to open all the boxes.

#### Specifications:
- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists.
- A key with the same number as a box can open that box.
- All keys are positive integers.
- There can be keys that do not have corresponding boxes.
- The first box, `boxes[0]`, is unlocked.
- The method should return `True` if all boxes can be opened, otherwise it should return `False`.
