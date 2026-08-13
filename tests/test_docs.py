"""Every documented command must actually run.

The README's report command passed four arguments to a `main()` that takes
three. It printed usage, exited 2, and wrote nothing -- so `analysis.md`
silently kept the previous wave's numbers and anyone reading it took a stale
median as current. A wrong command that fails loudly costs a minute; this
one cost a wave.
"""

import contextlib
import io
import os
import re
import unittest

from src import allocate
from src import clocks
from src import report
from src import schema
from src import stats

MODULES = {
    "allocate": allocate,
    "clocks": clocks,
    "report": report,
    "schema": schema,
    "stats": stats,
}

DOCS = ["README.md", "docs/superpowers/RUNBOOK.md"]

COMMAND = re.compile(r"python3 -m src\.(\w+)(.*)")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Somewhere that cannot exist, so a command with the right arity gets as far
# as opening a file and stops there instead of overwriting real output.
MISSING = os.path.join(ROOT, "no-such-directory")


def documented_commands():
    """(doc, module_name, argv) for every `python3 -m src.x` line in the docs."""
    for doc in DOCS:
        with open(os.path.join(ROOT, doc), encoding="utf-8") as handle:
            for line in handle:
                match = COMMAND.search(line)
                if not match:
                    continue
                argv = ["src." + match.group(1)]
                for arg in match.group(2).split():
                    if arg == "...":
                        continue  # a placeholder for more of the same
                    if "/" in arg:
                        arg = os.path.join(MISSING, os.path.basename(arg))
                    argv.append(arg)
                yield doc, match.group(1), argv


class TestDocumentedCommands(unittest.TestCase):
    def test_the_docs_contain_commands(self):
        found = {doc for doc, _, _ in documented_commands()}
        self.assertEqual(found, set(DOCS))

    def test_every_command_is_accepted_by_its_module(self):
        for doc, name, argv in documented_commands():
            self.assertIn(name, MODULES, "%s: unknown module %r" % (doc, name))
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    code = MODULES[name].main(argv)
            except OSError:
                continue  # got past argument parsing to the missing file
            self.assertNotEqual(code, 2, "%s prints usage for: %s"
                                         % (doc, " ".join(argv)))
