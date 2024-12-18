from Chicken_Disease_Classification.config.configuration import ConfigurationManager
from Chicken_Disease_Classification.components.prepare_base_model import PrepareBaseModel
from Chicken_Disease_Classification import logger


from Chicken_Disease_Classification.config.configuration import ConfigurationManager
from Chicken_Disease_Classification.components.data_ingestion import DataIngestion
from Chicken_Disease_Classification import logger


STAGE_NAME = "Prepare Base Model Stage"


class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        

if __name__ == '__main__':
    try:
        logger.info(f"====== Stage {STAGE_NAME} Started =============")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f"====== Stage {STAGE_NAME} Completed =============")
    except Exception as e:
        logger.exception(f"====== Stage {STAGE_NAME} Failed due to {e} ======")
        raise e