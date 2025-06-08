import sys
import random
import yaml
import os
import datetime

Japanese = [("あ", "ア", "a"), ("い", "イ", "i"), ("う", "ウ", "u"), ("え", "エ", "e"), ("お", "オ", "o"), ("か", "カ", "ka"), ("き", "キ", "ki"), ("く", "ク", "ku"), ("け", "ケ", "ke"), ("こ", "コ", "ko"), ("さ", "サ", "sa"), ("し", "シ", "shi"), ("す", "ス", "su"), ("せ", "セ", "se"), ("そ", "ソ", "so"), ("た", "タ", "ta"), ("ち", "チ", "chi"), ("つ", "ツ", "tsu"), ("て", "テ", "te"), ("と", "ト", "to"), ("な", "ナ", "na"), ("に", "ニ", "ni"), ("ぬ", "ヌ", "nu"), ("ね", "ネ", "ne"), ("の", "ノ", "no"), ("は", "ハ", "ha"), ("ひ", "ヒ", "hi"), ("ふ", "フ", "fu"), ("へ", "ヘ", "he"), ("ほ", "ホ", "ho"), ("ま", "マ", "ma"), ("み", "ミ", "mi"), ("む", "ム", "mu"), ("め", "メ", "me"), ("も", "モ", "mo"), ("や", "ヤ", "ya"), ("ゆ", "ユ", "yu"), ("よ", "ヨ", "yo"), ("ら", "ラ", "ra"), ("り", "リ", "ri"), ("る", "ル", "ru"), ("れ", "レ", "re"), ("ろ", "ロ", "ro"), ("わ", "ワ", "wa"), ("を", "ヲ", "o"), ("ん", "ン", "n"), ("が", "ガ", "ga"), ("ぎ", "ギ", "gi"), ("ぐ", "グ", "gu"), ("げ", "ゲ", "ge"), ("ご", "ゴ", "go"), ("ざ", "ザ", "za"), ("じ", "ジ", "ji"), ("ず", "ズ", "zu"), ("ぜ", "ゼ", "ze"), ("ぞ", "ゾ", "zo"), ("だ", "ダ", "da"), ("ぢ", "ヂ", "ji"), ("づ", "ヅ","zu"), ("で", "デ", "de"), ("ど", "ド", "do"), ("ば", "バ", "ba"), ("び", "ビ", "bi"), ("ぶ", "ブ", "bu",), ("べ", "ベ", "be"), ("ぼ", "ボ", "bo"), ("ぱ", "パ", "pa"), ("ぴ", "ピ", "pi"), ("ぷ", "プ", "pu"), ("ぺ", "ペ", "pe"), ("ぽ", "ポ", "po")]

def Japanese_search(n):
    found = False
    for var in Japanese:
        if n == var[2]:
            print(f"Romaji '{n}' corresponds to: Hiragana '{var[0]}', Katakana '{var[1]}'")
            found = True
        elif n == var[0]:
            print(f"Hiragana '{n}' corresponds to: Katakana '{var[1]}', Romaji '{var[2]}'")
            found = True
        elif n == var[1]:
            print(f"Katakana '{n}' corresponds to: Hiragana '{var[0]}', Romaji '{var[2]}'")
            found = True
    if not found:
        print(f"Could not find '{n}' in the list.")

def train_kana():
    exit_word = ""
    print("\n--- Katakana to Hiragana Training ---")
    print("Enter the Hiragana for the Katakana shown.")
    print("Type 'exit' to quit.")
    print("-" * 35)

    while exit_word != "exit":
        number = random.randint(0, len(Japanese) - 1)
        correct_hiragana, katakana_char, _ = Japanese[number]

        print(f"Katakana: {katakana_char}")

        input_hiragana = input("Enter Hiragana > ")
        exit_word = input_hiragana.lower()

        if exit_word == "exit":
            print("Exiting training. Goodbye!")
            break

        if input_hiragana == correct_hiragana:
            print("Correct! 😁")
        else:
            print(f"Incorrect 😭 The correct Hiragana is: {correct_hiragana}")

        print("")

