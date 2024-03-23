# card_game_war

The War Card game is a simple yet engaging card game traditionally played by two players. This implementation of the game is created using Python and allows to simulate a game with two players.

## Requirements

- Python 3.6 or higher.
- No external libraries are required.

## Gameplay

The game is initiated by running the Python script from the command line. Each player draws the top card from their deck, and the player with the higher card wins the round, taking both cards. In the case of a tie, a "war" takes place, where each player places three cards face down and then one card face up. The player with the higher face-up card wins all the cards from that round. The game continues until one player has all the cards or a player can no longer continue the war, thereby losing the game.

## Additional Features

1. **Game History**:
   - After each game, a text file named `game_history.txt` is generated in the project directory.
   - The file contains a history of the last game played, detailing each turn taken by the players.

2. **Printing Logic**:
   - Each turn is logged in the `game_history.txt` file in a visually descriptive manner.
   - The format for each turn shows the cards played by each player and the number of cards remaining in their decks. The layout is as follows:

     ```
     Player 1's deck (40): [10♡]  vs  Player 2's deck (10): [J♧]
     ```

     Where the number in parentheses indicates the number of cards remaining in the player's deck after the turn is completed, and the bracketed symbols represent the card played by each player during the turn.

## Setup and Execution

To play the game, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the repository's directory in your terminal.
3. Run the game using the command `python war_game.py`.
4. Follow the on-screen prompts to enter each player's name.
5. The game will proceed automatically, and the winner will be announced at the end.
6. Check the `game_history.txt` file for a detailed log of the game's turns.

## Contribution

Feel free to fork this repository and contribute to its development. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
