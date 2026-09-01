from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT / os.getenv(
    "PROJECT_DATA_DIR",
    "data"
)

RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

NOTEBOOK_DIR = ROOT / "notebooks"
REPORT_DIR = ROOT / "reports"
MODEL_DIR = ROOT / "model"