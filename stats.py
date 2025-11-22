import string

def get_num_words(text):
  words = text.split()
  count = 0
  for word in words:
    count +=1
  return count

def get_num_chars(text):
  character_set = set(string.ascii_lowercase)
  lower_text = text.lower()
  dict = {}

  for uniq in character_set:
    for char in lower_text:
      if uniq == char:
        if char in dict:
          dict[uniq] += 1
        else:
          dict[uniq] = 1

  return dict

def sort_on(items):
    return items["num"]


def report(dict, count):
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {count} total words")
  print("--------- Character Count -------")
  list = []
  for k, v in dict.items():
    list.append({"char": k, "num": v})

  list.sort(key=sort_on, reverse=True)
  for item in list:
    print(f"{item['char']}: {item['num']}")


