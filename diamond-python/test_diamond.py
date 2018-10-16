import diamond
import unittest

class TestDiamond(unittest.TestCase):
    def setUp(self):
        self.dia = diamond.Diamond()
        
    def test_it_can_print_a_letter(self):
        ''' can print a single letter '''

        letter = 'a'

        self.assertEqual(self.dia.make(letter), letter + '\n')

    def test_do_something_with_b(self):
        '''when it gets b as an argument it knows that should also have a'''

        letter = 'b'

        self.assertEqual(self.dia.get_letters(letter), ['a','b'])

    def test_get_all_letters_of_alphabet_as_array(self):
        ''' can get all the letters of the alphabet as an array '''

        alphabet = self.dia.get_alphabet()

        filtered = filter(lambda a: type(a) is str, alphabet)
        self.assertEquals(len(filtered), 26)

    def test_that_it_can_get_an_alphabet_slice(self):
        ''' when we give it a character it will return the list of characters up to that one in the alphabet'''
        self.assertEquals(self.dia.get_letters('c'), ['a','b','c'])

    def test_that_it_can_make_a_new_line_for_each_letter_in_the_diamond(self):
        expected = 'a \n' + 'b \n' + 'c \n'    
       
        diamond = self.dia.make('c')
 
        self.assertEquals(diamond.count('\n'), 3)

    def test_that_knows_the_indent_for_an_element_in_the_list(self):
        ''' when the list is a given length the first element will have the correct number of indents'''
        self.assertEquals(self.dia.get_indent_for_letter('d','c'),1)
    def test_that_knows_the_spacing_between_letters_an_element_in_the_list(self):
        '''the letters for a given element will have the correct number of spaces between them'''
        self.assertEquals(self.dia.get_spacing_for_letter('c'), 2)
        self.assertEquals(self.dia.get_spacing_for_letter('f'), 5)
    def test_that_a_only_prints_one_letter(self):
        ''' a should only appear once'''
        self.assertEquals( self.dia.make('d')[0].count('a'), 1) 
    def test_that_other_letters_print_twice(self):
        '''everything else should print twice'''
        print self.dia.make('d')
        self.assertEquals( self.dia.make('d')[1].count('b'), 2) 


if __name__ == '__main__':
    unittest.main() # pragma: no cover

