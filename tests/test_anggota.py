import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from unittest.mock import patch, MagicMock
from models.anggota_model import AnggotaModel


@patch.object(AnggotaModel, "setup_database")
@patch("models.anggota_model.mysql.connector.connect")
def test_get_all_anggota_berhasil(mock_connect, mock_setup):
    # Koneksi dan cursor palsu, tidak menyentuh MySQL asli
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        {"id_anggota": 1, "nama_anggota": "Test Nama", "alamat": "Test Alamat"}
    ]

    model = AnggotaModel()
    data = model.get_all_anggota()

    assert data is not None
    assert len(data) == 1
    assert data[0]["nama_anggota"] == "Test Nama"
    mock_cursor.execute.assert_called_once()


@patch.object(AnggotaModel, "setup_database")
@patch("models.anggota_model.mysql.connector.connect")
def test_create_anggota_berhasil(mock_connect, mock_setup):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    model = AnggotaModel()
    model.add_anggota("Test Nama", "Test Alamat")

    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()