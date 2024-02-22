from config import Config
from logger import Logger
from pathlib import Path


CFG = Config()
logger = Logger(CFG.config)

PROJECT_ROOT = Path(__file__).parent.parent.absolute()
TERRAFORM_PATH = PROJECT_ROOT / CFG.terraform.get('base_dir') if CFG.terraform else None
