# 1. Перевіряє, чи число є простим
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2. Класифікує вік
def classify_age(age):
    if age < 0:
        return "Invalid"
    elif age < 13:
        return "Child"
    elif age < 18:
        return "Teen"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

# 3. Конвертація оцінки у бал (літерний)
def grade_to_letter(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# 4. Розраховує знижку за кількістю товару
def calculate_discount(quantity, price_per_item):
    if quantity <= 0 or price_per_item <= 0:
        return 0
    total = quantity * price_per_item
    if quantity >= 100:
        return total * 0.2
    elif quantity >= 50:
        return total * 0.1
    else:
        return 0

# 5. Повертає найменше позитивне число в списку
def min_positive(lst):
    positives = [x for x in lst if x > 0]
    return min(positives) if positives else None

# 6. Обчислює плату за доставку залежно від ваги
def shipping_cost(weight):
    if weight <= 0:
        return 0
    elif weight <= 1:
        return 5
    elif weight <= 5:
        return 10
    elif weight <= 20:
        return 20
    else:
        return 50

# 7. Розпізнає тип трикутника за сторонами
def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    elif a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# 8. Повертає категорію ІМТ (індекс маси тіла)
def bmi_category(weight, height):
    try:
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    except ZeroDivisionError:
        return "Invalid height"

# 9. Конвертує час у форматі HH:MM в хвилини
def time_to_minutes(time_str):
    try:
        parts = time_str.split(":")
        hours = int(parts[0])
        minutes = int(parts[1])
        return hours * 60 + minutes
    except (ValueError, IndexError):
        return -1

# 10. Перевіряє пароль на складність
def is_strong_password(pw):
    if len(pw) < 8:
        return False
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    return has_upper and has_lower and has_digit

# 11. Повертає наступний день тижня
def next_day(current_day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if current_day not in days:
        return "Invalid day"
    idx = days.index(current_day)
    return days[(idx + 1) % 7]

# 12. Обчислює податок залежно від доходу
def calculate_tax(income):
    if income < 0:
        return 0
    elif income <= 10000:
        return income * 0.1
    elif income <= 50000:
        return 1000 + (income - 10000) * 0.2
    else:
        return 9000 + (income - 50000) * 0.3

# 13. Знаходить перший непарний елемент у списку
def first_odd(lst):
    for x in lst:
        if x % 2 != 0:
            return x
    return None

# 14. Визначає, чи рядок містить лише букви
def is_alpha_only(s):
    if not s:
        return False
    return s.isalpha()

# 15. Перевіряє, чи дата у форматі YYYY-MM-DD
def is_valid_date(date_str):
    try:
        year, month, day = map(int, date_str.split("-"))
        return 1 <= month <= 12 and 1 <= day <= 31
    except ValueError:
        return False

# 16. Симулює банкомат: знімає гроші, якщо вистачає
def atm_withdraw(balance, amount):
    if amount <= 0:
        return "Invalid amount"
    elif amount > balance:
        return "Insufficient funds"
    return balance - amount
