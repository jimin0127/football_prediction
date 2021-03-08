from PyQt5.QtWidgets import  QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QComboBox, QLabel, QDialog
from PyQt5.QtGui import QImage, QPalette, QBrush
import PyQt5.QtGui as QtGui
from PyQt5.QtCore import Qt, QSize
import sys
from prediction_football import prediction_football

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        bg_img = QImage('Football-player-match_1920x1080.jpg')
        bg_img = bg_img.scaled(QSize(700, 800))
        palette = QPalette()
        palette.setBrush(10, QBrush(bg_img))
        self.setPalette(palette)

        apply_btn = QPushButton('확인', self)
        #apply_btn.resize(100, 100)
        apply_btn.setMaximumHeight(500)
        apply_btn.clicked.connect(self.predict_result)

        self.team1_combo = QComboBox(self)
        self.team2_combo = QComboBox(self)
        self.team1_combo.setFont(QtGui.QFont('돋움', 10))
        self.team2_combo.setFont(QtGui.QFont('돋움', 10))
        self.team1_combo.activated.connect(self.onActivated_1)
        self.team2_combo.activated.connect(self.onActivated_2)

        label1 = QLabel('경기할 두 팀을 골라주세요.')
        label1.setObjectName('label1')
        label1.setStyleSheet('QLabel#label1 {color : white}')

        label1.setFont(QtGui.QFont('돋움', 20))


        vs_label = QLabel('VS', self)

        self.team_list = ['리버풀', '맨시티', '맨유', '첼시', '레스터', '토트넘', '울버햄튼',
                     '아스널', '셰필드', '번리', '샤우샘프턴', '에버턴', '뉴캐슬',
                     '브라이튼', '팰리스', '웨스트햄', '아스톤 빌라', '본머스', '왓포드', '노리치']
        for team in self.team_list:
            self.team1_combo.addItem(team)
            self.team2_combo.addItem(team)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(label1)
        self.hbox.addStretch(1)

        self.hbox1 = QHBoxLayout()
        self.hbox1.addStretch(1)
        self.hbox1.addWidget(self.team1_combo)
        self.hbox1.addStretch(1)
        self.hbox1.addWidget(vs_label)
        self.hbox1.addStretch(1)
        self.hbox1.addWidget(self.team2_combo)
        self.hbox1.addStretch(1)


        self.hbox2 = QHBoxLayout()
        self.hbox2.addStretch(1)
        self.hbox2.addWidget(apply_btn)
        self.hbox2.addStretch(1)


        # v
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addStretch(2)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addStretch(1)

        self.setLayout(self.vbox)


        self.setWindowTitle('My Furst Appilcation')
        self.resize(700, 800)
        # self.setGeometry(300, 400, 400, 200)
        self.center()
        self.show()

    def onActivated_1(self, text):
        self.team1 = self.team_list[text]

    def onActivated_2(self, text):
        self.team2 = self.team_list[text]

    def predict_result(self):
        print(self.team1, self.team2)
        if self.team1 == self.team2 :
            print('.')
            self.show_exception()
            return

        pr = prediction_football(self.team1, self.team2)
        winner = pr.get_winner()
        print(winner)
        self.show_dialog(winner)

    def show_exception(self):
        self.exception_dialog = QDialog()
        label1 = QLabel('중복된 팀을 선택하셨습니다. 다시 선택해주세요', self.exception_dialog)
        label1.move(100, 100)
        self.btn = QPushButton('확인', self.exception_dialog)
        self.btn.clicked.connect(self.exception_dialog_close)

        self.exception_dialog.setWindowTitle('Dialog')
        self.exception_dialog.setWindowModality(Qt.ApplicationModal)
        self.exception_dialog.resize(300, 200)
        self.exception_dialog.show()

    def exception_dialog_close(self):
        self.exception_dialog.close()

    def show_dialog(self, winner):
        self.result_dialog = QDialog()
        label1 = QLabel('예상 경기 결과 : ' + winner + '승', self.result_dialog)

        label1.move(100, 100)

        self.result_dialog.setWindowTitle('Dialog')
        self.result_dialog.setWindowModality(Qt.ApplicationModal)
        self.result_dialog.resize(300, 200)
        self.center()
        self.result_dialog.show()


    # 화면 가운데로 맞추기
    def center(self):
        # 창의 위치와 크기 정보 가져오기
        qr = self.frameGeometry()
        # 사용하는 모니터 가운데 위치
        cp = QDesktopWidget().availableGeometry().center()
        # 창의 중심을 화면의 중심으로 이동
        qr.moveCenter(cp)
        # 현재의 창을 qr의 위치로 옮긴다.
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())