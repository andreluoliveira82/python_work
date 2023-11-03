
def count_characters(palavra):
    """
    Percorre cada caractere de uma string e retorna quantas vezes cada caractere ocorre
    """
    count_dict = {}

    for c in palavra:
        if c in count_dict:
            count_dict[c] += 1

        else:
            count_dict[c] = 1

    print(count_dict)
    return count_dict

# ---------------------------------------------------------------------------

count_characters("paralelepipedo")