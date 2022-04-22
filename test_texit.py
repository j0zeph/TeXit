import unittest
from texit import add_tex_syntax


class TestTexit(unittest.TestCase):
    def test_bold_syntax_is_added(self):
        txt = '-bf Lorem ipsum dolor sit amet, ...'
        bolded = r'\large\textbf{Lorem ipsum dolor sit amet, ...}'
        self.assertEqual(bolded, add_tex_syntax(txt))

    def test_bullet_point_is_added(self):
        pass

    def test_large_newline_is_added(self):
        pass

    def test_small_newline_is_added(self):
        pass

    def test_underline_is_added(self):
        pass