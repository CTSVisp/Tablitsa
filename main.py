import sys
import csv
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView, QMessageBox
from PyQt6.QtCore import Qt

class PeriodicTableWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Периодическая таблица Менделеева')
        self.setGeometry(100, 100, 800, 400)

        layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(12)
        self.table_widget.setColumnCount(14)

        with open('periodic_table.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 5:
                    symbol = row[0]
                    full_name = row[1]
                    group = row[2]
                    period = row[3]
                    mass = row[4]

                    item = QTableWidgetItem(symbol)
                    item.setData(Qt.ItemDataRole.ToolTipRole, f"Полное название: {full_name}, Масса: {mass}")
                    self.table_widget.setItem(int(period) - 1, int(group) - 1, item)

        self.table_widget.setHorizontalHeaderLabels(["1", "2", "3", "4", "5", "6", "7", "8"])
        self.table_widget.setVerticalHeaderLabels(["1", "2", "3", "4.1", "4.2", "5.1", "5.2","6.1","6.2" ,"7","Лантаноиды","Актиноиды"])

        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        layout.addWidget(self.table_widget)
        self.setLayout(layout)

        self.table_widget.cellClicked.connect(self.show_element_details)

    def show_element_details(self, row, col):
        item = self.table_widget.item(row, col)
        element_info = item.data(Qt.ItemDataRole.ToolTipRole)
        QMessageBox.information(self, "Информация об элементе", element_info)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PeriodicTableWidget()
    window.show()
    sys.exit(app.exec())
