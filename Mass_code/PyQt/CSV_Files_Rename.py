import sys
from PyQt5.QtCore import (QDir, QIODevice, QFile, QFileInfo, Qt, QTextStream,
        QUrl)
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QComboBox,
        QDialog, QFileDialog, QGridLayout, QHBoxLayout, QHeaderView, QLabel,
        QProgressDialog, QPushButton, QSizePolicy, QTableWidget,
        QTableWidgetItem)

class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
                     
        browseButton = self.createButton("&Browse", self.browse)
        findButton = self.createButton("&Find",self.find)

        processButton=self.createButton("&Rename",self.process)



        self.directoryComboBox = self.createComboBox(QDir.currentPath())
        directoryLabel = QLabel("CSV directory:")


        self.filesFoundLabel = QLabel()
        self.createFilesTable()

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addStretch()
        buttonsLayout.addWidget(findButton)
        buttonsLayout.addWidget(processButton)

        self.textlabel= QLabel()

        #textLabel = QLabel("Containing text:")

        mainLayout = QGridLayout()

        mainLayout.addWidget(directoryLabel, 2, 0)
        mainLayout.addWidget(self.directoryComboBox, 2, 1)
        mainLayout.addWidget(browseButton, 2, 2)
        mainLayout.addWidget(self.filesTable,3,0,1,3)
        mainLayout.addWidget(self.filesFoundLabel,4,0)
        mainLayout.addLayout(buttonsLayout, 5, 0, 1, 3)

        mainLayout.addWidget(processButton, 6, 0, 1, 3)
        mainLayout.addWidget(self.textlabel, 7, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle('CSV_Files_Rename')  
        self.resize(700, 500)

    def browse(self):
        directory = QFileDialog.getExistingDirectory(self, "CSV_Files_Rename",
                QDir.currentPath())

        if directory:
            if self.directoryComboBox.findText(directory) == -1:
                self.directoryComboBox.addItem(directory)

            self.directoryComboBox.setCurrentIndex(self.directoryComboBox.findText(directory))
   
    @staticmethod
    def updateComboBox(comboBox):
        if comboBox.findText(comboBox.currentText()) == -1:
            comboBox.addItem(comboBox.currentText())

    def find(self):
        self.filesTable.setRowCount(0)
        path = self.directoryComboBox.currentText()
        self.updateComboBox(self.directoryComboBox)
        self.currentDir = QDir(path)
        files = self.currentDir.entryList(QDir.Files | QDir.NoSymLinks)
        self.showFiles(files)

    def findFiles(self, files, text):
        progressDialog = QProgressDialog(self)

        progressDialog.setCancelButtonText("&Cancel")
        progressDialog.setRange(0, files.count())
        progressDialog.setWindowTitle("Find Files")

        foundFiles = []

        for i in range(files.count()):
            progressDialog.setValue(i)
            progressDialog.setLabelText("Searching file number %d of %d..." % (i, files.count()))
            QApplication.processEvents()

            if progressDialog.wasCanceled():
                break

            inFile = QFile(self.currentDir.absoluteFilePath(files[i]))

            if inFile.open(QIODevice.ReadOnly):
                stream = QTextStream(inFile)
                while not stream.atEnd():
                    if progressDialog.wasCanceled():
                        break
                    line = stream.readLine()
                    if text in line:
                        foundFiles.append(files[i])
                        break

        progressDialog.close()

        return foundFiles

    def showFiles(self, files):
        for fn in files:
            file = QFile(self.currentDir.absoluteFilePath(fn))
            size = QFileInfo(file).size()

            fileNameItem = QTableWidgetItem(fn)
            fileNameItem.setFlags(fileNameItem.flags() ^ Qt.ItemIsEditable)
            sizeItem = QTableWidgetItem("%d KB" % (int((size + 1023) / 1024)))
            sizeItem.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
            sizeItem.setFlags(sizeItem.flags() ^ Qt.ItemIsEditable)

            row = self.filesTable.rowCount()
            self.filesTable.insertRow(row)
            self.filesTable.setItem(row, 0, fileNameItem)
            self.filesTable.setItem(row, 1, sizeItem)

        self.filesFoundLabel.setText("%d file(s) found (Double click on a file to open it)" % len(files))


    def createButton(self, text, member):
        button = QPushButton(text)
        button.clicked.connect(member)
        return button

    def createComboBox(self, text=""):
        comboBox = QComboBox()
        comboBox.setEditable(True)
        comboBox.addItem(text)
        comboBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        return comboBox
    def createFilesTable(self):
        self.filesTable=QTableWidget(0,2)
        self.filesTable.setSelectionBehavior(QAbstractItemView.SelectColumns)

        self.filesTable.setHorizontalHeaderLabels(("File Name","Size"))
        self.filesTable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.filesTable.verticalHeader().hide()
        self.filesTable.setShowGrid(False)

        self.filesTable.cellActivated.connect(self.openFileOfItem)
    def openFileOfItem(self,row,colum):
        item=self.filesTable.item(row,0)
        QDesktopServices.openUrl(QUrl(self.currentDir.absoluteFilePath(item.text())))

    def process(self):
        self.textlabel.setText(self.directoryComboBox.currentText())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

