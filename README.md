# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.
## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Class Materials Rules
- Each stage's handouts go in their own subfolder, named exactly as the course
 folder, e.g. `class_materials/stage01_problem-framing-and-scoping/`.
- Run lecture notebooks in place from that folder.
- Copy a homework starter into `homework/homeworkN/` before working on it.
## Project Folder Rules
- Keep project files organized and clearly named.
- The project folder structure is set up in Stage 02.

## Data Storage

Stage 05 implements a reproducible storage layer using environment-driven paths.

### Folder Structure

- `data/raw/` stores raw data in CSV format.
- `data/processed/` stores processed data in Parquet format.

### Formats

CSV is used for raw data because it is portable and human-readable.

Parquet is used for processed data because it preserves data types and provides efficient columnar storage.

### Environment Variables

Storage paths are configured in `.env`:

```text
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed