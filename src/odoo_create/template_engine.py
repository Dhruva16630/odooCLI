from pathlib import Path
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = Path(__file__).parent / "templates"
TEMPLATE_DIR2 = Path(__file__).parent
print(TEMPLATE_DIR)
print(TEMPLATE_DIR2)

def render_template(template_name:str,destination:Path,**context):
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template(template_name)
    output = template.render(**context)
    destination.write_text(output)