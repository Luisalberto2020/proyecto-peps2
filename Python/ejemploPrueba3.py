def recuperar_numeros_primos(max_number):
    numbers = [True, True] + [True] * (max_number-1)
    last_prime_number = 2
    i = last_prime_number
    
    while last_prime_number**2 <= max_number:
        i += last_prime_number
        while i <= max_number:
            numbers[i] = False
            i += last_prime_number
        j = last_prime_number + 1
        while j < max_number:
            if numbers[j]:
                last_prime_number = j
                break
            j += 1
        i = last_prime_number
    
    return [i + 2 for i, not_crossed in enumerate(numbers[2:]) if not_crossed]
def es_primo(n):
    return n in recuperar_numeros_primos(n)
print(es_primo(12))