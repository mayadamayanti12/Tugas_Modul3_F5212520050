import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from models.buku_model import BukuModel

@pytest.fixture
def buku_model():
    return BukuModel()

def test_create_buku_berhasil(buku_model):
    try:
        # Mengecek method apa yang tersedia di BukuModel kamu secara dinamis
        if hasattr(buku_model, 'add_buku'):
            buku_model.add_buku("Pemrograman Python MVC", "Guido van Rossum", "2023")
        elif hasattr(buku_model, 'create_buku'):
            buku_model.create_buku("Pemrograman Python MVC", "Guido van Rossum", "2023")
        else:
            buku_model.insert_buku("Pemrograman Python MVC", "Guido van Rossum", "2023")
        berhasil = True
    except Exception as e:
        print("Error:", e)
        berhasil = False
        
    assert berhasil is True

def test_get_all_buku_berhasil(buku_model):
    # Mengambil data buku dengan aman berdasarkan method yang ada
    data = buku_model.get_all_buku() if hasattr(buku_model, 'get_all_buku') else buku_model.get_buku()
    assert data is not None