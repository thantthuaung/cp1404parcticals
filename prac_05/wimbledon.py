FILENAME = "wimbledon.csv"
NUMBER_ONE = 1
PLAYER_POSITION = 2


def main():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        data = []
        for line in in_file:
            row = line.strip().split(",")
            data.append(row)

    champion_amount = {}
    things = set()
    for part in data[NUMBER_ONE:]:
        things.add(part[NUMBER_ONE])
        if part[PLAYER_POSITION] not in champion_amount:
            champion_amount[part[PLAYER_POSITION]] = NUMBER_ONE
        else:
            champion_amount[part[PLAYER_POSITION]] += NUMBER_ONE

    for key, value in champion_amount.items():
        print(f"{key}:{value}")
    print(f"\nThese {len(list(things))} countries have won Wimbledon: ")
    print(", ".join(list(things)))


main()
