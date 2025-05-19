def calc_moves(itemsOnFloors,elevatorMoves = 0):
    while itemsOnFloors[-1] != sum(itemsOnFloors):
        for floor in range(0,len(itemsOnFloors)-1):
            elevatorMoves += 2 * (itemsOnFloors[floor] - 1) - 1
            itemsOnFloors[floor + 1] += itemsOnFloors[floor]
            itemsOnFloors[floor] = 0
    return elevatorMoves


print("Task1: ",calc_moves( [4, 5, 1, 0]))
print("Task2: ",calc_moves( [8, 5, 1, 0]))
