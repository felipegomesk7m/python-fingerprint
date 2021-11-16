from PyQt5 import QtGui, uic,QtWidgets
import cv2
import numpy as np
import sqlite3
import time
import fingerprint_enhancer
from matplotlib import pyplot as plt

def chama_tela_home():
    user = loginUi3.lineEdit_user.text()
    password = loginUi3.lineEdit_password.text()
    try:
      db=sqlite3.connect("Cadastros_Agentes.db")
      cursor=db.cursor()
      cursor.execute("SELECT Senha FROM Cadastro_Agentes WHERE Usuário = '{}';".format(user));
      senha_bd = cursor.fetchall()
      
      if user =="" and password =="":
        loginUi3.loginInvalido.setText("Campos Vazios")
      elif senha_bd[0][0] == password:
        loginUi3.close()
        if user == 'fgomes96':
          tipo_de_acesso(1)
        elif user == 'hboracine01':
          tipo_de_acesso(2)
        elif user == 'gbajona01':
          tipo_de_acesso(3)   
      else:
        loginUi3.loginInvalido.setText("Dados de Login ou Senha Incorretos")
    except:
      loginUi3.loginInvalido.setText("Dados de Login ou Senha Incorretos")
    finally:
      db.close()

def tipo_de_acesso(acesso):
  acesso_bd = acesso
  if acesso_bd == 1:
    autenticar()
    home.lineEdit.setText('Felipe Gomes')
    home.lineEdit_2.setText('1')
    home.label_4.setText('Informações do nível 1 - Produção agrícola\n Nome da unidade produtora (produtor agrícola) – Bom Futuro\n Endereço do produtor agrícola - Av. dos Florais, S/N - Ribeirão do Lipa, Cuiabá - MT\n Produto(s) agrícolas produzidos – Soja, milho e algodão\n Produção anual em quilogramas – Aproximadamente 1,7 milhão de toneladas\n Destino da produção (mercado interno ou exportação)\n Número de empregados da unidade produtora - 5 mil\n Quantidade de máquinas e implementos agrícolas – Em torno de 400 máquinas, sendo elas tanto para colheita,\nquanto caminhões de transporte\n Nível de automação da unidade produtora – Alto nível, sendo a maior produtora agrícola do Brasil')  
  elif acesso_bd == 2:
    autenticar()
    home.lineEdit.setText('Heitor Boracine')
    home.lineEdit_2.setText('2')
    home.label_4.setText('Incentivos fiscais recebidos – Anistia, antecipação de receitas, refinanciamento tributário, entre outros.\n Impostos municipais pagos – IPTU (Imposto Predial Territorial Urbano)\n*poderá incidir caso trata-se de propriedade localizada em zona urbana ou urbanizada*;\n ISSQN (Imposto Sobre Serviços de Qualquer Natureza).\n Impostos estaduais recolhidos – ICMS (Imposto sobre Circulação de Mercadorias);\n IPVA (Imposto sobre Propriedade de Veículos Automotores).\n Impostos federais pagos – IRPJ (Imposto de Renda);\n IE (Imposto de Exportação);\n ITR (Imposto Territorial Rural)\n *poderá incidir caso trata-se de propriedade localizada em zona rural*; Cofins, PIS PASEP, CSLL, INSS.\n Taxas federais pagas – Taxa de licenciamento ambiental para instalação e operação da empresa.')  
  elif acesso_bd == 3:
    autenticar() 
    home.lineEdit.setText('Gabriel Bajona')
    home.lineEdit_2.setText('3')
    home.label_4.setText('Agrotóxicos empregados nas produções agrícolas - glifosato; mancozebe; acefato; óleo mineral; atrazina;\n Ação do sistema: quando da ocorrência de agrotóxicos proibidos, notificar a unidade produtora quanto a interdição da produção.')  
    

