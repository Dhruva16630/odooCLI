from pathlib import Path

folders = [
    "models",
    "views",
    "security",
    "controllers",
    "demo"
]

init_folders = [
    "models",
    "controllers"
]


def create_module_directory(module_path:Path) -> Path | None:
    if module_path.exists():
        return None
    
    module_path.mkdir()
    return module_path

def create_root_files(module_path:Path,module_name:str):
    init_file = module_path / "__init__.py"
    manifest_file = module_path / "__manifest__.py"
    
    init_file.touch()
    manifest_file.write_text(
        f"""{{
    "name":"{module_name}"
}}
"""
)

def create_folders(module_path:Path):
    for folder in folders:
        (module_path / folder).mkdir()

def create_init_files(module_path:Path):
    for folder in init_folders:
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