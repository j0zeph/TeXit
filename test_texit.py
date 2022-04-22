import unittest
from texit import add_tex_syntax


class TestTexit(unittest.TestCase):
    def setUp(self) -> None:
        self.txt = 'Lorem ipsum dolor sit amet, ...'

    def test_bold_syntax_is_added(self):
        bolded = r'\large\textbf{Lorem ipsum dolor sit amet, ...}\\'
        self.assertEqual(bolded, add_tex_syntax('-bf' + self.txt))

    def test_bullet_point_is_added(self):
        bolded = r'\bullet\large\text{ Lorem ipsum dolor sit amet, ...}\\'
        self.assertEqual(bolded, add_tex_syntax('-bp' + self.txt))

    def test_large_newline_is_added(self):
        self.assertEqual('$$ $$', add_tex_syntax('-bbr'))

    def test_small_newline_is_added(self):
        self.assertEqual('$$$$', add_tex_syntax('-br'))

    def test_underline_is_added(self):
        underlined = r'\underline{\large\text{Lorem ipsum dolor sit amet, ...}}'
        self.assertEqual(underlined, add_tex_syntax('-und' + self.txt))
