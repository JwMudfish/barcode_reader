import pyzbar.pyzbar as pyzbar
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

img_name = '88021485'

#img = cv2.imread(f'./images/{img_name}.jpg', cv2.IMREAD_GRAYSCALE)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# import matplotlib.pyplot as plt
# plt.imshow(img)

#decoded = pyzbar.decode(img)
decoded = pyzbar.decode(img)
'''
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
      #print(text)
    #print(barcode_data)
    #print(barcode_type)
      #cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
      cv2.putText(img, barcode_data, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
    except:
      print('------------------------------')
'''

print(len(decoded))
print(decoded)
