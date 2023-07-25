from django.conf import settings

from main.utils import get_env_variables


def test_dot_env_example_relevance():
    """Регрессионный тест, который проверяет актуальность .env.example файла"""

    project_root = settings.BASE_DIR.parent.absolute()

    dot_env_filename = str(project_root / '.env')
    dot_env_example_filename = str(project_root / '.env.example')

    dot_env_variables_names = get_env_variables(dot_env_filename).keys()
    dot_env_example_variables_names = get_env_variables(dot_env_example_filename).keys()

    assert dot_env_variables_names == dot_env_example_variables_names
