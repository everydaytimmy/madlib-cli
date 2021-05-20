from madlib_cli.madlib import read_template, parse_template, merge

print("""

****************************************************

Welcome. We are going to play Madlibs! 
You will be prompted with a series of prompts. 
Provde appropriate responses to complete the Madlib

****************************************************

""")

user_responses = []

def get_responses():
  adj1 = input("Provide an Adjective ")
  user_responses.append(adj1)
  adj2 = input("Provide another Adjective ")
  user_responses.append(adj2)
  noun1 = input("Provide a Noun ")
  user_responses.append(noun1)


madlib = read_template("assets/dark_and_stormy_night.txt")
deconstructed = parse_template(madlib)

parts = get_responses()
print(merge(deconstructed.final_text, parts))
