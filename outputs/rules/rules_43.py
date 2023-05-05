def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 117, "metric_value": 0.0, "depth": 4}
            if obj[6]<=81.23929846266847:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 110, "metric_value": 0.0, "depth": 5}
               if obj[8]<=24.1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 94, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=37.297872340425535:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 66, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=30.196969696969695:
                        # {"feature": "Direct_Bilirubin", "instances": 44, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>30.196969696969695:
                        # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=12:
                           return 'liver'
                        elif obj[1]>12:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>37.297872340425535:
                     # {"feature": "Total_Bilirubin", "instances": 28, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=58.62147853983738:
                        # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=15:
                           return 'liver'
                        elif obj[2]>15:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>58.62147853983738:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>24.1:
                  # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=13:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=30:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]>13:
                           return 'normal'
                        elif obj[5]<=13:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>30:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]>20:
                           return 'liver'
                        elif obj[5]<=20:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>13:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[5]>20:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>12:
                           return 'liver'
                        elif obj[4]<=12:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=20:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]>81.23929846266847:
               # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 5}
               if obj[4]>32:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=1:
                     return 'liver'
                  elif obj[8]>1:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[4]<=32:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=1:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'normal'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Bilirubin", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[1]<=204.5459987088306:
               # {"feature": "Total_Protiens", "instances": 31, "metric_value": -0.0, "depth": 5}
               if obj[6]<=71:
                  return 'liver'
               elif obj[6]>71:
                  # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=55:
                     # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[4]>29:
                        return 'liver'
                     elif obj[4]<=29:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=17:
                           return 'liver'
                        elif obj[5]>17:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]>55:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[1]>204.5459987088306:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[8]<=36.36541586292405:
            # {"feature": "Total_Protiens", "instances": 103, "metric_value": 0.0, "depth": 4}
            if obj[6]>48.728155339805824:
               # {"feature": "Alkaline_Phosphotase", "instances": 68, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 48, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=42.020833333333336:
                     # {"feature": "Total_Bilirubin", "instances": 35, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=13:
                        # {"feature": "Direct_Bilirubin", "instances": 20, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>13:
                        # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>42.020833333333336:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=152:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>152:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 20, "metric_value": -0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[5]>29:
                        # {"feature": "Total_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 8}
                        if obj[1]>58:
                           return 'liver'
                        elif obj[1]<=58:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=29:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=12:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=48.728155339805824:
               # {"feature": "Alamine_Aminotransferase", "instances": 35, "metric_value": 0.0, "depth": 5}
               if obj[4]>15:
                  # {"feature": "Direct_Bilirubin", "instances": 33, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=5:
                     # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Alkaline_Phosphotase", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>5:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=15:
                  # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
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
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[8]>36.36541586292405:
            # {"feature": "Total_Protiens", "instances": 15, "metric_value": 0.0, "depth": 4}
            if obj[6]<=52:
               # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[5]>28:
                  # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=11:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>21:
                        return 'liver'
                     elif obj[4]<=21:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>11:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=28:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[6]>52:
               # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": -0.0, "depth": 5}
               if obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 6}
                  if obj[1]>5:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=28:
                        return 'liver'
                     elif obj[5]>28:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=5:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=1:
                        return 'normal'
                     elif obj[2]>1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[3]<=291.0539499036609:
                  return 'liver'
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
         # {"feature": "Alkaline_Phosphotase", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 116, "metric_value": 0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Aspartate_Aminotransferase", "instances": 94, "metric_value": -0.0, "depth": 5}
               if obj[5]<=133.31914893617022:
                  # {"feature": "Total_Protiens", "instances": 76, "metric_value": -0.0, "depth": 6}
                  if obj[6]>18.623210885217063:
                     # {"feature": "Alamine_Aminotransferase", "instances": 67, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=79.3131975251878:
                        # {"feature": "Total_Bilirubin", "instances": 61, "metric_value": -0.0, "depth": 8}
                        if obj[1]>5:
                           return 'liver'
                        elif obj[1]<=5:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>79.3131975251878:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]<=18.623210885217063:
                     # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'liver'
                        elif obj[2]>1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'normal'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[5]>133.31914893617022:
                  # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[4]>86:
                     return 'liver'
                  elif obj[4]<=86:
                     # {"feature": "Total_Protiens", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[6]>56:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>11:
                           return 'liver'
                        elif obj[1]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=56:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 5}
               if obj[1]<=18:
                  # {"feature": "Total_Protiens", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[6]<=68:
                     # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=25:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]>68:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[5]>34:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'normal'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=34:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[1]>18:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[5]>19:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=7:
                        return 'liver'
                     elif obj[2]>7:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=19:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Alamine_Aminotransferase", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[4]<=308.3038098719911:
               # {"feature": "Total_Protiens", "instances": 34, "metric_value": -0.0, "depth": 5}
               if obj[6]>55:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 33, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=117.36363636363636:
                     # {"feature": "Direct_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[8]>7:
                           return 'liver'
                        elif obj[8]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>2:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'liver'
                        elif obj[8]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>117.36363636363636:
                     # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>3:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=55:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[4]>308.3038098719911:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[6]>44.49473684210526:
            # {"feature": "Alkaline_Phosphotase", "instances": 63, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 46, "metric_value": 0.0, "depth": 5}
               if obj[5]<=69.41304347826087:
                  # {"feature": "Direct_Bilirubin", "instances": 33, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 27, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=15:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'normal'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]>20:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'normal'
                        elif obj[1]>6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=20:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[5]>69.41304347826087:
                  # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[1]>2:
                     # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=89:
                        # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[4]>56:
                           return 'liver'
                        elif obj[4]<=56:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>89:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=2:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 5}
               if obj[5]>40:
                  # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[2]>15:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[4]>50:
                        return 'liver'
                     elif obj[4]<=50:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>25:
                           return 'normal'
                        elif obj[1]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=15:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]>28:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[8]>5:
                           return 'normal'
                        elif obj[8]<=5:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=28:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=40:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=44.49473684210526:
            # {"feature": "Alkaline_Phosphotase", "instances": 32, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[8]<=13:
                  # {"feature": "Direct_Bilirubin", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[4]>12:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[5]>20:
                           return 'liver'
                        elif obj[5]<=20:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=88:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=20:
                           return 'liver'
                        elif obj[5]>20:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>88:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>13:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[8]<=5:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[1]>9:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]>4:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>10:
                           return 'liver'
                        elif obj[4]<=10:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=4:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=9:
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
               elif obj[8]>5:
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
