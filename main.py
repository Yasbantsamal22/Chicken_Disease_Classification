from Chicken_Disease_Classification import logger
from Chicken_Disease_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"====== Stage {STAGE_NAME} Started =============")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"====== Stage {STAGE_NAME} Completed =============")
except Exception as e:
    logger.exception(f"====== Stage {STAGE_NAME} Failed due to {e} ======")
    raise e