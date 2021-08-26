# https://app.codesignal.com/arcade/intro/level-4/cC5QuL9fqvZjXJsW9
def alternating_sums(weights):
    team_1 = []
    team_2 = []

    for i in range(len(weights)):
        if i % 2 == 0:
            team_1.append(weights[i])
        else:
            team_2.append(weights[i])

    return [sum(team_1), sum(team_2)]


input_user = [50, 60, 60, 45, 70]
print(alternating_sums(input_user))
