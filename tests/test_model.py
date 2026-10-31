import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from unittest.mock import patch, MagicMock
from models.buku_model import BukuModel


@patch("models.buku_model.get_db_connection")
def test_create_buku_berhasil(mock_get_conn):
    # Koneksi dan cursor palsu, tidak menyentuh MySQL asli
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_get_conn.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    model = BukuModel()
    model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)

    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()


@patch("models.buku_model.get_db_connection")
def test_get_all_buku_berhasil(mock_get_conn):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_get_conn.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        {"id_buku": 1, "judul": "Pemrograman Python MVC",
         "penulis": "Guido van Rossum", "tahun_terbit": 2023}
    ]

    model = BukuModel()
    data = model.get_all_buku()

    assert data is not None
    assert len(data) == 1
    assert data[0]["judul"] == "Pemrograman Python MVC"