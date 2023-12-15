import cmudict
import re


def main():
    phrase_to_placeholder_override()


def generate_duplicate_phoneme_words():
    duplicated_phonemes = 2
    for binary in cmudict.dict_stream():
        [word, *phonemes] = binary.decode('ascii').split()
        for i in range(len(phonemes) - duplicated_phonemes):
            for j in range(i + duplicated_phonemes, len(phonemes) - duplicated_phonemes):
                k = 0
                while k < duplicated_phonemes and phonemes[i + k] == phonemes[j + k]:
                    k += 1
                if k == duplicated_phonemes:
                    print(word, phonemes)

def phrase_to_placeholder_override():
    phrase = ""
    result = ""
    for word in re.split(" ", phrase):
        if word.isalpha():
            result += str(len(word)) + " "
        else:
            result += word + " "
    print(result)

if __name__ == "__main__":
    main()
