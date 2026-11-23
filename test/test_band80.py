import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

import band80


class TestGen(unittest.TestCase):
    def test_every_grouping(self):
        for groups in (1, 2, 4, 5, 8, 10, 16, 20, 40, 80):
            size = 80 // groups
            parts = band80.gen(groups, size).split(".")
            self.assertEqual(len(parts), groups)
            self.assertTrue(all(len(p) == size and p.isdigit() for p in parts))

    def test_rejects_bad_grouping(self):
        for groups, size in ((4, 21), (80, 80), (0, 0)):
            with self.assertRaises(ValueError):
                band80.gen(groups, size)

    def test_keeps_leading_zeros(self):
        firsts = [band80.gen(1, 80)[0] for _ in range(2000)]
        self.assertIn("0", firsts)

    def test_digits_look_uniform(self):
        digits = "".join(band80.gen(1, 80) for _ in range(500))
        for d in "0123456789":
            self.assertAlmostEqual(digits.count(d) / len(digits), 0.1, delta=0.01)


class TestCli(unittest.TestCase):
    def run_cli(self, args):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = band80.main(args)
        return code, out.getvalue(), err.getvalue()

    def test_valid(self):
        code, out, _ = self.run_cli(["4:20"])
        self.assertEqual(code, 0)
        self.assertEqual(len(out.strip().split(".")), 4)

    def test_invalid_shows_usage(self):
        for args in ([], ["4:21"], ["420"], ["4", "20"], ["a:b"]):
            code, out, err = self.run_cli(args)
            self.assertEqual(code, 2)
            self.assertEqual(out, "")
            self.assertIn("usage: band80", err)


if __name__ == "__main__":
    unittest.main()
