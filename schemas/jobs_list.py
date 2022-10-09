from voluptuous import Schema
from voluptuous import Any

jobs_list = Schema({
    "jobs": [
        {
            "absolute_url": str,
            "data_compliance": [
                {
                    "type": str,
                    "requires_consent": bool,
                    "retention_period": None
                }
            ],
            "education": str,
            "internal_job_id": int,
            "location": {
                "name": str
            },
            "metadata": [
                {
                    "id": int,
                    "name": str,
                    "value": Any(None, str, list),
                    "value_type": str
                }

            ],
            "id": int,
            "updated_at": str,
            "requisition_id": str,
            "title": str,
            "content": str,
            "departments": [
                {
                    "id": int,
                    "name": str,
                    "child_ids": list,
                    "parent_id": None
                }
            ],
            "offices": [
                {
                    "id": int,
                    "name": str,
                    "location": str,
                    "child_ids": list,
                    "parent_id": None
                }
            ]
        }
    ],
    "meta": {
        "total": int
    }
}
)
