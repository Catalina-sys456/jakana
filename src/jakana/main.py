import sys
import random
Japanese = [("あ", "ア", "a"), ("い", "イ", "i"), ("う", "ウ", "u"), ("え", "エ", "e"), ("お", "オ", "o"), ("か", "カ", "ka"), ("き", "キ", "ki"), ("く", "ク", "ku"), ("け", "ケ", "ke"), ("こ", "コ", "ko"), ("さ", "サ", "sa"), ("し", "シ", "shi"), ("す", "ス", "su"), ("せ", "セ", "se"), ("そ", "ソ", "so"), ("た", "タ", "ta"), ("ち", "チ", "chi"), ("つ", "ツ", "tsu"), ("て", "テ", "te"), ("と", "ト", "to"), ("な", "ナ", "na"), ("に", "ニ", "ni"), ("ぬ", "ヌ", "nu"), ("ね", "ネ", "ne"), ("の", "ノ", "no"), ("は", "ハ", "ha"), ("ひ", "ヒ", "hi"), ("ふ", "フ", "fu"), ("へ", "ヘ", "he"), ("ほ", "ホ", "ho"), ("ま", "マ", "ma"), ("み", "ミ", "mi"), ("む", "ム", "mu"), ("め", "メ", "me"), ("も", "モ", "mo"), ("や", "ヤ", "ya"), ("ゆ", "ユ", "yu"), ("よ", "ヨ", "yo"), ("ら", "ラ", "ra"), ("り", "リ", "ri"), ("る", "ル", "ru"), ("れ", "レ", "re"), ("ろ", "ロ", "ro"), ("わ", "ワ", "wa"), ("を", "ヲ", "o"), ("ん", "ン", "n"), ("が", "ガ", "ga"), ("ぎ", "ギ", "gi"), ("ぐ", "グ", "gu"), ("げ", "ゲ", "ge"), ("ご", "ゴ", "go"), ("ざ", "ザ", "za"), ("じ", "ジ", "ji"), ("ず", "ズ", "zu"), ("ぜ", "ゼ", "ze"), ("ぞ", "ゾ", "zo"), ("だ", "ダ", "da"), ("ぢ", "ヂ", "ji"), ("づ", "ヅ","zu"), ("で", "デ", "de"), ("ど", "ド", "do"), ("ば", "バ", "ba"), ("び", "ビ", "bi"), ("ぶ", "ブ", "bu",), ("べ", "ベ", "be"), ("ぼ", "ボ", "bo"), ("ぱ", "パ", "pa"), ("ぴ", "ピ", "pi"), ("ぷ", "プ", "pu"), ("ぺ", "ペ", "pe"), ("ぽ", "ポ", "po")]

def Japanese_search(n):
    """
    Searches the Japanese list for a given Hiragana, Katakana, or Romaji character
    and prints the corresponding other forms.
    """
    found = False
    for var in Japanese:
        # Check if input matches Romaji
        if n == var[2]:
            print(f"Romaji '{n}' corresponds to: Hiragana '{var[0]}', Katakana '{var[1]}'")
            found = True
        # Check if input matches Hiragana
        elif n == var[0]:
            print(f"Hiragana '{n}' corresponds to: Katakana '{var[1]}', Romaji '{var[2]}'")
            found = True
        # Check if input matches Katakana
        elif n == var[1]:
            print(f"Katakana '{n}' corresponds to: Hiragana '{var[0]}', Romaji '{var[2]}'")
            found = True
    if not found:
        print(f"Could not find '{n}' in the list.")


def train():
    """
    Runs an interactive training session:
    Shows a random Katakana character and asks the user for the corresponding Hiragana.
    Continues until the user types 'exit'.
    """
    exit_word = ""
    print("--- Katakana to Hiragana Training ---")
    print("Enter the Hiragana for the Katakana shown.")
    print("Type 'exit' to quit.")
    print("-" * 35) # Separator line

    while exit_word != "exit":
        # Select a random index from the Japanese list
        number = random.randint(0, len(Japanese) - 1)
        # Get the Hiragana (correct_hiragana) and Katakana (katakana_char)
        # We don't need the Romaji here, so we use '_' as a placeholder
        correct_hiragana, katakana_char, _ = Japanese[number]

        # Display the Katakana character to the user
        print(f"Katakana: {katakana_char}")

        # Get user input for the corresponding Hiragana
        input_hiragana = input("Enter Hiragana > ")

        # Check if the user wants to exit
        exit_word = input_hiragana.lower() # Convert to lowercase for case-insensitive exit

        if exit_word == "exit":
            print("Exiting training. Goodbye!")
            break # Exit the loop immediately

        # Check if the input matches the correct Hiragana
        if input_hiragana == correct_hiragana:
            print("Correct! 😁")
        else:
            print(f"Incorrect 😭 The correct Hiragana is: {correct_hiragana}")

        print("") # Add a blank line for spacing between questions

def main():
    """
    Main function to determine whether to run search or training mode.
    """
    # Check if command-line arguments are provided (for search mode)
    if len(sys.argv) > 1:
        to_search = sys.argv[1]
        print(f"Searching for: {to_search}")
        Japanese_search(to_search)
    # Otherwise, run the training mode
    else:
        train()

# Standard Python entry point
if __name__ == "__main__":
    main()
