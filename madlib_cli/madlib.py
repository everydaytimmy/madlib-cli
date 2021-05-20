
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

if __name__ == "__main__":

  print("""

  ****************************************************

  Welcome. We are going to play Madlibs! 
  You will be prompted with a series of prompts. 
  Provde appropriate responses to complete the Madlib

  ****************************************************

  """)

  user_responses = []

  madlib = read_template("assets/dark_and_stormy_night.txt")
  parsed_text, words = parse_template(madlib)

  def get_responses(speech_parts):
    for part in speech_parts:
        prompt = f"Provide a/an {part}  "
        response = input(prompt)
        user_responses.append(response)
  
  get_responses(words)
  print(merge(parsed_text, user_responses))

  #TO DO - Create more templates and RNG to select one for read_template
