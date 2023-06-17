import pytest

from apps.posts.models import Staff, New, Region, Category


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


@pytest.mark.django_db
class TestNewModel:

    def test_new(self):
        count = New.objects.count()

        data = {
            'title': 'Kun.uz',
            'short_description': 'test_description',
            'long_description': 'test_description',
            'image': 'test_logo.png',
            'created_at': '2023-06-13',
            'views': '23',
            'category': 'New',
        }
        new = New.objects.create(**data)

        assert new.title == data['title']
        assert count + 1 == New.objects.count()


@pytest.mark.django_db
class TestRegionModel:

    def test_region(self):
        count = Region.objects.count()

        data = {
            'name': 'Samarqand',
            'blog': 'Kun.uz',
        }
        region = Region.objects.create(**data)

        assert region.name == data['name']
        assert count + 1 == Region.objects.count()


@pytest.mark.django_db
class TestCategoryModel:

    def test_category(self):
        count = Category.objects.count()

        data = {
            'name': 'Clothes',
        }
        category = Category.objects.create(**data)

        assert category.name == data['name']
        assert count + 1 == Category.objects.count()
