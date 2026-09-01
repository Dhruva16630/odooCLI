from jinja2 import Environment, FileSystemLoader
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent / "templates"

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template("hello.txt.j2")
output = template.render(name="Dhruva",city = "Mysuru")
print(output)