import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name='project2'

list_of_files=[

    'src/{project_name}/__init__.py',
    'src/{project_name}/component/data_ingestion.py',
    'src/{project_name}/component/data_transformation.py',
    'src/{project_name}/component/model_trainer.py',
    'src/{project_name}/component/model_monitoring.py',
    'src/{project_name}/pipelines/__init__.py',
    'src/{project_name}/pipelines/training_pipeline.py',
    'src/{project_name}/pipelines/prediction_pipeline.py',
    'src/{project_name}/exception.py',
    'src/{project_name}/logger.py',
    'src/{project_name}/utils.py',
    'app.py',
    'Dockerfile',
]

for filepath in list_of_files:
    fileapth = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f" {filename} already exist")

