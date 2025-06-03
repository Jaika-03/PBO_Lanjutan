import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout,
    QMessageBox, QComboBox
)

from abc import ABC, abstractmethod

# Kelas Abstrak dan Turunannya
class Kamar(ABC):
    def __init__(self, nama_pelanggan, jumlah_malam):
        self.__nama = nama_pelanggan         
        self.__jumlah_malam = jumlah_malam    
    
    def get_nama(self):
        return self.__nama
    
    def get_jumlah_malam(self):
        return self.__jumlah_malam

    @abstractmethod
    def hitung_total(self):
        pass

class KamarStandard(Kamar):
    def hitung_total(self):
        return 500000 * self.get_jumlah_malam()

class KamarVIP(Kamar):
    def hitung_total(self):
        total = 700000 * self.get_jumlah_malam()
        if self.get_jumlah_malam() > 3:
            total *= 0.85
        return total

# GUI
class HotelApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistem Reservasi Hotel Jaika")
        self.setGeometry(600, 100, 800, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Input Nama
        self.nama_label = QLabel("Nama Pelanggan:")
        self.nama_input = QLineEdit()

        # Pilihan Kamar
        self.kamar_label = QLabel("Pilih Tipe Kamar:")
        self.kamar_combo = QComboBox()
        self.kamar_combo.addItems(["Standard", "VIP (diskon 15% jika lebih dari 3 hari)"])

        # Input Jumlah Malam
        self.malam_label = QLabel("Jumlah Malam:")
        self.malam_input = QLineEdit()

        # Tombol
        self.hitung_btn = QPushButton("Hitung Total")
        self.hitung_btn.clicked.connect(self.hitung_total)

        # Label hasil
        self.hasil_label = QLabel("")

        # Tambah ke layout
        layout.addWidget(self.nama_label)
        layout.addWidget(self.nama_input)
        layout.addWidget(self.kamar_label)
        layout.addWidget(self.kamar_combo)
        layout.addWidget(self.malam_label)
        layout.addWidget(self.malam_input)
        layout.addWidget(self.hitung_btn)
        layout.addWidget(self.hasil_label)

        self.setLayout(layout)

    def hitung_total(self):
        try:
            nama = self.nama_input.text()
            tipe = self.kamar_combo.currentText()
            jumlah_malam = int(self.malam_input.text())

            if tipe == "Standard":
                kamar = KamarStandard(nama, jumlah_malam)
            else:
                kamar = KamarVIP(nama, jumlah_malam)

            total = kamar.hitung_total()

            self.hasil_label.setText(
                f"--- RINCIAN ---\nNama: {nama}\nKamar: {tipe}\nTotal: Rp{int(total)}"
            )

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Jumlah malam harus berupa angka!")

# Run
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HotelApp()
    window.show()
    sys.exit(app.exec_())
