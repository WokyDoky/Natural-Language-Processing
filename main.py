
# Unzip file
import zipfile
import math


with zipfile.ZipFile('glove.6B.50d.zip', 'r') as zip_ref:
    zip_ref.extractall()

# Read the resulting txt file and print the first 15 lines
embeddings_file = open("glove.6B.50d.txt", "r", encoding="ISO-8859-1")
words_lst = []
embeddings_lst = []

for line in embeddings_file:
  tokens = line.replace("\n","").split(" ")
  word_text = tokens[0]
  word_embedding = []

  for i in range(1, len(tokens)):
    word_embedding.append(float(tokens[i]))

  words_lst.append(word_text)
  embeddings_lst.append(word_embedding)

  Tree = AVL_Tree()
  raiz = None
  print(raiz)
  for i in range(len(words_lst)):
    if any(c.isalpha() for c in words_lst[i]): raiz = Tree.insert(raiz, words_lst[i], embeddings_lst[i])


  def search(root, key):
    key = key.lower()
    if root is None: return [0]
    if root.val == key: return root.embedding
    if key < root.val:
      return search(root.left, key)
    else:
      return search(root.right, key)


  def dot(e1, e2):
    if len(e1) != len(e2):
      return 0

    return sum(i[0] * i[1] for i in zip(e1, e2))


  def magnitud(e1, e2):
    if len(e1) != len(e2):
      return -1
    E1 = 0
    E2 = 0
    m1 = 0
    m2 = 0
    for i in range(len(e1)):
      E1 += pow(e1[i], 2)
      E2 += pow(e2[i], 2)
    m1 = math.sqrt(E1)
    m2 = math.sqrt(E2)
    return m1 * m2


  def simi(word1, word2):
    s1 = dot(search(raiz, word1), search(raiz, word2))
    s2 = magnitud(search(raiz, word1), search(raiz, word2))
    return s1 / s2


  # USER INPUT IN COMMENTS

  word1 = input("Input first word:  ")
  word2 = input("Input first word:  ")
  print(simi(word1, word2))

  print("barley shrimp:     ", simi("barley", "shrimp"))
  print("barley oat:        ", simi("barley", "oat"))
  print("federer baseball:  ", simi("federer", "baseball"))
  print("federer tennis:    ", simi("federer", "tennis"))
  print("harvard stanford:  ", simi("harvard", "stanford"))
  print("harvard utep:      ", simi("harvard", "utep"))
  print("harvard ant:      ", simi("harvard", "ant"))
  print("raven crow:        ", simi("raven", "crow"))
  print("raven whale:       ", simi("raven", "whale"))
  print("spain france:      ", simi("spain", "france"))
  print("spain mexico:      ", simi("spain", "mexico"))
  print("mexico france:     ", simi("mexico", "france"))

  print()
  print("Things I found interesting")
  print("women female:    ",
        simi("women", "female"))  # Why does women and female have a worst ratio than mexico and spain? Interesting
  print("human animal:    ", simi("human", "animal"))
  print("same same:       ", simi("same", "same"))  # Why 0.2? Roundingn Errors?
  print("dry wet:         ", simi("dry", "wet"))  # highest similarity I found without being the same word
  print("jenalia.moreno@chron.com of", simi("jenalia.moreno@chron.com", "of"))  # lowest similarity I could find

