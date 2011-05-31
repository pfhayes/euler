// We have a strip of paper n squares long. On each turn, a player picks two
// adjacent squares and colors them in. The first player who cannot loses.
// For how many values of n <= 1000000 can the first player win?

// Note that, in general, each move divides the game into two subgames.
// Note furthermore that, depending on the split, it may be in the player's
// best interest to lose the subgame in order to win the full game! So, for
// each game we will track to see if it is possible for the player to guarantee
// a win for themselves, as well as a for a player to guarantee a loss for
// themselves. A game the player can win or lose is called a choice game.

// 1 means the next player must win, 0 means they lose
// 2 means that they are able to choose whether they want to win or lose!

// Observe that if n is even, then first player can always win. They play their
// first move in the middle, and then they mirror their opponents moves in the
// opposite half for the rest of the game.

// In order to win, the player wants to make a choice such that either
//   a) Both games are must win or must lose
//   b) Both games are identical choice games (make same choice as opponent).

// In order to be able to lose, there must be a split such that
//   a) One game is must win/must lose
//   b) Both games are identical choice games (make opposite choice from opponent).

// However, it may be that there is a split that splits the game into
// two different choice games - it will require further investigation to see
// when it is possible for the player to force a win or loss in these games.

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#define true (0 == 0)
#define false !true
#define BOUND 1000*1000

int main() {
  char* results = malloc(sizeof(char) * (BOUND + 1));

  // Given in problem
  results[0] = 0;
  results[1] = 0;
  results[2] = 1;
  results[3] = 1;
  results[4] = 2;
  results[5] = 0;

  int count = 3;
  for (int i = 6; i <= BOUND; ++i) {
    int canWin = false;
    int canLose = false;
    // If there are an even number of spaces, you can play in the middle,
    // and then mirror the opponents moves to win. Furthermore,
    // if both games are choice games, then you can make the opposite choice
    // to lose.
    if (i % 2 == 0) {
      canWin = true;
      if (results[i/2 - 1] == 2) {
        canLose = true;
      }
    }

    if (!canWin || !canLose) {
      for (int j = 0; j < i/2; ++j) {
        if (results[j] == results[i - 2 - j]) {
          if (results[j] != 2) {
            // If the game can be split into two games that are both must-win or
            // must-lose, then the player can win.
            canWin = true;
            if (canLose) {
              break;
            }
          } else {
            // This is a split into two choice games!
          }
        } else {
          if (results[j] != 2 && results[i - j - 2] != 2) {
            // If the game is split into one win game and one lose game, then the
            // player can lose.
            canLose = true;
            if (canWin) {
              break;
            }
          } else {
            // This is a split into a choice game and a non-choice game!
          }
        }
      }
    }
    
    if (canWin && canLose) {
      results[i] = 2;
      ++count;
    } else if (canWin) {
      results[i] = 1;
      ++count;
    } else {
      results[i] = 0;
      printf("%d, %d\n", i, results[i]);
    }
  }

  printf("%d\n", count);

  free(results);
}
