from voluptuous import Schema

success_authorization = Schema({
    "token": str,
    "user_settings": {
        "locale": str,
        "theme": str
    },
    "user_id": str
})
