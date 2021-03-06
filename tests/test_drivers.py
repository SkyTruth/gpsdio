"""
Unittests for gpsdio.drivers
"""


import sys

import pytest

import gpsdio.drivers


def test_get_compression():
    assert gpsdio.drivers.GZIPDriver == gpsdio.drivers._COMPRESSION['GZIP']
    with pytest.raises(KeyError):
        gpsdio.drivers._COMPRESSION["bad-name"]


def test_gzip_cannot_read_from_stdin():
    d = gpsdio.drivers.GZIPDriver()
    with pytest.raises(IOError):
        d.open(name=sys.stdin, mode='r')


def test_msg_bz2_round_robin(types_msg_bz2_path, tmpdir):
    pth = str(tmpdir.mkdir('test').join('test_bz2_round_robin.msg.bz2'))
    with gpsdio.open(types_msg_bz2_path) as src, gpsdio.open(pth, 'w') as dst:
        for msg in src:
            dst.write(msg)


def test_msg_gz_round_robin(types_msg_gz_path, tmpdir):
    pth = str(tmpdir.mkdir('test').join('test_gz_round_robin.msg.gz'))
    with gpsdio.open(types_msg_gz_path) as src, gpsdio.open(pth, 'w') as dst:
        for msg in src:
            dst.write(msg)


def test_open_gzip(types_json_gz_path):
    with open(types_json_gz_path, 'rb') as f:
        with gpsdio.open(f, driver='NewlineJSON', compression='GZIP') as src:
            for msg in src:
                assert 'mmsi' in msg
                assert 'type' in msg
                assert 'timestamp' in msg
