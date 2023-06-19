import unittest
from unittest import TestCase
from mentor import popular_names, mentors, mentors_in_learnnig_two_courses, duratuons_courses, durations, courses
import pytest


class PopularNamesTestCase(TestCase):
    def test_comparison_of_values(self):
        # mentors_list = mentors
        expected_result = [['Александр', 10], ['Евгений', 5], ['Максим', 4]]
        res = popular_names(mentors)
        self.assertEqual(res, expected_result)
    
    def test_len_output_list(self):
        expected_result = 4
        res = len(popular_names(mentors))
        self.assertLess(res, expected_result)

class MentorsInLearnnigTwoCourses(TestCase):
    def test_isinstance_types_output(self):
        res = mentors_in_learnnig_two_courses(mentors)
        self.assertIsInstance(res, list)

    def test_name_in_res(self):
        res = mentors_in_learnnig_two_courses(mentors)
        test_name = 'Александр'
        self.assertIn(test_name, res)

class DuratuonsCourses(TestCase):
    def test_isinstance_types_output(self):
        res = duratuons_courses(courses, durations)
        self.assertIsInstance(res, list)

    def test_name_in_res(self):
        res = duratuons_courses(courses, durations)
        test_name = 'Java-разработчик с нуля'
        self.assertIn(test_name, res)

    def test_len_output_list(self):
        expected_result = 5
        res = len(duratuons_courses(courses, durations))
        self.assertLess(res, expected_result)

class TestDuratuonsCourses:
    def test_results_list(self):
        expected_result = ['Java-разработчик с нуля', 'Frontend-разработчик с нуля']
        res = duratuons_courses(courses, durations)
        assert res == expected_result


if __name__ == '__main__':
    # unittest.main()
    pytest.main()