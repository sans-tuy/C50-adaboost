def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Bilirubin", "instances": 117, "metric_value": 0.0, "depth": 4}
            if obj[1]<=12.914529914529915:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 91, "metric_value": -0.0, "depth": 5}
               if obj[8]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 70, "metric_value": 0.0, "depth": 6}
                  if obj[4]>10:
                     # {"feature": "Direct_Bilirubin", "instances": 69, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 61, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=41.295081967213115:
                           return 'liver'
                        elif obj[5]>41.295081967213115:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        # {"feature": "Total_Protiens", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=66:
                           return 'normal'
                        elif obj[6]>66:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=10:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[8]<=1:
                  # {"feature": "Total_Protiens", "instances": 21, "metric_value": 0.0, "depth": 6}
                  if obj[6]>63:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[5]>23:
                        return 'liver'
                     elif obj[5]<=23:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[6]<=63:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]>24:
                        return 'liver'
                     elif obj[4]<=24:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[1]>12.914529914529915:
               # {"feature": "Direct_Bilirubin", "instances": 26, "metric_value": -0.0, "depth": 5}
               if obj[2]>4:
                  # {"feature": "Total_Protiens", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[6]>54:
                     # {"feature": "Alamine_Aminotransferase", "instances": 20, "metric_value": -0.0, "depth": 7}
                     if obj[4]>22:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=202:
                           return 'liver'
                        elif obj[5]>202:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=22:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>20:
                           return 'liver'
                        elif obj[5]<=20:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=54:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=4:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[8]>9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=30:
                        return 'normal'
                     elif obj[4]>30:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=9:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 35, "metric_value": -0.0, "depth": 4}
            if obj[6]<=73:
               # {"feature": "Alamine_Aminotransferase", "instances": 28, "metric_value": -0.0, "depth": 5}
               if obj[4]<=67.57142857142857:
                  # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[2]>3:
                     return 'liver'
                  elif obj[2]<=3:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>30:
                           return 'liver'
                        elif obj[5]<=30:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>67.57142857142857:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[6]>73:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": -0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[6]>47.123456790123456:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 54, "metric_value": -0.0, "depth": 5}
               if obj[8]<=11:
                  # {"feature": "Alamine_Aminotransferase", "instances": 47, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=40.02127659574468:
                     # {"feature": "Direct_Bilirubin", "instances": 33, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=31:
                           return 'liver'
                        elif obj[1]>31:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=28:
                           return 'liver'
                        elif obj[5]>28:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>40.02127659574468:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=181:
                        # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=184:
                           return 'liver'
                        elif obj[1]>184:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>181:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>11:
                  # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=5:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=21:
                        return 'liver'
                     elif obj[4]>21:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'liver'
                        elif obj[1]>6:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]>5:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=47.123456790123456:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 27, "metric_value": -0.0, "depth": 5}
               if obj[8]<=14:
                  # {"feature": "Alamine_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[4]>22:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 20, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=53:
                        # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>53:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=22:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>14:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[2]>2:
                     return 'liver'
                  elif obj[2]<=2:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=7:
                        return 'normal'
                     elif obj[1]>7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Bilirubin", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[1]<=128.79616352900172:
               # {"feature": "Direct_Bilirubin", "instances": 30, "metric_value": -0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 26, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 7}
                     if obj[4]>31:
                        # {"feature": "Total_Protiens", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[6]>52:
                           return 'liver'
                        elif obj[6]<=52:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=31:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[4]>64:
                        # {"feature": "Total_Protiens", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[6]>7:
                           return 'liver'
                        elif obj[6]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=64:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[4]>17:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>34:
                        return 'liver'
                     elif obj[5]<=34:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]<=17:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[1]>128.79616352900172:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 116, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 101, "metric_value": 0.0, "depth": 5}
               if obj[8]<=114.14567476352765:
                  # {"feature": "Total_Bilirubin", "instances": 92, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=27.782608695652176:
                     # {"feature": "Total_Protiens", "instances": 74, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=85.04048209101472:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 70, "metric_value": -0.0, "depth": 8}
                        if obj[5]>11:
                           return 'liver'
                        elif obj[5]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>85.04048209101472:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=15:
                           return 'liver'
                        elif obj[4]>15:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>27.782608695652176:
                     # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=779:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=406:
                           return 'liver'
                        elif obj[5]>406:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>779:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>114.14567476352765:
                  # {"feature": "Total_Protiens", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[6]>65:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=42:
                           return 'liver'
                        elif obj[4]>42:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>18:
                           return 'normal'
                        elif obj[4]<=18:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]<=65:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 5}
               if obj[1]<=6:
                  # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[4]>22:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[5]>21:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[8]>11:
                           return 'liver'
                        elif obj[8]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=21:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]<=22:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[1]>6:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[5]>21:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=35:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'liver'
                        elif obj[8]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>35:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=21:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]>24:
                        return 'normal'
                     elif obj[4]<=24:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[6]>69:
               # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": 0.0, "depth": 5}
               if obj[4]>26:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[8]>7:
                     # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        return 'liver'
                     elif obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'normal'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]<=7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[5]>42:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=42:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'normal'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[4]<=26:
                  # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>16:
                           return 'liver'
                        elif obj[5]<=16:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>21:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=21:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=69:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 17, "metric_value": -0.0, "depth": 5}
               if obj[8]<=9:
                  # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[4]>84:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=84:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>25:
                           return 'liver'
                        elif obj[5]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[8]>9:
                  # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[4]>25:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[5]>67:
                        return 'liver'
                     elif obj[5]<=67:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=25:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[6]>44.49473684210526:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 63, "metric_value": -0.0, "depth": 4}
            if obj[8]<=12:
               # {"feature": "Alkaline_Phosphotase", "instances": 54, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 38, "metric_value": 0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Total_Bilirubin", "instances": 37, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=12:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=44.31818181818182:
                           return 'normal'
                        elif obj[5]>44.31818181818182:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>12:
                        # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[2]>7:
                           return 'liver'
                        elif obj[2]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=12:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=102:
                     # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=48:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>48:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[1]>9:
                           return 'normal'
                        elif obj[1]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>102:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>12:
               # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[5]>18:
                  # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[4]>31:
                     # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'normal'
                        elif obj[1]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[3]>291.0539499036609:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=31:
                     # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'normal'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=18:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=7:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=44.49473684210526:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 32, "metric_value": 0.0, "depth": 4}
            if obj[8]<=3:
               # {"feature": "Total_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 5}
               if obj[1]<=9:
                  # {"feature": "Alkaline_Phosphotase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[5]>16:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=16:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=30:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>9:
                  # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[4]>15:
                     # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>22:
                           return 'normal'
                        elif obj[5]<=22:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[3]>291.0539499036609:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>48:
                           return 'liver'
                        elif obj[5]<=48:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=15:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>3:
               # {"feature": "Alkaline_Phosphotase", "instances": 15, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[4]>21:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[5]>28:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'normal'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=28:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=21:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=1:
                        return 'liver'
                     elif obj[2]>1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[1]>12:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=7:
                        return 'normal'
                     elif obj[2]>7:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=12:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
