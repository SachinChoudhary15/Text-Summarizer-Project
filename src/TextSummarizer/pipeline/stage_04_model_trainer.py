


from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.model_trainer import ModelTrainer
from TextSummarizer.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()

            model_trainer = ModelTrainer(config=model_trainer_config)

            logger.info("Starting Model Training...")

            model_trainer.train()

            logger.info("Model Training Completed Successfully")

        except Exception as e:
            logger.error(f"Error in Model Training: {e}")
            raise e