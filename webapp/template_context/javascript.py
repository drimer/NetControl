import os

from webconf import settings

__author__ = 'alberto'


def templates(request):
    del request

    templates_dir = os.path.join(settings.BASE_DIR, 'client', 'js_templates')

    js_templates = []
    for file_name in os.listdir(templates_dir):
        file_path = os.path.join(templates_dir, file_name)
        with open(file_path, 'r') as f:
            template_content = f.read()

        js_templates.append((file_name, template_content))

    return {
        'js_templates': js_templates,
    }
