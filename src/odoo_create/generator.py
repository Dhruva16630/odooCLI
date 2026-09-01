from pathlib import Path
from template_engine import render_template

FOLDERS = [
    "models",
    "views",
    "security",
    "controllers",
    "demo"
]

INIT_FOLDERS = [
    "models",
    "controllers"
]

def create_module_directory(module_path:Path) -> Path | None:
    if module_path.exists():
        return None
    
    module_path.mkdir()
    return module_path

def create_root_files(module_path:Path,module_name:str):
    render_template("__manifest__.py.j2",module_path / "__manifest__.py",module_name = module_name,)
    render_template("__init__.py.j2", module_path / "__init__.py")

def create_folders(module_path:Path):
    for folder in FOLDERS:
        (module_path / folder).mkdir()

def create_init_files(module_path:Path):
    for folder in INIT_FOLDERS:
        init_file = module_path / folder / "__init__.py"
        init_file.touch() 


def create_module(module_name:str):
    module_path = Path(module_name)
    module_path = create_module_directory(module_path)
    if module_path is None:
            print(f"Module '{module_name}' already exists.")
            return
    create_root_files(module_path,module_name)
    create_folders(module_path)
    create_init_files(module_path)
    print(f"Module '{module_name}' created successfully")