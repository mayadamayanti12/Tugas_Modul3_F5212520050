import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from models.anggota_model import AnggotaModel

@pytest.fixture
def model():
    return AnggotaModel()

def test_get_all_anggota_berhasil(model):
    # Veritabanından verileri çekme test edilir
    data = model.get_all_anggota()
    assert data is not None
    assert len(data) > 0

def test_create_anggota_berhasil(model):
    # Yeni üye ekleme fonksiyonu test edilir
    try:
        model.add_anggota("Test Nama", "Test Alamat")
        eklendi = True
    except Exception:
        eklendi = False
    
    assert eklendi is True