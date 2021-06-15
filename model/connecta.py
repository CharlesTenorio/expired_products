from neo4j import GraphDatabase
from .single import MetaSigleton


class ConnectaNeo4j(metaclass=MetaSigleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "password"))

        return self.connection

