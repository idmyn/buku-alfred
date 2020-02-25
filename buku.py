import sys
import os.path
import sqlite3
from workflow import Workflow, ICON_WEB

db_path = os.path.expanduser('~/.local/share/buku/bookmarks.db')
conn = sqlite3.connect(db_path)
c = conn.cursor()


def main(wf):
    for row in c.execute("select * from bookmarks"):
        wf.add_item(title=row[2],
                    subtitle=row[1],
                    arg=row[1],
                    valid=True,
                    icon=ICON_WEB)

    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
