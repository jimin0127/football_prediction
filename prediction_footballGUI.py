from PyQt5.QtWidgets import  QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QComboBox, QLabel
from PyQt5.QtCore import Qt
import sys
import prediction_football as pf

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        apply_btn = QPushButton('확인', self)
        team1 = QComboBox(self)
        team2 = QComboBox(self)
        label1 = QLabel('경기할 두 팀을 골라주세요.')
        vs_label = QLabel('VS', self)

        team_list = ['리버풀', '맨시티', '맨유', '첼시', '레스터', '토트넘', '울버햄튼',
                     '아스널', '셰필드', '번리', '샤우샘프턴', '에버턴', '뉴캐슬',
                     '브라이튼', '팰리스', '웨스트햄', '아스톤 빌라', '본머스', '왓포드', '노리치']
        for team in team_list:
            team1.addItem(team)
            team2.addItem(team)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(label1)
        hbox.addStretch(1)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(team1)
        hbox1.addStretch(1)
        hbox1.addWidget(vs_label)
        hbox1.addStretch(1)
        hbox1.addWidget(team2)
        hbox1.addStretch(1)


        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(apply_btn)
        hbox2.addStretch(1)


        # v
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(2)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)

        self.setLayout(vbox)


        self.setWindowTitle('My Furst Appilcation')
        self.resize(700, 800)
        # self.setGeometry(300, 400, 400, 200)
        self.center()
        self.show()


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