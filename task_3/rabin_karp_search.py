def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)  # Визначаємо довжину рядка s
    hash_value = 0  # Ініціалізуємо початкове значення хешу
    for i, char in enumerate(s):  # Проходимо по кожному символу рядка s
        power_of_base = pow(base, n - i - 1) % modulus  # Обчислюємо степінь основи base по модулю modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus  # Оновлюємо значення хешу
    return hash_value  # Повертаємо обчислене значення хешу

def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)  # Довжина підрядка
    main_string_length = len(main_string)  # Довжина основного рядка
    
    # Базове число для хешування та модуль
    base = 256  # Вибираємо базове число для хешування
    modulus = 101  # Вибираємо модуль для хешування
    
    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)  # Обчислюємо хеш для підрядка
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)  # Обчислюємо хеш для першого відрізка основного рядка, довжиною як підрядок
    
    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus  # Визначаємо множник для перерахунку хешу

    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:  # Якщо хеші збігаються, перевіряємо підрядок
            if main_string[i:i+substring_length] == substring:  # Перевіряємо, чи збігаються підрядки
                return i  # Якщо збігаються, повертаємо індекс початку підрядка

        if i < main_string_length - substring_length:  # Якщо ще є символи для перевірки
            # Перераховуємо хеш для наступного відрізка
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus  # Видаляємо вплив першого символу попереднього відрізка
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus  # Додаємо вплив нового символу
            if current_slice_hash < 0:  # У разі негативного хешу, коригуємо його
                current_slice_hash += modulus

    return -1  # Якщо підрядок не знайдено, повертаємо -1