#word counting code
def count_words(text):
  if not text:
    raise ValueError("Input text cannot be empty.")
  words = text.split() # splits input string into individual 
  return len(words)

# Driver code
print("Enter a sentence or a paragraph:\n ")
print("Note: If you are pasting text please paste it as 'paste as one line' and click enter.\n")
while True:
  text = input()
  if text:  # check if text is not empty
    try:
      word_count = count_words(text)
      print("Total number of words in the given sentence or paragraph is:-", word_count)
      input("Enter any key to exit program")
      break  # break the loop if input is valid
    except ValueError as e:
      print("Error:", e)  # handle errors
  else:
    print("Please enter some text. An empty string is not allowed.")

