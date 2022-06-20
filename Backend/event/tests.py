from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from event.models import Event


class TestEvent(APITestCase):
    url = reverse_lazy('event-list')

    def format_datetime(self, value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test_list(self):
        event = Event.objects.create(activity='Enquête', day_week=5, planning=1, description='Recueillir des infos afin de povoir classer la populasse')
        Event.objects.create(activity='Recensement', day_week=3, description='aller sur le terrain recenser le sgens')

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        expected = [
            {
                'id': event.pk,
                'activity': event.activity,
                'description': event.description,
                'day_week': event.day_week,
                'create': self.format_datetime(event.create),
                'updated': self.format_datetime(event.updated)
            }
        ]
        self.assertEqual(expected, response.json())

    def test_create(self):
        self.assertFalse(Event.objects.exists())
        response = self.client.post(self.url, data={'activity': 'New activity'})

        self.assertEqual(response.status_code, 405)

        self.assertFalse(Event.objects.exists())
