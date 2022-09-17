
candles = 0
birthday = 0
boxes = 0
boxesNeeded = 0

for i in range(0, 100):
    birthday += 1
    while candles < birthday:
        boxesNeeded += 1
        candles += 24
    boxes += boxesNeeded
    if boxesNeeded > 0:
        print(f"Before birthday {birthday}, buy {boxesNeeded} box(es)")
        boxesNeeded = 0
    candles -= birthday


print(f"Total number of boxes: {boxes}, Remaining candles: {candles}")
