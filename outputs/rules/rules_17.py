def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]>60.46052631578947:
            # {"feature": "Aspartate_Aminotransferase", "instances": 117, "metric_value": -0.0, "depth": 4}
            if obj[5]<=66.09401709401709:
               # {"feature": "Direct_Bilirubin", "instances": 87, "metric_value": -0.0, "depth": 5}
               if obj[2]<=3:
                  # {"feature": "Total_Bilirubin", "instances": 58, "metric_value": -0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Alkaline_Phosphotase", "instances": 32, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Alamine_Aminotransferase", "instances": 28, "metric_value": 0.0, "depth": 8}
                        if obj[4]>10:
                           return 'liver'
                        elif obj[4]<=10:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[3]>291.0539499036609:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 26, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=24:
                        # {"feature": "Alkaline_Phosphotase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        elif obj[3]>291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>24:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=11:
                           return 'liver'
                        elif obj[8]>11:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>3:
                  # {"feature": "Alkaline_Phosphotase", "instances": 29, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=16:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=15:
                           return 'liver'
                        elif obj[8]>15:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>16:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]>66.09401709401709:
               # {"feature": "Alkaline_Phosphotase", "instances": 30, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[1]>1:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 17, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=7:
                        return 'liver'
                     elif obj[8]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[2]>3:
                           return 'liver'
                        elif obj[2]<=3:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=60.46052631578947:
            # {"feature": "Alamine_Aminotransferase", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[4]>12:
               # {"feature": "Direct_Bilirubin", "instances": 34, "metric_value": 0.0, "depth": 5}
               if obj[2]<=3:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[5]>22:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[8]>11:
                        # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]<=11:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=22:
                     # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[2]>3:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=44:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=13:
                        # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>13:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>44:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=22:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=14:
                           return 'normal'
                        elif obj[8]>14:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>22:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[4]<=12:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[6]>47.559322033898304:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 79, "metric_value": -0.0, "depth": 4}
            if obj[8]<=8:
               # {"feature": "Alkaline_Phosphotase", "instances": 58, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 39, "metric_value": -0.0, "depth": 6}
                  if obj[4]>17.88741910849628:
                     # {"feature": "Total_Bilirubin", "instances": 34, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=162.23408019101092:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 30, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=61.733333333333334:
                           return 'liver'
                        elif obj[5]>61.733333333333334:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>162.23408019101092:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=17.88741910849628:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[5]>19:
                        return 'liver'
                     elif obj[5]<=19:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'liver'
                        elif obj[1]>9:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[1]>58:
                     # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[2]>32:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[5]>64:
                           return 'liver'
                        elif obj[5]<=64:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=32:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=58:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>8:
               # {"feature": "Alkaline_Phosphotase", "instances": 21, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": 0.0, "depth": 6}
                  if obj[1]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=30:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[5]>17:
                           return 'liver'
                        elif obj[5]<=17:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>30:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=16:
                           return 'normal'
                        elif obj[2]>16:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=1:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>16:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>3:
                           return 'normal'
                        elif obj[1]<=3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=16:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
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
         elif obj[6]<=47.559322033898304:
            # {"feature": "Direct_Bilirubin", "instances": 39, "metric_value": 0.0, "depth": 4}
            if obj[2]<=4:
               # {"feature": "Alamine_Aminotransferase", "instances": 20, "metric_value": -0.0, "depth": 5}
               if obj[4]>15:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=7:
                     # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>7:
                     # {"feature": "Alkaline_Phosphotase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=15:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[2]>4:
               # {"feature": "Alkaline_Phosphotase", "instances": 19, "metric_value": 0.0, "depth": 5}
               if obj[3]>291.0539499036609:
                  return 'liver'
               elif obj[3]<=291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[5]>25:
                     return 'liver'
                  elif obj[5]<=25:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>18:
                        return 'liver'
                     elif obj[1]<=18:
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
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 116, "metric_value": 0.0, "depth": 4}
            if obj[8]<=26.155172413793103:
               # {"feature": "Total_Bilirubin", "instances": 98, "metric_value": 0.0, "depth": 5}
               if obj[1]<=23.224489795918366:
                  # {"feature": "Total_Protiens", "instances": 81, "metric_value": 0.0, "depth": 6}
                  if obj[6]>60.98765432098765:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 61, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=43.967213114754095:
                        # {"feature": "Direct_Bilirubin", "instances": 46, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'normal'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>43.967213114754095:
                        # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=60.98765432098765:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 20, "metric_value": -0.0, "depth": 7}
                     if obj[5]>30:
                        # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=30:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]>23.224489795918366:
                  # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": 0.0, "depth": 6}
                  if obj[2]>7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=80:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=180:
                           return 'liver'
                        elif obj[5]>180:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>80:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>82:
                        return 'liver'
                     elif obj[4]<=82:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>26.155172413793103:
               # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[4]>34:
                  # {"feature": "Total_Protiens", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[6]<=69:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>45:
                           return 'liver'
                        elif obj[5]<=45:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]>69:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=34:
                  # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     return 'normal'
                  elif obj[2]>2:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>12:
                        return 'normal'
                     elif obj[1]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[8]>8:
               # {"feature": "Direct_Bilirubin", "instances": 20, "metric_value": -0.0, "depth": 5}
               if obj[2]<=16:
                  # {"feature": "Total_Protiens", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[6]>69:
                     # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1]>5:
                           return 'liver'
                        elif obj[1]<=5:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=25:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=69:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[5]>66:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[4]>84:
                           return 'liver'
                        elif obj[4]<=84:
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
                  else:
                     return 'liver'
               elif obj[2]>16:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=8:
               # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[1]>8:
                  # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[2]>2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=154:
                        # {"feature": "Total_Protiens", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[6]>62:
                           return 'normal'
                        elif obj[6]<=62:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>154:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        return 'normal'
                     elif obj[4]<=25:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[1]<=8:
                  # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
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
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 70, "metric_value": 0.0, "depth": 4}
            if obj[8]<=11:
               # {"feature": "Total_Protiens", "instances": 55, "metric_value": -0.0, "depth": 5}
               if obj[6]>41.03636363636364:
                  # {"feature": "Direct_Bilirubin", "instances": 36, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Total_Bilirubin", "instances": 28, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=12:
                        # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[4]>12:
                           return 'liver'
                        elif obj[4]<=12:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>12:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[5]>38:
                           return 'liver'
                        elif obj[5]<=38:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>20:
                           return 'normal'
                        elif obj[4]<=20:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>16:
                           return 'normal'
                        elif obj[4]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[6]<=41.03636363636364:
                  # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": -0.0, "depth": 7}
                     if obj[5]>21:
                        # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=21:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[4]>20:
                           return 'liver'
                        elif obj[4]<=20:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=7:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>11:
               # {"feature": "Total_Protiens", "instances": 15, "metric_value": 0.0, "depth": 5}
               if obj[6]<=71:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=30:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[4]>20:
                           return 'normal'
                        elif obj[4]<=20:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=6:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'liver'
                        elif obj[2]>1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>30:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]>71:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>43:
                           return 'normal'
                        elif obj[4]<=43:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
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
            # {"feature": "Total_Protiens", "instances": 25, "metric_value": 0.0, "depth": 4}
            if obj[6]<=75:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[8]>4:
                  # {"feature": "Alamine_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 6}
                  if obj[4]>28:
                     # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=23:
                        return 'liver'
                     elif obj[1]>23:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>57:
                           return 'liver'
                        elif obj[5]<=57:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=28:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[1]>12:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>7:
                           return 'normal'
                        elif obj[2]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=4:
                  # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[1]>15:
                     return 'liver'
                  elif obj[1]<=15:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=30:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>3:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[6]>75:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
