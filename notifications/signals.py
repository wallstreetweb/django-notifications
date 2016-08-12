from django.dispatch import Signal

notify = Signal(providing_args=[
    'recipient', 'actor', 'verb', 'action_object', 'target', 'description',
    'timestamp', 'level'
])


new_unread_notify = Signal(providing_args=[
    'sender', 'recipient',
])
