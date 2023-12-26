import random

a = str(input('Assalomu alaykum hurmatli bilimdon ismingiz nima ? '))
print(f"Siz bilan biz o'yin o'ynaymiz rozimisiz {a} ?")
        

words = ["tiger", "tree", "underground", "giraffe", "chair","lion","home", "family", "Suhrob", "developer","name","father","mother","english"]
selected_word = random.choice(words)

print(f"Men bir so'z tanladim {a}. Harfni topa olasizmi ?")

correct_guesses = []
wrong_guesses = []
max_wrong_guesses = 5

while True:
    letter = input( f"Harfni kiriting {a}: ").lower()

    if letter in selected_word:
        if letter not in correct_guesses:
            correct_guesses.append(letter)
        else:
            print(f"Bu harf allaqachon topilgan {a} !")
    else:
        if letter not in wrong_guesses:
            wrong_guesses.append(letter)
            max_wrong_guesses -= 1
        else:
            print(f"Bu harfga allaqachon urinib ko'rgansiz {a}! ")

    word_progress = ""
    for char in selected_word:
        if char in correct_guesses:
            word_progress += char + " "
        else:
            word_progress += "_ "

    print(word_progress)

    if set(correct_guesses) == set(selected_word):
        print(f"Tabriklaymiz! {a} Siz yutdingiz!")
        break

    if max_wrong_guesses == 0:
        print(f"Afsuski {a} siz yutqazdingiz!")
        break



# import random

# words = ["tiger", "tree", "underground", "giraffe", "chair"]
# selected_word = random.choice(words)

# def play_game():
 
#     guess_word = []
#     for _ in range(len(selected_word)):
#         guess_word.append("_")

# wrong_guesses = 0
# max_wrong_guesses = 5

# while wrong_guesses < max_wrong_guesses:
#     print(" ".join(guess_word))
#     guessed_letter = input("Harf kiriting: ")

# correct_guess = False

# for i in range(len(selected_word)):
#     if selected_word[i] == guessed_letter:
#         guess_word[i] = guessed_letter
# correct_guess = True

# if not correct_guess:
#      wrong_guesses += 1

# if "_" not in guess_word:
#     print("Tabriklaymiz! Siz o'yinga g'olib bo'ldingiz.")
#     return

# print("Noto'g'ri urinishlar soni:", wrong_guesses)

# print("Yutqazdingiz! Tanlangan so'z:", selected_word)

# play_game()