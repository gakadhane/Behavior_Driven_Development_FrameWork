import logging
import os

def get_project_root():
    return os.path.dirname(os.path.abspath(__file__))

# def setup_logging():
#     log_file = os.path.join(get_project_root(), 'logs', 'test_log.log')
#     logging.basicConfig(level=logging.INFO, filename=log_file,
#                         format='%(asctime)s - %(levelname)s - %(message)s')
#     return logging.getLogger()
#
# logger = setup_logging()