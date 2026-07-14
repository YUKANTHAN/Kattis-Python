rate = 0.1  # dollars per minute
day = 0
in_park = {}
totals = {}

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if not line:
        continue

    if line == "OPEN":
        day += 1
        in_park = {}
        totals = {}

    elif line == "CLOSE":
        print(f"Day {day}")
        for name in sorted(totals.keys()):
            print(f"{name} ${totals[name]:.2f}")
        print()

    else:
        parts = line.split()
        action, name, time = parts[0], parts[1], int(parts[2])

        if action == "ENTER":
            in_park[name] = time
        elif action == "EXIT":
            duration = time - in_park[name]
            totals[name] = totals.get(name, 0) + duration * rate
            del in_park[name]
