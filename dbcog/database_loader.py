import os
import shutil

from redbot.core import data_manager

from .database_context import DbContext
from .database_manager import DBCogDatabase
from .dungeon_context import DungeonContext
from .monster_graph import MonsterGraph


def _data_file(file_name: str) -> str:
    return os.path.join(str(data_manager.cog_data_path(raw_name='dbcog')), file_name)


def load_database(existing_db, debug_monster_ids):
    DB_DUMP_FILE = _data_file('dadguide.sqlite')
    DB_DUMP_WORKING_FILE = _data_file('dadguide_working.sqlite')
    # Release the handle to the database file if it has one
    if existing_db:
        existing_db.close()
    # Overwrite the working copy so we can open a handle to it without affecting future downloads
    if os.path.exists(DB_DUMP_FILE):
        shutil.copy2(DB_DUMP_FILE, DB_DUMP_WORKING_FILE)
    # Open the new working copy.
    database = DBCogDatabase(data_file=DB_DUMP_WORKING_FILE)
    graph = MonsterGraph(database, debug_monster_ids)
    dungeon = DungeonContext(database)
    db_context = DbContext(database, graph, dungeon, debug_monster_ids)
    return db_context
