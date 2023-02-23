from datetime import datetime
from typing import Dict

from django.template.defaultfilters import slugify as django_slugify
from pythonjsonlogger import jsonlogger

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify_unicode(s):
    """
    Overriding django slugify_unicode that allows to use russian words as well.
    """
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class JsonFormatter(jsonlogger.JsonFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.json_ensure_ascii = False

    def add_fields(self, log_record, record, message_dict):
        super(JsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname


def get_env_variables(filename: str) -> Dict[str, str]:
    variables = {}
    with open(filename) as file:
        for line in file:
            if line.startswith('#') or not line.strip():
                continue

            key, value = line.strip().split('=', 1)
            variables[key] = value

    return variables
