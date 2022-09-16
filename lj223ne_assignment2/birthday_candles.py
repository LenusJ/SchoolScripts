
candles = 0
birthday = 0
boxes = 0

for i in range(0, 100):
    birthday += 1
    boxesNeeded = (birthday // 24) + 1
    if birthday == 100:
        boxesNeeded -= 1
    if candles < birthday:
        boxes += boxesNeeded
        candles += 24 * boxesNeeded
        if birthday < 15 or birthday > 94:
            print(f"Before birthday {birthday}, buy {boxesNeeded} box(es)")
        elif birthday == 16:
            print("\n ...\n")

    candles -= birthday

print(f"Total number of boxes: {boxes}, Remaining candles: {candles}")
