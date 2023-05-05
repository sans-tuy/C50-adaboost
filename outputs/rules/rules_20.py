def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Total_Protiens", "instances": 122, "metric_value": 0.0, "depth": 4}
            if obj[6]>13.321873032129226:
               # {"feature": "Direct_Bilirubin", "instances": 104, "metric_value": -0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 93, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=68.47311827956989:
                     # {"feature": "Alkaline_Phosphotase", "instances": 69, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Alamine_Aminotransferase", "instances": 54, "metric_value": 0.0, "depth": 8}
                        if obj[4]>12.56871321401331:
                           return 'liver'
                        elif obj[4]<=12.56871321401331:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[3]>291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>68.47311827956989:
                     # {"feature": "Alkaline_Phosphotase", "instances": 24, "metric_value": -0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=57:
                           return 'liver'
                        elif obj[1]>57:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[3]>291.0539499036609:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[1]>6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]>16:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>22:
                           return 'liver'
                        elif obj[5]<=22:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=16:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>20:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>27:
                           return 'liver'
                        elif obj[5]<=27:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=20:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=13.321873032129226:
               # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[2]>2:
                  # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[1]>11:
                     # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[3]>291.0539499036609:
                        return 'liver'
                     elif obj[3]<=291.0539499036609:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>30:
                           return 'liver'
                        elif obj[4]<=30:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]<=11:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>30:
                        # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        elif obj[3]>291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=30:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=2:
                  # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[4]>12:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]>32:
                           return 'normal'
                        elif obj[5]<=32:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Direct_Bilirubin", "instances": 30, "metric_value": -0.0, "depth": 4}
            if obj[2]<=5:
               # {"feature": "Total_Protiens", "instances": 22, "metric_value": -0.0, "depth": 5}
               if obj[6]>64:
                  # {"feature": "Alkaline_Phosphotase", "instances": 13, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[5]>20:
                        # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=20:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[1]>1:
                           return 'normal'
                        elif obj[1]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=64:
                  # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[4]>14:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>27:
                           return 'liver'
                        elif obj[5]<=27:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=14:
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
      elif obj[7]<=26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 118, "metric_value": -0.0, "depth": 3}
         if obj[8]<=13.838983050847459:
            # {"feature": "Direct_Bilirubin", "instances": 100, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Alkaline_Phosphotase", "instances": 87, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Protiens", "instances": 60, "metric_value": -0.0, "depth": 6}
                  if obj[6]>51.36666666666667:
                     # {"feature": "Alamine_Aminotransferase", "instances": 37, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=45.513513513513516:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 28, "metric_value": 0.0, "depth": 8}
                        if obj[5]>13:
                           return 'liver'
                        elif obj[5]<=13:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>45.513513513513516:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=330:
                           return 'liver'
                        elif obj[5]>330:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=51.36666666666667:
                     # {"feature": "Alamine_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[4]>30:
                        # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[1]>18:
                           return 'liver'
                        elif obj[1]<=18:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=30:
                        # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=22:
                           return 'liver'
                        elif obj[1]>22:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 27, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=75.92592592592592:
                     # {"feature": "Alamine_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 7}
                     if obj[4]>22:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[5]>50:
                           return 'liver'
                        elif obj[5]<=50:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=22:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>75.92592592592592:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 5}
               if obj[5]>35:
                  # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[4]>24:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=6:
                        # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>6:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=24:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=6:
                        # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[5]<=35:
                  # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Protiens", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[6]>7:
                        return 'liver'
                     elif obj[6]<=7:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]>13.838983050847459:
            # {"feature": "Alkaline_Phosphotase", "instances": 18, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 5}
               if obj[5]>28:
                  # {"feature": "Total_Protiens", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[6]<=43:
                     return 'liver'
                  elif obj[6]>43:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>21:
                        return 'liver'
                     elif obj[4]<=21:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[5]<=28:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     return 'liver'
                  elif obj[1]<=7:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[5]>34:
                  # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[2]>3:
                     return 'liver'
                  elif obj[2]<=3:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[5]<=34:
                  # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[1]>5:
                     return 'liver'
                  elif obj[1]<=5:
                     return 'normal'
                  else:
                     return 'normal'
               else:
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
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Alkaline_Phosphotase", "instances": 123, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 94, "metric_value": 0.0, "depth": 5}
               if obj[5]>11:
                  # {"feature": "Total_Protiens", "instances": 93, "metric_value": -0.0, "depth": 6}
                  if obj[6]>59.526881720430104:
                     # {"feature": "Total_Bilirubin", "instances": 68, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=24.352941176470587:
                        # {"feature": "Direct_Bilirubin", "instances": 57, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>24.352941176470587:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=59.526881720430104:
                     # {"feature": "Total_Bilirubin", "instances": 25, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=59:
                        # {"feature": "Alamine_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=50:
                           return 'liver'
                        elif obj[4]>50:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>59:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=11:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Protiens", "instances": 29, "metric_value": -0.0, "depth": 5}
               if obj[6]>69:
                  # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=23:
                     # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=57:
                           return 'liver'
                        elif obj[4]>57:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'normal'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>23:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=69:
                  # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[5]>66:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'normal'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=66:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[4]>102:
                        return 'liver'
                     elif obj[4]<=102:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=16:
                           return 'liver'
                        elif obj[1]>16:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Alkaline_Phosphotase", "instances": 31, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[4]>15:
                     # {"feature": "Total_Protiens", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=71:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>71:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[5]>24:
                           return 'liver'
                        elif obj[5]<=24:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=15:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[2]>2:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[5]>19:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=18:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>41:
                           return 'liver'
                        elif obj[4]<=41:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>18:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>11:
                           return 'liver'
                        elif obj[4]<=11:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]<=19:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]>62:
                           return 'normal'
                        elif obj[6]<=62:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>9:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[6]>44.49473684210526:
            # {"feature": "Alkaline_Phosphotase", "instances": 63, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 46, "metric_value": 0.0, "depth": 5}
               if obj[8]<=64:
                  # {"feature": "Alamine_Aminotransferase", "instances": 42, "metric_value": -0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Total_Bilirubin", "instances": 41, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 20, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=87:
                           return 'liver'
                        elif obj[5]>87:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=12:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[8]>64:
                  # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[4]>11:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>2:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=2:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=11:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": 0.0, "depth": 5}
               if obj[2]<=15:
                  # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=21:
                     return 'liver'
                  elif obj[1]>21:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[4]>48:
                        return 'normal'
                     elif obj[4]<=48:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[2]>15:
                  # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=68:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=25:
                           return 'normal'
                        elif obj[4]>25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>6:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>68:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=44.49473684210526:
            # {"feature": "Alkaline_Phosphotase", "instances": 32, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[4]>26:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'normal'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=26:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>16:
                           return 'liver'
                        elif obj[5]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>6:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>12:
                           return 'normal'
                        elif obj[4]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=15:
                           return 'liver'
                        elif obj[4]>15:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>2:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[5]>20:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[1]>11:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=1:
                           return 'liver'
                        elif obj[8]>1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=11:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=20:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        return 'liver'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[1]>9:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=5:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=60:
                        return 'normal'
                     elif obj[4]>60:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>5:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=9:
                  # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=30:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=1:
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
