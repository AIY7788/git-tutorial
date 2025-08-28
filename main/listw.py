

word = ('''What this program does is check to see if word is palindrome
         by starting with the first and last characters of string and 
        comparing them If they are the same it works its way inward until 
        it has completed all the letter or the number of letters is odd in 
        which case the middle letter is ignored''').lower()

word = word.split(' ')

hangman_art = {0:("   ",
                  "   ",
                  "   "),

               1:(" o ",
                  "   ",
                  "   "),

               2:(" o ",
                  " | ",
                  "   "),

               3:(" o ",
                  "/| ",
                  "   "),

               4:(" o ",
                  "/|\\",
                  "   "),

               5:(" o ",
                  "/|\\",
                  "/  "),

               6:(" o ",
                  "/|\\",
                  "/ \\")}
