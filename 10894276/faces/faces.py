def main(word):
  word = word.replace(":)","🙂")
  word = word.replace(":(","🙁")
  print(word )

wording = input("?")
main(wording)
