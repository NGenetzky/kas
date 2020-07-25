import os
import shutil
from kas import kas
from kas.libkas import run_cmd

import pytest

KAS_CONFIG = {
    'test.yml': """\
header:
  version: 8
repos:
  this:
  kas:
    url: https://github.com/siemens/kas.git
    refspec: 907816a5c4094b59a36aec12226e71c461c05b77
""",
}


@pytest.fixture
def changedir():
    yield
    os.chdir(os.path.join(os.path.dirname(__file__), '..'))


def test_repos_fetch(changedir, tmpdir):
    """
        Test that the local git clone is correctly updated when switching
        between a commit hash refspec and a branch refspec.
    """
    tdir = str(tmpdir.mkdir('test_repos_fetch'))
    shutil.rmtree(tdir, ignore_errors=True)
    # shutil.copytree('tests/test_refspec', tdir) # TODO create "{tdir}/test.yml"
    os.chdir(tdir)

    kas.kas(['shell', 'test.yml', '-c', 'true'])
    (rc, output) = run_cmd(['git', 'symbolic-ref', '-q', 'HEAD'], cwd='kas',
                           fail=False, liveupdate=False)
    assert rc != 0
    assert output.strip() == ''
    (rc, output) = run_cmd(['git', 'rev-parse', '-q', 'HEAD'], cwd='kas',
                           fail=False, liveupdate=False)
    assert rc == 0
    assert output.strip() == 'refs/heads/master'

    # TODO: Add more git remotes

    kas.kas(['shell', 'test.yml', '-c', 'true'])
    (rc, output) = run_cmd(['git', 'symbolic-ref', '-q', 'HEAD'], cwd='kas',
                           fail=False, liveupdate=False)
    kas.kas(['shell', 'test.yml', '-c', 'true'])
    (rc, output) = run_cmd(['git', 'symbolic-ref', '-q', 'HEAD'], cwd='kas',
                           fail=False, liveupdate=False)
    assert rc != 0
    assert output.strip() == ''
    (rc, output) = run_cmd(['git', 'rev-parse', '-q', 'HEAD'], cwd='kas',
                           fail=False, liveupdate=False)
    assert rc == 0
    assert output.strip() == 'refs/heads/master'
