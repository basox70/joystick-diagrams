# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configure.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QListView, QListWidget,
    QListWidgetItem, QSizePolicy, QTabWidget, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1050, 651)
        self.activeScreenWidget = QWidget(Form)
        self.activeScreenWidget.setObjectName(u"activeScreenWidget")
        self.activeScreenWidget.setGeometry(QRect(0, 0, 1041, 631))
        self.verticalLayout_2 = QVBoxLayout(self.activeScreenWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.activeScreenWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.activeScreenWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.tabWidget = QTabWidget(self.activeScreenWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget = QWidget(self.tab_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 1001, 521))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.profileList = QListWidget(self.verticalLayoutWidget)
        QListWidgetItem(self.profileList)
        QListWidgetItem(self.profileList)
        QListWidgetItem(self.profileList)
        QListWidgetItem(self.profileList)
        QListWidgetItem(self.profileList)
        self.profileList.setObjectName(u"profileList")
        self.profileList.setDragEnabled(True)
        self.profileList.setDragDropOverwriteMode(True)
        self.profileList.setDragDropMode(QAbstractItemView.DragOnly)
        self.profileList.setViewMode(QListView.ListMode)
        self.profileList.setSelectionRectVisible(False)

        self.horizontalLayout.addWidget(self.profileList)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.horizontalLayout.addLayout(self.verticalLayout_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayoutWidget_2 = QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 1001, 521))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.comboBox)

        self.treeWidget = QTreeWidget(self.verticalLayoutWidget_2)
        QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem2)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setProperty("showDropIndicator", False)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setCascadingSectionResizes(True)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setProperty("showSortIndicator", True)
        self.treeWidget.header().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.treeWidget)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Configure</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"... setup your profiles/binds", None))

        __sortingEnabled = self.profileList.isSortingEnabled()
        self.profileList.setSortingEnabled(False)
        ___qlistwidgetitem = self.profileList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"DCS World - A10C2", None));
        ___qlistwidgetitem1 = self.profileList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"DCS World - FA18", None));
        ___qlistwidgetitem2 = self.profileList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"Joystick Gremlin - Base", None));
        ___qlistwidgetitem3 = self.profileList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"Joystick Gremlin - A10C", None));
        ___qlistwidgetitem4 = self.profileList.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Form", u"Joystick Gremlin - FA18", None));
        self.profileList.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Profile Setup", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"FA-18", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"A10-C", None))

        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"Action", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"Control", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"Device", None));

        __sortingEnabled1 = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("Form", u"Go Fast", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Form", u"AXIS X", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Form", u"Throttle 1", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("Form", u"Fire Guns", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("Form", u"BUTTON 1", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Form", u"Joystick_1", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("Form", u"Drop Ordnance", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("Form", u"+CTRL", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Form", u"Modifier", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("Form", u"Drop something else", None));
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("Form", u"+CTRL ALT", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Form", u"Modifier", None));
        ___qtreewidgetitem5 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("Form", u"Fire the lasers", None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("Form", u"BUTTON 2", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("Form", u"Joystick_1", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(2, QCoreApplication.translate("Form", u"Reload", None));
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("Form", u"+ ALT", None));
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("Form", u"Modifier", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled1)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Customise Binds", None))
    # retranslateUi

