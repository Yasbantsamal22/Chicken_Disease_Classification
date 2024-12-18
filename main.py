from Chicken_Disease_Classification import logger
from Chicken_Disease_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Chicken_Disease_Classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from Chicken_Disease_Classification.pipeline.stage_03_training import ModelTrainingPipeline
from Chicken_Disease_Classification.pipeline.stage_04_evaluation import EvaluationPipeline





STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"====== Stage {STAGE_NAME} Started =============")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"====== Stage {STAGE_NAME} Completed =============")
except Exception as e:
    logger.exception(f"====== Stage {STAGE_NAME} Failed due to {e} ======")
    raise e




STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f"====== Stage {STAGE_NAME} Started =============")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f"====== Stage {STAGE_NAME} Completed =============")
except Exception as e:
    logger.exception(f"====== Stage {STAGE_NAME} Failed due to {e} ======")
    raise e


STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e