import sys
from stats import get_num_words
from stats import get_num_chars
from stats import report

def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
  return file_contents



def main():
  # print(get_book_text("./books/frankenstein.txt"))
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  content = get_book_text(sys.argv[1])
  # print(count_words(content))
  num_words = get_num_words(content)
  plm = get_num_chars(content)
  # print(f"plm={plm}")
  # print(f"Found {num_words} total words")
  # print(plm)
  report(plm, num_words)


main()
