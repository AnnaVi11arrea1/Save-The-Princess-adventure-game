print('''
                   (   .                   _ _ _ _ _
    (   .     .  .=##                      ]-I-I-I-[                    /
  .=##   .  (      ( .                     \ `  ' /        \\\' ,      / //
    ( .   .=##  .       .                   |'  []          \\\//    _/ //'
  .     .   ( .    .        _----|          |.  '|           \_-//' /  //<'
                             ----|_----|    | ' .|             \ ///  >   \\\`
    ]-I-I-I-I-[       ----|      |     |    |. ` |            /,)-^>>  _\`
     \ `   '_/            |     / \    |    | /^\|            (/   \\ / \\\
      []  `__|            ^    / ^ \   ^    | |*||                  //  //\\\
      |__   ,|           / \  / ^ ^`\ / \   | ===|                 ((`
   ___| ___ ,|__        / ^  /=_=_=_=\ ^ \  |, `_|
   I_I__I_I__I_I       (====(_________)_^___|____|____                 
   \-\--|-|--/-/       |     I  [ ]__I I_I__|____I_I_|                     
    |[] `    '|__   _  |_   _|`__  ._[  _-\--|-|--/-/                      
   / \  [] ` .|  |-| |-| |-| |_| |_| |_| | []   [] |                
  <===>    `  |.            .      .     |    '    |
  ] []|  `    |   []    --   []      `   |   [] '  |
  <===>.  `   |  .   '  .       '  .[]   | '       |             
   \_/    .   |       .       '          |   `  [] |           
    | []    . |   .  .           ,  .    | ,    .  |                   
    |    . '  |       . []  '            |    []'  |
   / \   ..   |  `      .    .     `[]   | -   `   |                     
  <===>      .|=-=-=-=-=-=-=-=-=-=-=-=-=-|    .   / \                   
  ] []|` ` [] |`  .  .   _________   .   |-      <===>            
  <===>  `  ' | '   |||  |       |  |||  |  []   <===>                      
   \_/     -- |   . |||  |       |  |||  | .  '   \_/                     
  ./|' . . . .|. . .||||/|_______|\|||| /|. . . . .|\_
''')

print("Welcome to Princess Journey.")
print("Your mission is to save the princess.") 



choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left", "right", or "straight" \n')
if choice1 == "left":
          print("You cross a rickety bridge. You are safe.")
          choice2 = input('You arrive at a grassy knoll.. Where do you want to go? Type "left" or "straight" \n')
          if choice2 == "straight":
                    print("You have found an invisible cloak. You are safe.")
                    choice3 = input("You feel like you are being watched. Where do you want to go? Type 'left' or 'right' \n")
                    if choice3 == "left":
                              print("You have found the castle.")
                              choice4 = input("Enter the castle? Type 'yes' or 'no' \n")
                              if choice4 == "yes":
                                        print("You sneak past the gaurds with your invisible cloak.")
                                        choice5 = input("Stone walls surround the corridors. Which way do you want to go? Type 'left' or 'right' \n")
                                        if choice5 == "left":
                                                  print("You got lost in the castle. Game Over.")
                                        elif choice5 == "right":
                                                  print("You found the princess. You Win!")
                              elif choice4 == "no":
                                        print("The dragon emerges and engulfs you in flames. Game Over.")
                    elif choice3 == "right":
                              print("You are lost in an open field. \n")
                              choice6 = input("Which way do you want to go? Type 'left', 'right', or 'straight' \n")
                              if choice6 == "left":
                                        print("You have found the castle. \n")
                                        choice7 = input("How do you want to approach? Type 'left', 'right', or 'straight' \n")
                                        if choice7 == "left":
                                                  print("A monster arrises from the moat and attacks you. Game Over.")
                                        elif choice7 == "right":
                                                  print("The drawbridge slams open! \n")
                                                  choice8 = input("You are momentarily frozen by fear. What happens? Type 'scream', 'pee pants', or 'enter' \n")
                                                  if choice8 == "scream":
                                                            print("Attacked by a giant spider with huge fangs. Game Over. \n")
                                                  elif choice8 == "pee pants":
                                                            print("You have drowned in your own excrement. Game Over. \n")
                                                  elif choice8 == "enter":
                                                            print("Using your invisible cloak, you sneak past the gaurds and save the princess. You win! \n")
                                        elif choice7 == "straight":
                                                  print("Attacked by thieves. Game Over. \n")
                              elif choice6 == "right":
                                        print("A dragon swoops in and sets the field aflame. Game Over. \n")
                              elif choice6 == "straight":
                                        print("RAIDERS! You are captured. Game Over. \n")
          if choice2 == "left":
                    print("You are struck by lightening. Game Over. \n")
elif choice1 == "right":
          print("You get stuck in a bear trap and bleed to death. Game Over. \n")
