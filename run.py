def is_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


res = is_anagrams('acificp', 'PACIFIC')
print(res)
