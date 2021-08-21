# Poker-Stats
Quickly calculate stats for your own poker games to see how well you and your friends are playing!
## What does it do?
I made this program because I've been playing a lot of poker with friends recently and wanted to see how well I was doing. As such, this application will let you calculate stats for individual games, as well as all games in total. For example, you can see your total percentage gained for each game or how much money you've won across all your games.
## How do I use it?
Using the program is simple. Each game is represented by a .csv file. The file should have three columns: "Name", "Buy In", and "Cash Out". Fill the rows appropriately. There are some examples in the data folder already incase you need help. Drop the file into the data folder and you are done! You can add as many games into the program as you would like. You can run the program with:
```
python main.py
```
This will create a few more .csv files with all the stats. Under the game stats directory, you will find .csv files that contain stats on each individual game. In the project directory, you will find Stats.csv which will contain stats based on all the games you've played.
## What the heck is rating??
I wanted to create an objective rating system to see who the best player is. The rating for a player in a single game is calculated by the following formula:
```
((Number of Players - Position + 1)/Number of Players + (Percentage Gained / 500)) * (1 + (Number of Players - 2) * .05) 
```
This system takes into account the position the player finished in, the number of players in the game, and how much money the player lost or gained. The rating of a player across multiple games is the average rating of the player across those games. The higher the rating, the stronger the player is. For example, a player with a rating of over 1.0 is either consistantly finishing first place or is always winning a lot of money. 
