import pytest

from apps.posts.models import Staff


@pytest.mark.django_db
class TestStaffModel:

    def test_staff(self):
        count = Staff.objects.count()

        data = {
            'full_name': 'PDP',
            'image': 'test_logo.png',
            'job': 'Test',
        }
        staff = Staff.objects.create(**data)

        assert staff.full_name == data['full_name']
        assert count + 1 == Staff.objects.count()
