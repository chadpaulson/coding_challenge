import unittest
from unittest import mock

from app.api import ProfileData

from tests.fixtures import bitbucket, github


class APITestCase(unittest.TestCase):

    @mock.patch('app.api.ProfileData.load_bitbucket', return_value=bitbucket)
    @mock.patch('app.api.ProfileData.load_github', return_value=github)
    def test_fetch_profile_data(self, load_bitbucket, load_github):
        """ Ensures merged data is calculated and formatted correctly. """
        profile = ProfileData(username='mailchimp')
        data = profile.fetch_profile_data()

        self.assertEqual(data['num_forked_repos'], 1)
        self.assertEqual(data['num_original_repos'], 11)
        self.assertEqual(data['num_total_repos'], 12)
        self.assertEqual(data['watchers'], 86)
        self.assertEqual(data['languages']['php'], 2)
        self.assertEqual(data['languages']['python'], 3)
        self.assertEqual(data['languages']['javascript'], 3)
        self.assertEqual(data['languages']['ruby'], 2)
        self.assertEqual(data['languages']['dart'], 1)
        self.assertEqual(data['languages']['java'], 1)
