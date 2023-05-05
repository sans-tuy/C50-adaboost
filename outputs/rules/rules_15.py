def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]<=81.47896483100102:
            # {"feature": "Alamine_Aminotransferase", "instances": 144, "metric_value": -0.0, "depth": 4}
            if obj[4]<=50.65972222222222:
               # {"feature": "Aspartate_Aminotransferase", "instances": 101, "metric_value": -0.0, "depth": 5}
               if obj[5]<=32.722772277227726:
                  # {"feature": "Direct_Bilirubin", "instances": 64, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Total_Bilirubin", "instances": 43, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 36, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'liver'
                        elif obj[8]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>8:
                        # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 21, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=14:
                        # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>14:
                        # {"feature": "Alkaline_Phosphotase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[5]>32.722772277227726:
                  # {"feature": "Total_Bilirubin", "instances": 37, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=12:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 25, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=11:
                        # {"feature": "Alkaline_Phosphotase", "instances": 17, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        elif obj[3]>291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>11:
                        # {"feature": "Alkaline_Phosphotase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>12:
                     # {"feature": "Alkaline_Phosphotase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[3]>291.0539499036609:
                        return 'liver'
                     elif obj[3]<=291.0539499036609:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[4]>50.65972222222222:
               # {"feature": "Alkaline_Phosphotase", "instances": 43, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 23, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=116:
                     # {"feature": "Direct_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=58:
                           return 'liver'
                        elif obj[1]>58:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=2:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>116:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[3]>291.0539499036609:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]>81.47896483100102:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 4}
            if obj[8]<=1:
               # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[4]>22:
                     return 'liver'
                  elif obj[4]<=22:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'normal'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>1:
               # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     return 'normal'
                  elif obj[1]<=7:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            else:
               return 'normal'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": -0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Bilirubin", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[1]>1:
               # {"feature": "Total_Protiens", "instances": 77, "metric_value": 0.0, "depth": 5}
               if obj[6]>46.42857142857143:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 50, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 31, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=64.07040720479426:
                        # {"feature": "Direct_Bilirubin", "instances": 29, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=15:
                           return 'liver'
                        elif obj[2]>15:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>64.07040720479426:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 19, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=17:
                           return 'liver'
                        elif obj[2]>17:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=46.42857142857143:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 27, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=52:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 25, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=48:
                        # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=41:
                           return 'liver'
                        elif obj[4]>41:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>48:
                        # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>52:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[1]<=1:
               # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[2]<=3:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[5]>13:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[8]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=22:
                           return 'normal'
                        elif obj[4]>22:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=13:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'normal'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 37, "metric_value": -0.0, "depth": 4}
            if obj[6]>48.513513513513516:
               # {"feature": "Direct_Bilirubin", "instances": 25, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[1]>14:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[5]>57:
                        # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[4]>102:
                           return 'liver'
                        elif obj[4]<=102:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=57:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=14:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[1]>5:
                     return 'liver'
                  elif obj[1]<=5:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[6]<=48.513513513513516:
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
                  # {"feature": "Alamine_Aminotransferase", "instances": 93, "metric_value": -0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Total_Protiens", "instances": 91, "metric_value": -0.0, "depth": 7}
                     if obj[6]>11.472876090699039:
                        # {"feature": "Total_Bilirubin", "instances": 77, "metric_value": -0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=11.472876090699039:
                        # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=12:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        return 'liver'
                     elif obj[1]<=8:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[5]<=11:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 29, "metric_value": -0.0, "depth": 5}
               if obj[4]>26:
                  # {"feature": "Total_Protiens", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[6]>66:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": -0.0, "depth": 7}
                     if obj[5]>34:
                        # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=23:
                           return 'liver'
                        elif obj[1]>23:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=34:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=66:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=16:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=139:
                           return 'liver'
                        elif obj[5]>139:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>16:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=26:
                  # {"feature": "Total_Protiens", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[6]<=75:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        return 'liver'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]>75:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Total_Protiens", "instances": 31, "metric_value": -0.0, "depth": 4}
            if obj[6]<=79:
               # {"feature": "Total_Bilirubin", "instances": 24, "metric_value": -0.0, "depth": 5}
               if obj[1]>6:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=50:
                     # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=31:
                        # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>31:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>50:
                     # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>29:
                           return 'liver'
                        elif obj[4]<=29:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[3]>291.0539499036609:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=6:
                  # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>71:
                           return 'liver'
                        elif obj[5]<=71:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]<=1:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]>291.0539499036609:
                        return 'normal'
                     elif obj[3]<=291.0539499036609:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[6]>79:
               # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=30:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'normal'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>30:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[2]>2:
                  # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[3]>291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        return 'normal'
                     elif obj[1]>9:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]<=291.0539499036609:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'normal'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[6]>19.418485261141242:
            # {"feature": "Direct_Bilirubin", "instances": 69, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Alkaline_Phosphotase", "instances": 59, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 41, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=44.707317073170735:
                     # {"feature": "Total_Bilirubin", "instances": 28, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=61:
                           return 'liver'
                        elif obj[5]>61:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=8:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[8]>8:
                           return 'normal'
                        elif obj[8]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[4]>44.707317073170735:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=8:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=263:
                           return 'liver'
                        elif obj[1]>263:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>8:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=26:
                           return 'liver'
                        elif obj[1]>26:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[8]>5:
                     # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=41:
                           return 'liver'
                        elif obj[4]>41:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=5:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Alkaline_Phosphotase", "instances": 10, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[8]>7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]>17:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>15:
                           return 'liver'
                        elif obj[4]<=15:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=17:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=7:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=6:
                        return 'normal'
                     elif obj[1]>6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=19.418485261141242:
            # {"feature": "Aspartate_Aminotransferase", "instances": 26, "metric_value": 0.0, "depth": 4}
            if obj[5]<=34:
               # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 5}
               if obj[1]>8:
                  # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>15:
                           return 'liver'
                        elif obj[4]<=15:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=5:
                        return 'normal'
                     elif obj[8]>5:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[1]<=8:
                  # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[8]>1:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]>34:
               # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 5}
               if obj[4]>29:
                  # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=4:
                     # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        return 'liver'
                     elif obj[3]>291.0539499036609:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>4:
                     # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[3]>291.0539499036609:
                        return 'liver'
                     elif obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=14:
                           return 'liver'
                        elif obj[1]>14:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=29:
                  # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
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
