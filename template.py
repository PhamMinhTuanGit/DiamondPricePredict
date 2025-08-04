from pathlib import Path

root = 'diamond_price_predict'

list_of_files = [
    f"{root}/pipeline/training_pipeline.py",
    f"{root}/pipeline/prediction_pipeline.py",
    f"{root}/components/data_ingestion.py",
    f"{root}/components/data_validation.py",
    f"{root}/components/data_transformation.py",
    f"{root}/components/model_trainer.py",
    f"{root}/components/model_evaluation.py",
    f"{root}/components/model_pusher.py",
    f"{root}/entity/config_entity.py",
    f"{root}/entity/artifact_entity.py",
    f"{root}/configuration/__init__.py",
    f"{root}/constant/__init__.py",
    f"{root}/logger/__init__.py",
    f"{root}/utils/main_utils.py",
    f"{root}/__init__.py",  # Tệp gốc,
    ".dockerignore",
    "requirements.txt",
    "setup.py",
    "README.md",
    "demo.py",
    "app.py",
    "config/model.yaml",
    "config/schema.yaml", 
]

for file_path in list_of_files:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)

print(f"✅ Đã tạo cấu trúc thư mục và file trong thư mục: '{root}'")
