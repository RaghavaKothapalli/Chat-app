to run project
$env:DJANGO_SETTINGS_MODULE="core.settings"; daphne -b 127.0.0.1 -p 8000 core.asgi:application
