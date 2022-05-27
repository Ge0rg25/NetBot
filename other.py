import Database

db = Database.DateB()


def get_short_groups_for_lambda():
    groups = db.get_all_group()

    short_groups = []

    for group in groups:
        short_groups.append(f'short-{group[0]}')
    return short_groups


def get_long_groups_for_lambda():
    groups = db.get_all_group()

    long_groups = []

    for group in groups:
        long_groups.append(f'long-{group[0]}')
    return long_groups