def autenticar():
  biometria.show()
  biometria.progressBar.setRange(0,100)
  biometria.progressBar.setValue(0)
  biometria.label.setPixmap(QtGui.QPixmap(''))
  biometria.image.setPixmap(QtGui.QPixmap(''))
  
  def progress():
    counter = 0
    biometria.image.setPixmap(QtGui.QPixmap('fingerprint.png'))
    biometria.text_progressbar.setText('Recebendo imagem por arquivo')
    
    while (int(counter) <= 100):
      MIN_MATCH_COUNT = 10
      if counter == 25:
        biometria.text_progressbar.setText('Aplicando Binarização')
        img1	=	cv2.imread('fingerprint.png',	0)
        img2 = cv2.imread('fingerprint2.png') 
        img1 = fingerprint_enhancer.enhance_Fingerprint(img1)
        img2 = fingerprint_enhancer.enhance_Fingerprint(img2)
        cv2.imwrite("img_binarizada.png", img1)
        biometria.image.setPixmap(QtGui.QPixmap('img_binarizada.png'))
      
      if counter == 50:
        biometria.text_progressbar.setText('Extração de Características')
        # Iniciando SIFT
        sift = cv2.SIFT_create()
        # Encontrando Keypoints e descriptors com SIFT
        kp1, des1 = sift.detectAndCompute(img1,None)
        kp2, des2 = sift.detectAndCompute(img2,None)
        kp_img = cv2.drawKeypoints(img1, kp1, None, color=(0, 255, 0),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imwrite("keypoints.png",kp_img)
        biometria.image.setPixmap(QtGui.QPixmap('keypoints.png'))
        time.sleep(2)
      
      if counter == 75:
        biometria.image.setPixmap(QtGui.QPixmap(''))
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 10)
        search_params = dict(checks = 50)
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des1,des2,k=2)
        # Agrupando todos os matches
        good = []
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append(m)
        # Verificando os matches e entregando resultado
        if len(good)>MIN_MATCH_COUNT:
            src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
            dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
            matchesMask = mask.ravel().tolist()
            h,w = img1.shape
            pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
            dst = cv2.perspectiveTransform(pts,M)
            img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)
            print("Obteve matches o suficiente - {}/{}".format(len(good), MIN_MATCH_COUNT))
            biometria.text_progressbar.setText("Obteve matches o suficiente - {}/{}".format(len(good), MIN_MATCH_COUNT))
        else:
            print("Não obteve matches o suficiente - {}/{}".format(len(good), MIN_MATCH_COUNT))
            biometria.text_progressbar.setText("Não obteve matches o suficiente - {}/{}".format(len(good), MIN_MATCH_COUNT))
            matchesMask = None
        draw_params = dict(matchColor = (0,255,0), 
                          singlePointColor = None,
                          matchesMask = matchesMask, 
                          flags = 2)
        img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
        plt.imshow(img3,)
        plt.savefig('Matches.png', format='png')
        biometria.label.setPixmap(QtGui.QPixmap('Matches.png'))
        time.sleep(2)
      
      counter += 1
      biometria.progressBar.setValue(int(counter))
      time.sleep(0.1)

      if counter == 100:
        biometria.text_progressbar.setText('Biometria Validada')
        biometria.image.setPixmap(QtGui.QPixmap('Matches.png'))
        time.sleep(5)
        biometria.close()
        home.show()

  biometria.pushButton.clicked.connect(lambda: progress())

def logout():
  home.close()
  loginUi3.show()
  loginUi3.lineEdit_user.setText("")
  loginUi3.lineEdit_password.setText("")
  loginUi3.loginInvalido.setText("")
    
app=QtWidgets.QApplication([])
loginUi3 = uic.loadUi('loginUi3.ui')
home = uic.loadUi('home.ui')
biometria = uic.loadUi('biometria.ui')
loginUi3.btn_acessar.clicked.connect(chama_tela_home)
home.pushButton.clicked.connect(logout)
loginUi3.show()
app.exec()