elif choice1 == "straight":
          print("You hear a roar in the distance. \n")
          choice9 = input("Which way do you want to go? Type 'left', 'right' or 'straight' \n")
          if choice9 == "left":
                    print("You are traversing the badlands. \n ")
                    choice10 = input("You see smoke on the horizon. Which way do you go? Type 'left', 'right', or 'straight' \n")
                    if choice10 == "left":
                              print("You have found the castle. \n")
                              choice11 = input("How do you want to approach? Type 'left', 'right', or 'straight' \n")
                              if choice11 == "left":
                                        print("A monster arrises from the moat and attacks you. Game Over. \n")
                              elif choice11 == "right":
                                        print("The drawbridge opens shakey and unevenly. \n")
                                        choice12 = input("You search for your courage. What happens? Type 'scream', 'pee pants', or 'enter' \n")
                                        if choice12 == "scream":
                                                  print("You are swarmed by spiders of all sizes. Game Over. \n")
                                        elif choice12 == "pee pants":
                                                  print("The wolves smell your scent and surround you slowly for an attack. Game Over. \n")
                                        elif choice12 == "enter":
                                                  print("You sport your invisible cloak and find the princess inside. You win! \n")
                              elif choice11 == "straight":
                                        print("A demented oger adopts you as his pet. Game Over. \n")
                    elif choice10 == "right":
                              print("You are attacked by a dragon. Game Over. \n")
                    elif choice10 == "straight":
                              print("You are kidknapped by a cult of dark elves. Game Over. \n")
          elif choice9 == "right":
                    print("You enter the woods. \n")
                    choice13 = input("You see tracks. Which way do you want to go? Type 'left', 'right', or 'straight' \n")
                    if choice13 == "left":
                              print("Attacked by bandits. Game Over. \n")
                    elif choice13 == "right":
                              print("Quicksand traps youe in. Game Over. \n")
                    elif choice13 == "straight":
                              print("You find a magical weapon in a tree. \n")
                              choice14 = input("How do you progress thorugh the forest? Type 'left', 'right', or 'straight' \n")
                              if choice14 == "straight":
                                        print("Arrow to the knee, you cannot walk. Game Over. \n")
                              elif choice14 == "right":
                                        print("You find a cross bridge covered in vines streching over a canyon. \n")
                                        choice15 = input("How do you cross? Type 'vines' or 'walk' \n")
                                        if choice15 == "vines":
                                                  print("You grab 3 vines for security and jump. You are a real tarzan. \n")
                                                  choice16 = input("The back entrance of the castle is on this side! How do you approach? Type 'attack' or 'sneak' \n")
                                                  if choice16 == "attack":
                                                            print("The magical weapon is no match for the gaurds. You win! \n")
                                                  elif choice16 == "sneak":
                                                            print("Your armor is too noisey! You are captured by the gaurds. Game Over. \n" )
                                        elif choice15 == "walk":
                                                  print("The bridge was a facade of black magic and you fall 1000 feet. Game Over. \n")
                              elif choice14 == "left":
                                        print("You see smoke in the distance. \n ")
                                        choice17 = input("Which way do you want to go? Type 'left' or 'straight' \n")
                                        if choice17 == "left":
                                                  print("A dragon attacks, but is no match for your magical weapon. You are now a hero. You win! \n")
                                        elif choice17 == "straight":
                                                  print("You find the castle. \n")
                                                  choice18 = input("How do you enter? Type 'climb' or 'sewer \n")
                                                  if choice18 == "climb":
                                                            print("A dragon attack as you scale the castle walls. Your magical weapon protects you. \n")
                                                            choice19 = input("You reach the top of the castle. Which wing do you want to go? Type 'left' or 'right' \n")
                                                            if choice19 == "left":
                                                                      print("You save the princess! You win. \n")
                                                            elif choice19 == "right":
                                                                      print("The princess is mad that you took so long, but you still win. \n")
                                                  elif choice18 == "sewer":
                                                            print("Attacked by sludge monster. Your magic weapon protects you. \n")
                                                            choice20 = input("What happens next?. Type 'sneak' or 'stank' \n")
                                                            if choice20 == "sneak":
                                                                      print("You successfullly sneak past the gaurds and save the princess. You win! \n")
                                                            elif choice20 == "stank":
                                                                      print("Your smell attracts the attention of the gaurds. Game Over. \n")
          elif choice9 == "straight":
                    print("You have quickly found the castle. \n")
                    choice21 = input("How do you approach? Type 'left', 'right', or 'straight' \n")
                    if choice21 == "left":
                              print("You are scorched by an angry dragon. Game Over. \n")
                    elif choice21 == "right":
                              print("You ate a diseased wombat earlier. Game Over. \n")
                    elif choice21 == "straight":
                              print("There is a hole where the drawbridge is supposed to be. \n" )
                              choice22 = input("How do you enter? Type 'sneak' or 'swim' \n")
                              if choice22 == "sneak":
                                        print("You are not sneaky enough. Game Over. \n")
                              elif choice22 == "swim":
                                        print("The water is freezing but you make it across the moat alive and save the princess. You Win!\n ")