import random

res = {
    "['stone', 'scissors']": "User wins",
    "['scissors', 'stone']": "System wins",
    "['stone', 'paper']": "System wins",
    "['paper', 'stone']": "User wins",
    "['paper', 'scissors']": "System Wins",
    "['scissors', 'paper']": "User Wins"
}

sys_value = ["stone", "paper", "scissors"]
count = 0
i = 3
system_win_count = 0
user_win_count = 0

while i != count:
 user_input = input('> stone/paper/scissors : ').lower()
 system_value = random.choice(sys_value)
 print(system_value)
 if user_input == system_value:
     print("match draw")
 elif user_input != system_value:
    result = [user_input, system_value]
    match result:
          case ['stone', 'scissors']:
              print("User wins")
              user_win_count = user_win_count+1
          case ['scissors', 'stone']:
             print("System wins")
             system_win_count =system_win_count+1
          case ['stone', 'paper']:
             print("System wins")
             system_win_count = system_win_count + 1
          case ['paper', 'stone']:
             print("User wins")
             user_win_count = user_win_count + 1
          case ['paper', 'scissors']:
             print("System wins")
             system_win_count = system_win_count + 1
          case ['scissors', 'paper']:
             print("User wins")
             user_win_count = user_win_count + 1

    i = i - 1
print(f'SYSTEM_WIN_COUNT = {system_win_count } USER_WIN_COUNT = {user_win_count}')

