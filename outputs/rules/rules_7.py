def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Albumin", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[7]>26.393063583815028:
      # {"feature": "Age", "instances": 306, "metric_value": 0.0, "depth": 2}
      if obj[0]<=59.11851760467796:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 247, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Total_Protiens", "instances": 193, "metric_value": 0.0, "depth": 4}
            if obj[6]>60.461139896373055:
               # {"feature": "Alkaline_Phosphotase", "instances": 146, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 107, "metric_value": 0.0, "depth": 6}
                  if obj[5]>11:
                     # {"feature": "Total_Bilirubin", "instances": 105, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=103.80038583549518:
                        # {"feature": "Direct_Bilirubin", "instances": 101, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=6:
                           return 'liver'
                        elif obj[2]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>103.80038583549518:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=11:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 39, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=38.35897435897436:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 32, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=116.40625:
                        # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 8}
                        if obj[4]>25:
                           return 'liver'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>116.40625:
                        # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>38.35897435897436:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=60.461139896373055:
               # {"feature": "Alkaline_Phosphotase", "instances": 47, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 40, "metric_value": 0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Total_Bilirubin", "instances": 39, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Direct_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>9:
                        # {"feature": "Direct_Bilirubin", "instances": 16, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=8:
                           return 'liver'
                        elif obj[2]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=12:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[1]>9:
                     return 'liver'
                  elif obj[1]<=9:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Alkaline_Phosphotase", "instances": 54, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 42, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Total_Protiens", "instances": 37, "metric_value": 0.0, "depth": 6}
                  if obj[6]>57:
                     # {"feature": "Alamine_Aminotransferase", "instances": 31, "metric_value": -0.0, "depth": 7}
                     if obj[4]>11:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 30, "metric_value": -0.0, "depth": 8}
                        if obj[5]>17:
                           return 'liver'
                        elif obj[5]<=17:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=11:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]<=57:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        return 'liver'
                     elif obj[1]<=6:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 6}
                  if obj[4]>18:
                     return 'liver'
                  elif obj[4]<=18:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
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
            elif obj[3]>291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=19:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=108:
                        # {"feature": "Total_Protiens", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[6]<=68:
                           return 'liver'
                        elif obj[6]>68:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>108:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>19:
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
      elif obj[0]>59.11851760467796:
         # {"feature": "Alkaline_Phosphotase", "instances": 59, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Alamine_Aminotransferase", "instances": 44, "metric_value": 0.0, "depth": 4}
            if obj[4]<=47.25:
               # {"feature": "Aspartate_Aminotransferase", "instances": 33, "metric_value": 0.0, "depth": 5}
               if obj[5]>14:
                  # {"feature": "Total_Protiens", "instances": 32, "metric_value": 0.0, "depth": 6}
                  if obj[6]<=68:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=139:
                        # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'liver'
                        elif obj[1]>9:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>139:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]>68:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[8]>7:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'normal'
                        elif obj[1]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=7:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
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
               elif obj[5]<=14:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[4]>47.25:
               # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 5}
               if obj[2]<=19:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[8]>12:
                     # {"feature": "Total_Protiens", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[6]<=66:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>66:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]<=12:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]>40:
                           return 'liver'
                        elif obj[5]<=40:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=8:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>19:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 15, "metric_value": 0.0, "depth": 4}
            if obj[6]<=69:
               return 'liver'
            elif obj[6]>69:
               # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 5}
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
      else:
         return 'liver'
   elif obj[7]<=26.393063583815028:
      # {"feature": "Alkaline_Phosphotase", "instances": 213, "metric_value": 0.0, "depth": 2}
      if obj[3]<=291.0539499036609:
         # {"feature": "Total_Protiens", "instances": 151, "metric_value": 0.0, "depth": 3}
         if obj[6]>21.50804221771271:
            # {"feature": "Age", "instances": 115, "metric_value": 0.0, "depth": 4}
            if obj[0]>29.40811534763015:
               # {"feature": "Total_Bilirubin", "instances": 93, "metric_value": 0.0, "depth": 5}
               if obj[1]<=35.73118279569893:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 75, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=53.626666666666665:
                     # {"feature": "Alamine_Aminotransferase", "instances": 56, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=27.196428571428573:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 35, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=12:
                           return 'liver'
                        elif obj[8]>12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>27.196428571428573:
                        # {"feature": "Direct_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=5:
                           return 'normal'
                        elif obj[2]>5:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[5]>53.626666666666665:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": 0.0, "depth": 7}
                     if obj[8]>5:
                        # {"feature": "Direct_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=5:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>35.73118279569893:
                  # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[2]>2:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 17, "metric_value": 0.0, "depth": 7}
                     if obj[8]>1:
                        return 'liver'
                     elif obj[8]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]<=2:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[0]<=29.40811534763015:
               # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 5}
               if obj[1]<=8:
                  # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[8]>8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>11:
                           return 'normal'
                        elif obj[4]<=11:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]<=8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        return 'normal'
                     elif obj[4]<=15:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[1]>8:
                  # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[4]>37:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[5]>46:
                        return 'liver'
                     elif obj[5]<=46:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]<=37:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=5:
                        return 'normal'
                     elif obj[2]>5:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'normal'
         elif obj[6]<=21.50804221771271:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 36, "metric_value": -0.0, "depth": 4}
            if obj[8]<=75:
               # {"feature": "Alamine_Aminotransferase", "instances": 35, "metric_value": -0.0, "depth": 5}
               if obj[4]<=62.31428571428572:
                  # {"feature": "Age", "instances": 28, "metric_value": 0.0, "depth": 6}
                  if obj[0]>26:
                     # {"feature": "Total_Bilirubin", "instances": 26, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[5]>20:
                           return 'liver'
                        elif obj[5]<=20:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[0]<=26:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>62.31428571428572:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[5]>74:
                     return 'liver'
                  elif obj[5]<=74:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>75:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[3]>291.0539499036609:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 62, "metric_value": -0.0, "depth": 3}
         if obj[8]<=7:
            # {"feature": "Age", "instances": 42, "metric_value": -0.0, "depth": 4}
            if obj[0]>47.523809523809526:
               # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": 0.0, "depth": 5}
               if obj[1]>7:
                  # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=167.9090909090909:
                     # {"feature": "Direct_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=23:
                        return 'liver'
                     elif obj[2]>23:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=64:
                           return 'liver'
                        elif obj[5]>64:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>167.9090909090909:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=7:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[0]<=47.523809523809526:
               # {"feature": "Total_Protiens", "instances": 19, "metric_value": -0.0, "depth": 5}
               if obj[6]>8:
                  # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[4]>50:
                     return 'liver'
                  elif obj[4]<=50:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[1]>17:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[2]>6:
                           return 'liver'
                        elif obj[2]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=17:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=8:
                  # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[2]>3:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>13:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>48:
                           return 'liver'
                        elif obj[5]<=48:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=13:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]<=3:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=34:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>9:
                           return 'liver'
                        elif obj[1]<=9:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>34:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]>7:
            # {"feature": "Aspartate_Aminotransferase", "instances": 20, "metric_value": 0.0, "depth": 4}
            if obj[5]>57:
               # {"feature": "Age", "instances": 11, "metric_value": -0.0, "depth": 5}
               if obj[0]<=47:
                  return 'liver'
               elif obj[0]>47:
                  # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[2]>3:
                     return 'liver'
                  elif obj[2]<=3:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[5]<=57:
               # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[1]<=21:
                  # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     return 'liver'
                  elif obj[2]<=1:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[1]>21:
                  # {"feature": "Age", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[0]<=38:
                     return 'normal'
                  elif obj[0]>38:
                     return 'liver'
                  else:
                     return 'liver'
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
