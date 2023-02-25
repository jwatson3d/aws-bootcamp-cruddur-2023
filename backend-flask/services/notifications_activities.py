from datetime import datetime, timedelta, timezone
class NotificationsActivities:
  def run():
    now = datetime.now(timezone.utc).astimezone()
    results = [{
      'uuid': 'a2bd7ac5-cdcc-4019-873c-6024fcebbc05',
      'handle':  'sherlock',
      'message': 'Elementary, my dear Watson',
      'created_at': (now - timedelta(days=2)).isoformat(),
      'expires_at': (now + timedelta(days=5)).isoformat(),
      'likes_count': 5,
      'replies_count': 1,
      'reposts_count': 0,
      'replies': [{
        'uuid': 'eb014c61-823b-4d99-a452-1c2f84d8c1cb',
        'reply_to_activity_uuid': 'a2bd7ac5-cdcc-4019-873c-6024fcebbc05',
        'handle':  'watson',
        'message': 'Watson, you idiot! Someone has stolen our tent!',
        'likes_count': 0,
        'replies_count': 0,
        'reposts_count': 0,
        'created_at': (now - timedelta(days=2)).isoformat()
      }],
    }
    ]
    return results