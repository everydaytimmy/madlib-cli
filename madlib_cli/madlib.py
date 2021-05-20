
def read_template(path):
  with open(path) as text:
    return text.read().strip()
   
def parse_template(template):
  final_text = ""
  collection = []
  temp_word = ""
  capturing_word = False
  for char in template:
    if char == '{':
      final_text += char
      capturing_word = True
      temp_word = ""
    elif char == '}':
      final_text += char
      capturing_word = False
      collection.append(temp_word)
    elif capturing_word:
      temp_word += char
    else:
      final_text += char
  
  return final_text, tuple(collection)

def merge(template, parts):
  merged = template.format(*parts)
  return merged