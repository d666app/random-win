import random, os, json


def analyze_and_update_top():

   # code to collect data from your database

data = analyze_and_update_top()

def choose_winners(data, num_winners):

    id_xp_pairs = [(d["id"], d["xp"]) for d in data]

    winners = []

    while len(winners) < num_winners:
        id_xp_pairs.sort(key=lambda x: x[1], reverse=True)

        total_xp = sum(xp for _, xp in id_xp_pairs)
        probabilities = [xp / total_xp for _, xp in id_xp_pairs]

        winner_index = random.choices(range(len(id_xp_pairs)), probabilities)[0]
        winner = id_xp_pairs[winner_index]

        id = winner[0]

        data_user = ... # code to collect data from your database

        if 'connected_wallet' in data_user and 'JVT' in data_user['tasks']:
            winners.append(winner[0])

        del id_xp_pairs[winner_index]

    return winners

winners = choose_winners(data, 100)

print("Победители:")
print(winners)
