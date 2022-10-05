from voluptuous import Schema

location_metadata = Schema({
        "consent_required": bool,
        "country_code": str,
        "promotional_email_opt_in": {
            "required": bool,
            "pre_checked": bool
        }
    }
)
