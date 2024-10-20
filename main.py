def all_variants(text):
    length = len(text)
    # Генерируем все возможные подпоследовательности
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield text[start:end]

# Использование функции-генератора
a = all_variants("abc")
for i in a:
    print(i)
