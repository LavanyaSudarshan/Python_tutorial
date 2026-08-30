s1="Listen"
s2="silent"

if sorted(s1.lower()) == sorted(s2.lower()):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

#using Dictionary (hashmap equivalent)
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    freq = {}

    # Count characters from s1
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    # Subtract using s2
    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1

        if freq[ch] == 0:
            del freq[ch]

    return len(freq) == 0
print("Anagram" if is_anagram("listen", "silent") else "Not Anagram")    