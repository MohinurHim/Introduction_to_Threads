# Задача "Потоковая запись в файлы":
import threading
import time
from datetime import datetime
from time import sleep
def write_words(word_count, file_name):
    # word_count - количество записываемых слов,
    # file_name - название файла, куда будут записываться слова
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")
# Взятие текущего времени
time_start = datetime.now()
# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
# Взятие текущего времени
time_stop = datetime.now()
# Вывод разницы начала и конца работы функций
time_result = time_stop - time_start
print(f'Время работы функций {time_result}')
#Взятие текущего времени
time_start2 = datetime.now()
# Создание и запуск потоков с аргументами из задачи
thread = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
#Запустите эти потоки методом start
thread.start()
thread2.start()
thread3.start()
thread4.start()
# Сделайте остановку основного потока при помощи join
thread.join()
thread2.join()
thread3.join()
thread4.join()
# #Взятие текущего времени
time_stop2 = datetime.now()
# Вывод разницы начала и конца работы потоков
time_result2 = time_stop2 - time_start2
print(f'Время работы потоков {time_result2}')