def check_special_char(input_str):
    if '@' in str(input_str):
        return f"Karakter '@' ditemukan: {input_str}"
    return "Karakter '@' tidak ditemukan."

# Contoh penggunaan
print(check_special_char("hello@world"))
print(check_special_char("helloworld"))