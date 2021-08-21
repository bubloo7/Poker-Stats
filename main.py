import os
import csv


def loadCSV(fileName):
    data = []
    with open("./data/" + fileName, mode='r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            if row[0] == "Name":
                continue
            temp = {
                "Name": row[0],
                "Buy in": float(row[1]),
                "Cash out": float(row[2]),
            }
            data.append(temp)

    for i in range(len(data)):
        data[i]["Net Gain/Loss"] = round(data[i]
                                         ["Cash out"] - data[i]["Buy in"], 2)
        data[i]["Percentage Gain"] = str(round(
            (data[i]["Net Gain/Loss"]/data[i]["Buy in"]) * 100, 2)) + "%"

    data = sorted(
        data, key=lambda k: k["Net Gain/Loss"]/k["Buy in"], reverse=True)

    for i in range(len(data)):
        data[i]["Rating"] = round(((len(data) - i)/len(data) + (
            float(data[i]["Percentage Gain"][:-1]))/500) * (1 + .05*(len(data)-2)), 2)
    with open("Game Stats/" + fileName[:-4] + " — Stats.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
                                "Name", "Buy in", "Cash out", "Net Gain/Loss", "Percentage Gain", "Rating"])
        writer.writeheader()
        for d in data:
            writer.writerow(d)
    return data


def avgStats(gameStats):
    stats = {}

    for data in gameStats:
        for user in data:
            if user["Name"] in stats:
                stats[user["Name"]] = {
                    "Games Played": stats[user["Name"]]["Games Played"] + 1,
                    "Total Invested": round(stats[user["Name"]]["Total Invested"] + user["Buy in"], 2),
                    "Total Cashed Out": round(stats[user["Name"]]["Total Cashed Out"] + user["Cash out"], 2),
                    "Total Gain/Loss": round(stats[user["Name"]]["Total Gain/Loss"] + user["Net Gain/Loss"], 2),
                    "Rating": round(((stats[user["Name"]]["Games Played"] * stats[user["Name"]]["Rating"]) + user["Rating"])/(stats[user["Name"]]["Games Played"] + 1), 2),
                }
                stats[user["Name"]]["Percentage Gain"] = str(round(
                    (stats[user["Name"]]["Total Gain/Loss"]/stats[user["Name"]]["Total Invested"]) * 100, 2)) + "%"
            else:
                stats[user["Name"]] = {
                    "Name": user["Name"],
                    "Games Played": 1,
                    "Total Invested": user["Buy in"],
                    "Total Cashed Out": user["Cash out"],
                    "Total Gain/Loss": user["Net Gain/Loss"],
                    "Rating": user["Rating"],
                    "Percentage Gain": user["Percentage Gain"]
                }
    newData = []
    for dict in stats:
        temp = stats[dict]
        temp["Name"] = dict
        newData.append(temp)

    with open("Stats.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
                                "Name", "Total Invested", "Total Cashed Out", "Total Gain/Loss",  "Percentage Gain", "Rating", "Games Played"])
        writer.writeheader()
        for d in newData:
            writer.writerow(d)


def main():
    fileNames = os.listdir("./data")
    gameStats = []
    for fileName in fileNames:
        gameStats.append(loadCSV(fileName))

    avgStats(gameStats)


if __name__ == "__main__":
    main()
