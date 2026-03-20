import os
from TextSummarizer.entities import DataValidationConfig
from TextSummarizer.logging import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:

            data_path = os.path.join("artifacts", "data_ingestion", "samsum_dataset")
            all_files = os.listdir(data_path)

            required_files = self.config.ALL_REQUIRED_FILES

            missing_files = [f for f in required_files if f not in all_files]

            validation_status = len(missing_files) == 0

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            logger.info(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            logger.error(f"Validation error: {e}")
            raise e