#INTRO TO IT 2nd COURSE
# Задача 8: Слова, слова, слова!
# Узнай количество слов в предложении.
def count_words(string):
    return len(string.split())

string = "Python прекрасен!"
print(f"В '{string}' {count_words(string)} слов")