import logging
from deploy import Deployer
from constants import CFG


if __name__ == "__main__":
    logging.info('Starting Inception automatic deployment')
    Deployer(CFG).deploy()
    logging.info('Inception deployment finished without any errors.')

