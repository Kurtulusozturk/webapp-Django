class Role():

    READER = 1
    WRITER = 2
    ADMIN = 5
    ROLE_CHOICES = (
        (READER, 'Reader'),
        (WRITER, 'Writer'),
        (ADMIN, 'Admin'),
    )
