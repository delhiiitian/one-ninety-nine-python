import unittest

from contacts import (add_contact, add_phone, all_tags, birthdays_in, by_tag, delete_contact,
                      get_contact, grouped_by_letter, search, tag_counts)
from sample_data import sample_book


class TestContacts(unittest.TestCase):
    def setUp(self):
        self.book = sample_book()

    def test_lookup_ignores_case_and_spaces(self):
        self.assertEqual(get_contact(self.book, "  ASHA   rao ")["email"], "asha@example.com")

    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):
            add_contact(self.book, "asha rao", "1")

    def test_extra_phone_no_duplicates(self):
        add_phone(self.book, "Ben Thomas", "98200 22222")
        add_phone(self.book, "Ben Thomas", "011 1234")
        self.assertEqual(get_contact(self.book, "ben thomas")["phones"], ["98200 22222", "011 1234"])

    def test_search_by_name_email_phone(self):
        self.assertEqual([c["name"] for c in search(self.book, "a r")], ["Asha Rao"])
        self.assertEqual([c["name"] for c in search(self.book, "AR")], ["Arjun Mehta"])
        self.assertEqual(search(self.book, "work.com")[0]["name"], "Ben Thomas")
        self.assertEqual(search(self.book, "98300-33333")[0]["name"], "Chen Li")

    def test_tags(self):
        self.assertEqual(all_tags(self.book), ["family", "gym", "pune", "work"])
        self.assertEqual([c["name"] for c in by_tag(self.book, "gym")], ["Arjun Mehta", "Chen Li"])
        self.assertEqual(tag_counts(self.book)["family"], 2)

    def test_birthdays_sorted_by_day(self):
        self.assertEqual(birthdays_in(self.book, 10), ["Ben Thomas", "Chen Li"])

    def test_grouping(self):
        self.assertEqual(grouped_by_letter(self.book)["A"], ["Arjun Mehta", "Asha Rao"])

    def test_delete(self):
        delete_contact(self.book, "Divya Nair")
        with self.assertRaises(KeyError):
            get_contact(self.book, "Divya Nair")


if __name__ == "__main__":
    unittest.main()
