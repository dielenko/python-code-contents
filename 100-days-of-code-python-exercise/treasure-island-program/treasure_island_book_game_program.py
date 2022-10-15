welcome_book = (r'''
Welcome to the Treasure Island Book Game
****************************************

            /;
           / |'-,.
          /  '    `"---,.__
         /  '    ,'     ,  '"--,"|
        /  '    ,     ,'     ,"::|
       /  '   ,'    ,      ,"::::|
      /  '   ,    ,'     ,"::::::L
     /  '  ,'   ,'     ,"::::::::L
    /  '  ,    ,     ,":::::::::J
    k-,._    ,'   _.":::::::::::J
     \.  `"----'"".J::::::::::::|
      \.    .-,    .L:::::::::::|
       \.  (       .J:::::::::::!
        \.  `--     .L:::::::::/
         \.   .-.   .|::::::::/
          \. (   )  .J:::::::/
           \. `-'    .L:::::/
            \.  L    .|::::/
             \. !__  .J:::/
              \.  __  .L:/
               \. L_) .|/
                `-,__,-'
  ''')

print(welcome_book)
print('''
-------------------------------------------------------------------------------------------------
| If you open the right book page you will find the way to catch the treasure and win the game! |
-------------------------------------------------------------------------------------------------
''')

# Input Params
first_user_attempt = int(
    input('Which is your initial choice of page. The book size is 100 pages: \n'))


# Prepare the output images based on the user input
game_over_image = (r'''
                     __...__...__
              _..-"      `Y`      "-._
              \           |           /
              \\          |          //
              \\\         |         ///
               \\\ _..---.|.---.._ ///
                \\`_..---.Y.---.._`//
                 '`   Game Over   `'
''')

second_try_image = (r'''
                      _.--._  _.--._
              ,-=.-":;:;:;\':;:;:;"-._
              \\\:;:;:;:;:;\:;:;:;:;:;\
              \\\:;:;:;:;:;\:;:;:;:;:;\
                \\\:;:;:;:;:;\:;:;:;:;:;\ - Second try to find the Treasure island
                \\\:;:;:;:;:;\:;::;:;:;:\
                  \\\;:;::;:;:;\:;:;:;::;:\
                  \\\;;:;:_:--:\:_:--:_;:;\
                    \\\_.-"      :      "-._\
                    \`_..--""--.;.--""--.._=>
''')

win_game_image = (r'''
               __
              (`/\
              `=\/\ __...--~~~~~-._   _.-~~~~~--...__
                `=\/\               \ /               \\
                `=\/                V                 \\
                //_\___--~~~~~~-._  |  _.-~~~~~~--...__\\
                //  ) (..----~~~~._\ | /_.~~~~----.....__\\
              ==(Congratulations)=\\|//=====(You Win)=======
              ___\_____________/____________`-------`_______
''')

# Make a decision statement based on the user input and provide next steps in the game
if first_user_attempt >= 50 and first_user_attempt <= 80:
    print(
        f"Your choice is page *** {first_user_attempt} ***. That means you lose the game. Game Over!")
    print(game_over_image)

elif first_user_attempt >= 1 and first_user_attempt < 50:
    print(
        f"Your choice is page *** {first_user_attempt} ***. That means you have one more attempt to find the right way.")
    print(second_try_image)

    second_user_attempt = int(
        input('Which is your second choice of page. The book size is 100 pages: \n'))
    if second_user_attempt >= 1 and second_user_attempt <= 80:
        print(
            f"Your choice is page *** {second_user_attempt} ***. That means you lose the game. Game Over!")
        print(game_over_image)
    else:
        print(
            f"Your choice is page *** {second_user_attempt} ***. That means you win the game. Congratulations!")
        print(win_game_image)
else:
    print(
        f"Your choice is page *** {first_user_attempt} ***. That means you win the game. Congratulations!")
    print(win_game_image)
