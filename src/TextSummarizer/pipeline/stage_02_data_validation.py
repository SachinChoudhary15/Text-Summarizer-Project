from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_validation import DataValidation
from TextSummarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()

            data_validation = DataValidation(config=data_validation_config)

            logger.info("Validating dataset...")

            status = data_validation.validate_all_files_exist()

            if not status:
                raise Exception("Data Validation Failed!")

            logger.info("Data Validation Completed Successfully")

        except Exception as e:
            logger.error(f"Error in Data Validation: {e}")
            raise e