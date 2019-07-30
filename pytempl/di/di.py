from dependency_injector import containers, providers
import logging

# from pytempl.app import PyTempl, PyTemplTest
from pytempl.controllers.resolvers import JSONLint


class DI(containers.DeclarativeContainer):

    logger = providers.Singleton(logging.Logger, name='pytempl')

    # pytempl = providers.Singleton(PyTempl)
    # pytempltest = providers.Singleton(PyTemplTest)

    jsonlint = providers.Factory(JSONLint, logger=logger)
