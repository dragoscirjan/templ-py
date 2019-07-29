from dependency_injector import containers, providers

from .base import Base
from .jsonlint import JSONLint
from .precommit import PreCommit
from .setup import Setup

class Resolvers(containers.DeclarativeContainer):
    """Resolvers Container."""

    config = providers.Configuration('config')

    jsonlint = providers.Singleton(JSONLint, args=config.args)
    pre_commit = providers.Singleton(PreCommit, args=config.args)
    setup = providers.Singleton(Setup, args=config.args)
