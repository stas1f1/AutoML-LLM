from typing import List
from streamlit.runtime.uploaded_file_manager import UploadedFile
from fedot_llm.data.loaders import PathDatasetLoader
from pathlib import Path
import os
import shutil

STREAMLIT_DATASET_DIR = Path("_experiments/datasets/streamlit")
class StreamlitDatasetLoader:
    @staticmethod
    def load(files: List[UploadedFile]):
        if os.path.exists(STREAMLIT_DATASET_DIR):
            shutil.rmtree(STREAMLIT_DATASET_DIR)
        os.makedirs(STREAMLIT_DATASET_DIR)
        for file in files:
            with open(STREAMLIT_DATASET_DIR / file.name, 'wb') as f:
                f.write(file.getvalue())
        dataset = PathDatasetLoader.load(STREAMLIT_DATASET_DIR)
        return dataset