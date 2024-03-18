from django.test import TestCase
from .models import Driver, Ride
from django.contrib.auth.models import User

class DriverModelTestCase(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create(id=5, name='pluto', status=True)

    def test_driver_creation(self):
        """Test Driver model creation"""
        self.assertEqual(self.driver.name, 'pluto')
        self.assertTrue(self.driver.status)

class RideModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.driver = Driver.objects.create(id=1, name='pluto', status=True)
        self.ride = Ride.objects.create(
            id=1,
            rider=self.user,
            driver=self.driver,
            pickup_location='placeA',
            dropoff_location='placeB',
            status='started'
        )

    def test_ride_creation(self):
        """Test Ride model creation"""
        self.assertEqual(self.ride.rider, self.user)
        self.assertEqual(self.ride.driver, self.driver)
        self.assertEqual(self.ride.pickup_location, 'placeA')
        self.assertEqual(self.ride.dropoff_location, 'placeB')
        self.assertEqual(self.ride.status, 'started')
