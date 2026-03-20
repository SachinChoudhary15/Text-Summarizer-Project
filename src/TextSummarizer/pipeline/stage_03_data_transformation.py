

from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_transformation import DataTransformation
from TextSummarizer.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()

            data_transformation = DataTransformation(config=data_transformation_config)

            logger.info("Starting Data Transformation...")

            data_transformation.convert()

            logger.info("Data Transformation Completed Successfully")

        except Exception as e:
            logger.error(f"Error in Data Transformation: {e}")
            raise e