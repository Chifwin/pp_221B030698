def reverse_sentence(s: str):
    return " ".join(reversed(s.split()))

if __name__ == "__main__":
    s = input("Enter sentense: ")
    print("Sentence with the words reversed: ", reverse_sentence(s))
