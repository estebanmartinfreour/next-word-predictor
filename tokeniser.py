class Tokeniser:
    def __init__(self, text):
        self.text = text
        self.word_to_index = {}
        self.index_to_word = {}

    def build_tables(self):
        "A partir d'un texte, tokenizer.word_to_index() doit renvoyer un dictionnaire qui associe"
        "à chaque mot du texte un nombre qui sera son code dans le texte."
        word_to_index = {}
        index_to_word = {}
        c_list = self.text.split()
        i = 1
        for string in c_list:
            if string not in word_to_index:
                word_to_index[string] = i
                index_to_word[i] = string
                i +=1
        self.word_to_index = word_to_index
        self.index_to_word = index_to_word

    def text_to_sequences(self):
        "Transforme un texte en une liste d'enteirs où chaque entier "
        c_list = self.text.split()
        text_to_sequences = []
        for string in c_list:
            text_to_sequences.append(self.word_to_index[string])
        return text_to_sequences


tokenizer = Tokeniser("bonjour je suis une chaîne de caractère bonjour je suis")
tokenizer.build_tables()
print(tokenizer.word_to_index)
print(tokenizer.index_to_word)
print(tokenizer.text_to_sequences())


    