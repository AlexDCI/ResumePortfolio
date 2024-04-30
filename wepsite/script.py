from django.contrib.auth.models import User
from wepsite.models import Profile

def create_profiles():
    from django.contrib.auth.models import User
    from wepsite.models import Profile

    # Создаем 20 пользователей и их профили
    for i in range(1, 21):
        # Создаем пользователя
        user = User.objects.create(username=f'user{i}', email=f'user{i}@example.com')
        # Создаем профиль пользователя
        profile = Profile.objects.create(
            user=user,
            bio=f'Bio for user {i}',
            skills='Python, JavaScript, SQL, Java, C++',
            experience=f'Experience for user {i}',
            education=f'Education for user {i}',
            contact_info=f'Contact info for user {i}'
        )

# Вызываем функцию для создания профилей пользователей
create_profiles()
