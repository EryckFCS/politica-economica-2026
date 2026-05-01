from __future__ import annotations
from ecs_quantitative.core.federation import FederatedNodeConfig

class NodeSettings(FederatedNodeConfig):
    """Configuración canonizada para el nodo economic_policy."""
    project_name: str = "Economic Policy"
    rag_collection: str = "economic_policy"

settings = NodeSettings()
