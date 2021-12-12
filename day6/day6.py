from utils import get_logger
LOGGER = get_logger()

def lanternfish_count(data, days):
    """
    Calculate the number of lanternfish after certain days
    """

    # Initialize the number lanternfish for each day
    fish_days = [0] * 9
    for day in data:
        fish_days[day] += 1

    LOGGER.info(f"Initial fish_days: {fish_days}")

    for i in range(days):
        newborn_fish = 0
        if fish_days[0]:
            newborn_fish = fish_days[0]
            LOGGER.debug(f"Fish at day 0: {newborn_fish}")

        for d in range(len(fish_days)-1):
            fish_days[d] = fish_days[d + 1]

        if newborn_fish:
            fish_days[-1] = newborn_fish
            fish_days[6] += newborn_fish
        else:
            fish_days[-1] = 0

        LOGGER.debug(f"day {i}: {fish_days=}")

    LOGGER.info(f"After {days} days: {fish_days}")

    return sum(fish_days)
