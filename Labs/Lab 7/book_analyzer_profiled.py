"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""


class BookAnalyzerProfiled:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = [",", "*", ";", ".", ":", "(", "[", "]", ")"]

    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        with open(src, mode='r', encoding='utf-8') as book_file:
            self.text = book_file.readlines()
        self.text = [line for line in self.text if line != "\n"]

        words = []
        for line in self.text:
            words += line.split()
        self.text = words

        temp_text = []
        for word in self.text:
            temp_word = word
            for punctuation in self.COMMON_PUNCTUATION:
                temp_word = temp_word.replace(punctuation, '')
            temp_text.append(temp_word)
        self.text = temp_text

    @staticmethod
    def is_unique(word, word_list):
        """
        Checks to see if the given word appears in the provided sequence.
        This check is case in-sensitive.
        :param word: a string
        :param word_list: a sequence of words
        :return: True if not found, false otherwise
        """
        for a_word in word_list:
            if word == a_word.lower():
                return False
        return True

    def find_unique_words(self):
        """
        Filters out all the words in the text.
        :return: a list of all the unique words.
        """
        temp_text = self.text
        unique_words = []
        while temp_text:
            word = temp_text.pop().lower()
            if self.is_unique(word, temp_text):
                unique_words.append(word)
        return unique_words


def main():
    book_analyzer = BookAnalyzerProfiled()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()

    print("-" * 50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-" * 50)

    for word in unique_words:
        print(word)
    print("-" * 50)


if __name__ == '__main__':
    main()
