from dependency_injector import containers, providers

from .base import Base
from .jsonlint import Jsonlint
from .pre_commit import PreCommit
from .pre_commit_config import PreCommitConfig


class Resolvers(containers.DeclarativeContainer):
    """Resolvers Container."""

    config = providers.Configuration('config')

    jsonlint = providers.Singleton(Jsonlint, app=config.app)

    pre_commit_config = providers.Singleton(PreCommitConfig, app=config.app)
    pre_commit = providers.Singleton(PreCommit, app=config.app)
