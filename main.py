from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from TextSummarizer.logging import logger


def run_stage(stage_name, stage_obj):
    try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        stage_obj.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


if __name__ == "__main__":
    run_stage("Data Ingestion", DataIngestionTrainingPipeline())
    run_stage("Data Validation", DataValidationTrainingPipeline())
    run_stage("Data Transformation", DataTransformationTrainingPipeline())
    run_stage("Model Trainer", ModelTrainerTrainingPipeline())
    run_stage("Model Evaluation", ModelEvaluationTrainingPipeline())