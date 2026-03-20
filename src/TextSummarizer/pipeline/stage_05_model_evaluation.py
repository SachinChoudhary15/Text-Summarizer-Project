


from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.model_evaluation import ModelEvaluation
from TextSummarizer.logging import logger


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()

            model_evaluation = ModelEvaluation(config=model_evaluation_config)

            logger.info("Starting Model Evaluation...")

            model_evaluation.evaluate()

            logger.info("Model Evaluation Completed Successfully")

        except Exception as e:
            logger.error(f"Error in Model Evaluation: {e}")
            raise e