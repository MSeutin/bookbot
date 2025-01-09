def main():
  with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    def count_words(file_contents):
      words = file_contents.split()
      return len(words)
    def count_chars(file_contents):
      book_lower = file_contents.lower()
      count_chars = {}
      for c in book_lower:
        if c.isalpha():
          if c in count_chars:
            count_chars[c] += 1
          else:
            count_chars[c] = 1
      return count_chars
    def format_book(file_contents):
      print(f"--- Begin report of books/frankenstein.txt ---")
      word_count = count_words(file_contents)
      print(f"{word_count} words found in the document")
      dict_chars = count_chars(file_contents)
      for key, value in dict_chars.items():
        print(f"The {key} character was found {value} times")
      print(f"--- End report of books/frankenstein.txt ---")
    format_book(file_contents)
  

main()