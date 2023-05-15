def unique_morse_code_words(words):
    # Create a dictionary that maps each letter to its Morse code.
    morse_dict = { 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
                   'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
                   'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
                   'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'
                 }
    
    # Compute the transformation for each word and store it in a set.
    transformations = set()
    for word in words:
        transformation = ''.join(morse_dict[c] for c in word)
        transformations.add(transformation)
    
    # Return the number of different transformations.
    return len(transformations)
words = ["gin", "zen", "gig", "msg"]
print(unique_morse_code_words(words))