with open('cyrillic.txt', encoding='utf-8') as file_text, open('transliteration.txt', 'w', encoding='utf-8') as file_result:
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'jo', 'ж': 'zh', 'з': 'z', 'и': 'i',
         'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
         'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shh', 'ъ': '*', 'ы': 'y', 'ь': "'", 'э': 'je',
         'ю': 'ju', 'я': 'ya'}

    text = file_text.read()
    result = ''
    for char in text:
        char_lower = char.lower()
        if char_lower in d:
            result += d[char] if char.islower() else d[char_lower].title()
        else:
            result += char
    file_result.write(result)
