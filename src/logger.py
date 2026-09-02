import logging
from pathlib import Path


# Get project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Create logs directory if it does not exist
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "process.log"


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger("ETL_Pipeline")