# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_window_qt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProjectWindow(object):
    def setupUi(self, ProjectWindow):
        ProjectWindow.setObjectName("ProjectWindow")
        ProjectWindow.resize(701, 555)
        self.centralwidget = QtWidgets.QWidget(ProjectWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mainProjectLayout = QtWidgets.QHBoxLayout()
        self.mainProjectLayout.setObjectName("mainProjectLayout")
        self.projectListLayout = QtWidgets.QVBoxLayout()
        self.projectListLayout.setObjectName("projectListLayout")
        self.projectTree = QtWidgets.QTreeWidget(self.centralwidget)
        self.projectTree.setAutoFillBackground(False)
        self.projectTree.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.projectTree.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.projectTree.setTabKeyNavigation(True)
        self.projectTree.setAlternatingRowColors(False)
        self.projectTree.setRootIsDecorated(True)
        self.projectTree.setUniformRowHeights(True)
        self.projectTree.setAnimated(True)
        self.projectTree.setWordWrap(True)
        self.projectTree.setHeaderHidden(True)
        self.projectTree.setObjectName("projectTree")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.projectTree.headerItem().setFont(0, font)
        self.projectTree.header().setVisible(False)
        self.projectTree.header().setCascadingSectionResizes(False)
        self.projectTree.header().setHighlightSections(True)
        self.projectTree.header().setSortIndicatorShown(False)
        self.projectListLayout.addWidget(self.projectTree)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.projectExpandButton = QtWidgets.QPushButton(self.centralwidget)
        self.projectExpandButton.setObjectName("projectExpandButton")
        self.horizontalLayout.addWidget(self.projectExpandButton)
        self.projectCollapseButton = QtWidgets.QPushButton(self.centralwidget)
        self.projectCollapseButton.setObjectName("projectCollapseButton")
        self.horizontalLayout.addWidget(self.projectCollapseButton)
        self.projectListLayout.addLayout(self.horizontalLayout)
        self.mainProjectLayout.addLayout(self.projectListLayout)
        self.projectInfoLayout = QtWidgets.QVBoxLayout()
        self.projectInfoLayout.setObjectName("projectInfoLayout")
        self.projectName = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectName.sizePolicy().hasHeightForWidth())
        self.projectName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.projectName.setFont(font)
        self.projectName.setText("")
        self.projectName.setAlignment(QtCore.Qt.AlignCenter)
        self.projectName.setWordWrap(True)
        self.projectName.setObjectName("projectName")
        self.projectInfoLayout.addWidget(self.projectName)
        self.researcherLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.researcherLabel.setFont(font)
        self.researcherLabel.setObjectName("researcherLabel")
        self.projectInfoLayout.addWidget(self.researcherLabel)
        self.researcherValue = QtWidgets.QLabel(self.centralwidget)
        self.researcherValue.setText("")
        self.researcherValue.setIndent(20)
        self.researcherValue.setObjectName("researcherValue")
        self.projectInfoLayout.addWidget(self.researcherValue)
        self.createdLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.createdLabel.setFont(font)
        self.createdLabel.setObjectName("createdLabel")
        self.projectInfoLayout.addWidget(self.createdLabel)
        self.createdValue = QtWidgets.QLabel(self.centralwidget)
        self.createdValue.setText("")
        self.createdValue.setIndent(20)
        self.createdValue.setObjectName("createdValue")
        self.projectInfoLayout.addWidget(self.createdValue)
        self.dirLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dirLabel.setFont(font)
        self.dirLabel.setObjectName("dirLabel")
        self.projectInfoLayout.addWidget(self.dirLabel)
        self.dirValue = QtWidgets.QLabel(self.centralwidget)
        self.dirValue.setText("")
        self.dirValue.setIndent(20)
        self.dirValue.setObjectName("dirValue")
        self.projectInfoLayout.addWidget(self.dirValue)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.projectInfoLayout.addItem(spacerItem)
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.openButton.setFont(font)
        self.openButton.setObjectName("openButton")
        self.projectInfoLayout.addWidget(self.openButton)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName("deleteButton")
        self.projectInfoLayout.addWidget(self.deleteButton)
        self.mainProjectLayout.addLayout(self.projectInfoLayout)
        self.mainProjectLayout.setStretch(0, 2)
        self.mainProjectLayout.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.mainProjectLayout)
        ProjectWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ProjectWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 21))
        self.menubar.setObjectName("menubar")
        self.menuProject = QtWidgets.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")
        ProjectWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ProjectWindow)
        self.statusbar.setObjectName("statusbar")
        ProjectWindow.setStatusBar(self.statusbar)
        self.actionNewProject = QtWidgets.QAction(ProjectWindow)
        self.actionNewProject.setObjectName("actionNewProject")
        self.actionExit = QtWidgets.QAction(ProjectWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuProject.addAction(self.actionNewProject)
        self.menuProject.addAction(self.actionExit)
        self.menubar.addAction(self.menuProject.menuAction())

        self.retranslateUi(ProjectWindow)
        QtCore.QMetaObject.connectSlotsByName(ProjectWindow)

    def retranslateUi(self, ProjectWindow):
        _translate = QtCore.QCoreApplication.translate
        ProjectWindow.setWindowTitle(_translate("ProjectWindow", "Project Manager"))
        self.projectTree.setSortingEnabled(False)
        self.projectTree.headerItem().setText(0, _translate("ProjectWindow", "Bookmarks"))
        self.projectExpandButton.setStatusTip(_translate("ProjectWindow", "Expand all projects in list"))
        self.projectExpandButton.setText(_translate("ProjectWindow", "Expand All"))
        self.projectCollapseButton.setStatusTip(_translate("ProjectWindow", "Collapse all projects in list"))
        self.projectCollapseButton.setText(_translate("ProjectWindow", "Collapse All"))
        self.researcherLabel.setText(_translate("ProjectWindow", "Researcher:"))
        self.createdLabel.setText(_translate("ProjectWindow", "Date created:"))
        self.dirLabel.setText(_translate("ProjectWindow", "Project path:"))
        self.openButton.setStatusTip(_translate("ProjectWindow", "Open selected project"))
        self.openButton.setText(_translate("ProjectWindow", "Open"))
        self.deleteButton.setText(_translate("ProjectWindow", "Delete Bookmark"))
        self.menuProject.setTitle(_translate("ProjectWindow", "Project"))
        self.actionNewProject.setText(_translate("ProjectWindow", "New Project Bookmark"))
        self.actionNewProject.setStatusTip(_translate("ProjectWindow", "Create new project"))
        self.actionExit.setText(_translate("ProjectWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("ProjectWindow", "Exit the battery"))

