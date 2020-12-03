import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import ZBarSymbol

import cv2

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased
from keys import keys
import models
engine = create_engine(f'postgresql://postgres:{keys.get("postgres", "./keys")}@database-1.ctnphj2dxhnf.ap-northeast-2.rds.amazonaws.com/emart24')
Session = sessionmaker(bind=engine)
session = Session()

def get_design_infer_labels(goods_id):
    result = session.query(models.Design.design_infer_label).filter_by(goods_id=goods_id).all()
    return result

def nothing(x):
    pass


cap = cv2.VideoCapture(6)


MJPG_CODEC = 1196444237.0 # MJPG


cap.set(cv2.CAP_PROP_BRIGHTNESS, 10)
cap.set(cv2.CAP_PROP_FOURCC, MJPG_CODEC)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1980)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1060)


cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
cap.set(cv2.CAP_PROP_FOCUS, 0)

#print(get_goods_name('8801056098834'))
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 1980,1060)

#FOCUS = 100

i = 0
while(cap.isOpened()):
  ret, img = cap.read()
  #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  img = cv2.GaussianBlur(img, (0,0), 1.0)

  #cap.set(cv2.CAP_PROP_FOCUS, FOCUS)
  print(cv2.CAP_PROP_FRAME_WIDTH)


  if not ret:
    continue

  #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     
  decoded = pyzbar.decode(img)

  for d in decoded: 
    x, y, w, h = d.rect

    barcode_data = d.data.decode("utf-8")
    barcode_type = d.type

    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    #text = '%s (%s)' % (barcode_data, barcode_type)
    text = '%s' % (barcode_data)
    try:
      #text = get_design_infer_labels(text)[0][0]
    #goods_name = get_goods_name(str(barcode_data))
    
    ##print(barcode_data)
    #print(barcode_type)
      #cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
      cv2.putText(img, barcode_data, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
    except:
      print('------------------------------')

  #FOCUS = cv2.getTrackbarPos('Focus', 'img') - 100

  cv2.imshow('img', img)

  key = cv2.waitKey(1)
  if key == ord('q'):
    break
  
  #elif key == ord('c'):
    #cv2.imwrite(f'./images/{}.jpg', img)

  
  elif key == ord('+'):
    FOCUS = FOCUS + 2
    print(FOCUS)
    
  elif key == ord('-'):
    FOCUS = FOCUS -2
    print(FOCUS)

cap.release()
cv2.destroyAllWindows()
