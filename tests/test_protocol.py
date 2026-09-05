import unittest

from trivian_protocol import TrivianLattice, TrivianRitual


class TrivianSutraTests(unittest.TestCase):
    def test_json_loads_and_indexes_sutras(self):
        lattice = TrivianLattice("trivian_sutra.json")
        self.assertIsInstance(lattice.sutras, list)
        self.assertGreater(len(lattice.sutras), 0)

    def test_invoke_pada_returns_text(self):
        lattice = TrivianLattice("trivian_sutra.json")
        result = lattice.invoke_pada(1)
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, "Pada not found in the current Lattice.")

    def test_missing_file_is_graceful(self):
        lattice = TrivianLattice("does-not-exist.json")
        self.assertEqual(lattice.sutras, [])
        self.assertIn("error", lattice.data)

    def test_ritual_close_without_start_is_safe(self):
        lattice = TrivianLattice("trivian_sutra.json")
        ritual = TrivianRitual(lattice)
        self.assertIsNone(ritual.session_start)
        ritual.end_dialogue()
        self.assertIsNone(ritual.session_start)


if __name__ == "__main__":
    unittest.main()
