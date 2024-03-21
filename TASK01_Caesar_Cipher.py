  def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            if mode == 'encrypt':
                shifted = (ord(char) - ord('a') + shift) % 26 + ord('a') if char.islower() else (ord(char) - ord('A') + shift) % 26 + ord('A')
            elif mode == 'decrypt':
                shifted = (ord(char) - ord('a') - shift) % 26 + ord('a') if char.islower() else (ord(char) - ord('A') - shift) % 26 + ord('A')
            result += chr(shifted)
        else:
            result += char
    return result

  def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? : ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
            continue
        else:
            break

    text = input("Input your message: ")
    shift = int(input("Input shift value: "))

    if choice == 'encrypt':
        encrypted_text = caesar_cipher(text, shift, 'encrypt')
        print("Encrypted Message:", encrypted_text)
    elif choice == 'decrypt':
        decrypted_text = caesar_cipher(text, shift, 'decrypt')
        print("Decrypted Message:", decrypted_text)

  if __name__ == "__main__":
    main()