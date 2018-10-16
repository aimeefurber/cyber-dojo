class Diamond:
    def make(self,letter):
        return '\n'.join(self.get_letters(letter))+'\n'
    def get_letters(self, letter):
        alphabet = self.get_alphabet()
        i = alphabet.index(letter)
        return alphabet[0:i + 1]
    def get_alphabet(self):
        alphabet_string = '''abcdefghijklmnopqrstuvwxyz'''
        return list(alphabet_string)
    def get_indent_for_letter(self, ending_letter, letter):
        letters = self.get_letters(ending_letter)
        l  = letters[::-1]
        return l.index(letter) 
    def get_spacing_for_letter(self, letter):
        letters = self.get_letters('z')
        return letters.index(letter) 
      