def train_romaji():
    exit_word = ""
    print("\n--- Hiragana/Katakana to Romaji Training ---")
    print("Enter the Romaji for the characters shown.")
    print("Type 'exit' to quit.")
    print("-" * 42)

    while exit_word != "exit":
        number = random.randint(0, len(Japanese) - 1)
        hiragana_char, katakana_char, correct_romaji = Japanese[number]

        print(f"Characters: {hiragana_char} / {katakana_char}")

        input_romaji = input("Enter Romaji > ")
        exit_word = input_romaji.lower()

        if exit_word == "exit":
            print("Exiting training. Goodbye!")
            break

        if input_romaji.lower() == correct_romaji.lower():
            print("Correct! 😁")
        else:
            print(f"Incorrect 😭 The correct Romaji is: {correct_romaji}")

        print("")

def write_wrong_exercises(wrong_exercises, wrong_exercises_folder_path):
    file_name = f'{datetime.date.today()}.yml'
    file_path = os.path.join(wrong_exercises_folder_path, file_name)
    if wrong_exercises != None:
        with open(file_path, 'a') as file:
            yaml.dump(wrong_exercises, file, explicit_start=True)

def train_from_folder(folder_path, record):
    try:
        #choose file
        all_file_names = os.listdir(folder_path)
        counter = 0
        print('Choose a file')
        for file_name in all_file_names:
            counter += 1
            print(f'{counter}: {file_name}')
        choice = input('Enter our choice (number): ')
        file_number = int(choice)
        #questions
        if isinstance(file_number, int) and file_number > 0 and file_number <= counter:
            file_number = file_number -1
            chosed_file = all_file_names[file_number]
            file_path = os.path.join(folder_path, chosed_file)
            total_question = 0
            correct_answer = 0
            with open(file_path) as exercise_file:
                all_exercises = yaml.safe_load_all(exercise_file)
                for exercise in all_exercises:
                    total_question += 1
                    topic = exercise['topic']
                    solution = exercise['solution']
                    print(topic)
                    get_answer = input('Your answer:')
                    if get_answer == solution:
                        correct_answer += 1
                        print('Correct! 😁')
                    elif record == True:
                        #record mistakes
                        wrong_exercises_path = os.path.join(os.path.expanduser('~'), '.config/jakana/mistakes')
                        write_wrong_exercises(exercise, wrong_exercises_path)
                        
                        print('Incorrect 😭 The corret answer is :')
                        print(solution)
                    else:
                        print('Incorrect 😭 The corret answer is :')
                        print(solution)

                #percentage and print 
                percentage = lambda x , y: f'{x / y * 100}%'
                accuracy = percentage(correct_answer, total_question)
                print(f'Total {total_question} questions, correct answer is {correct_answer}, accuracy{accuracy} ')
        else:
            print('\nPlease enter correct number!\n')
            train_from_folder(folder_path, record)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception:
        print('Error: Unknow error')

def main():
    if len(sys.argv) > 1:
        for word in sys.argv:
            to_search = word
            print(f"Searching for: {to_search}")
            Japanese_search(to_search)
    else:
        while True:
            print("\nChoose a mode:")
            print("1: Train Romaji (from Hiragana/Katakana)")
            print("2: Train Hiragana (from Katakana)")
            print("3: Train custom exercises from (from .config/jakana/exercises)")
            print("4: Train thr question you're done wrong (from .config/jakana/mistakes)")
            print("5: Exit")
            choice = input("Enter your choice (number): ")

            if choice == '1':
                train_romaji()
                break
            elif choice == '2':
                train_kana()
                break
            elif choice == '3':
                folder_path =  os.path.join(os.path.expanduser('~'), '.config/jakana/exercises')
                record = True
                train_from_folder(folder_path, record)
                break
            elif choice == '4':
                folder_path =  os.path.join(os.path.expanduser('~'), '.config/jakana/mistakes')
                record = False
                train_from_folder(folder_path, record)
                break
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

