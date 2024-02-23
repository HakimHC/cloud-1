from config import Config
from logger import Logger
from pathlib import Path
import sys


try:
    CFG = Config()
    logger = Logger(CFG.config)
except (Config.InvalidBlockError, ValueError) as e:
    print(e, file=sys.stderr)
    exit(1)


PROJECT_ROOT = Path(__file__).parent.parent.absolute()
TERRAFORM_PATH = PROJECT_ROOT / CFG.terraform.get('base_dir') if CFG.terraform else None
