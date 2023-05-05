def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]>18.423649285366366:
            # {"feature": "Aspartate_Aminotransferase", "instances": 134, "metric_value": 0.0, "depth": 4}
            if obj[5]<=62.634328358208954:
               # {"feature": "Alkaline_Phosphotase", "instances": 99, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 83, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=43.06564954707283:
                     # {"feature": "Total_Bilirubin", "instances": 69, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 42, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'liver'
                        elif obj[8]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>43.06564954707283:
                     # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=6:
                        # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>6:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>3:
                           return 'normal'
                        elif obj[1]<=3:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=226:
                     # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=4:
                        # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=24:
                           return 'liver'
                        elif obj[4]>24:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>4:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>226:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]>62.634328358208954:
               # {"feature": "Alkaline_Phosphotase", "instances": 35, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": 0.0, "depth": 6}
                  if obj[1]>1:
                     # {"feature": "Direct_Bilirubin", "instances": 20, "metric_value": 0.0, "depth": 7}
                     if obj[2]>6:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=7:
                           return 'liver'
                        elif obj[8]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=6:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'liver'
                        elif obj[8]<=1:
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
         elif obj[6]<=18.423649285366366:
            # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 4}
            if obj[5]>25:
               # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 5}
               if obj[2]>2:
                  # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[4]>50:
                     return 'liver'
                  elif obj[4]<=50:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>2:
                        # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        elif obj[3]>291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=2:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=2:
                  # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=9:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>9:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[5]<=25:
               # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>2:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]<=12:
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
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[6]>47.123456790123456:
               # {"feature": "Alamine_Aminotransferase", "instances": 54, "metric_value": -0.0, "depth": 5}
               if obj[4]>10:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 53, "metric_value": -0.0, "depth": 6}
                  if obj[8]>6:
                     # {"feature": "Total_Bilirubin", "instances": 31, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=24.387096774193548:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 24, "metric_value": 0.0, "depth": 8}
                        if obj[5]>13:
                           return 'liver'
                        elif obj[5]<=13:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>24.387096774193548:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=6:
                     # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=10:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[6]<=47.123456790123456:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 27, "metric_value": -0.0, "depth": 5}
               if obj[8]<=8:
                  # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=48:
                           return 'liver'
                        elif obj[5]>48:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>21:
                           return 'normal'
                        elif obj[5]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[8]>8:
                  # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>18:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>42:
                           return 'normal'
                        elif obj[5]<=42:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=18:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>4:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>26:
                           return 'liver'
                        elif obj[4]<=26:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=4:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[8]<=55:
               # {"feature": "Direct_Bilirubin", "instances": 36, "metric_value": -0.0, "depth": 5}
               if obj[2]<=30.0:
                  # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": 0.0, "depth": 6}
                  if obj[1]>2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 7}
                     if obj[5]>38:
                        return 'liver'
                     elif obj[5]<=38:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=22:
                           return 'liver'
                        elif obj[4]>22:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=2:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>30.0:
                  # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=196:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[4]>48:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=384:
                           return 'liver'
                        elif obj[5]>384:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=48:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>196:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>55:
               return 'normal'
            else:
               return 'normal'
         else:
            return 'liver'
      else:
         return 'liver'
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Total_Protiens", "instances": 123, "metric_value": 0.0, "depth": 4}
            if obj[6]>62.28455284552845:
               # {"feature": "Alkaline_Phosphotase", "instances": 90, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 65, "metric_value": 0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Total_Bilirubin", "instances": 63, "metric_value": -0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 58, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=85.63793103448276:
                           return 'liver'
                        elif obj[5]>85.63793103448276:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        return 'normal'
                     else:
                        return 'normal'
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
               elif obj[3]>291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 25, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=188.68:
                     # {"feature": "Alamine_Aminotransferase", "instances": 17, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=57:
                        # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>57:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>188.68:
                     # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=16:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=152:
                           return 'liver'
                        elif obj[4]>152:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>16:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=62.28455284552845:
               # {"feature": "Total_Bilirubin", "instances": 33, "metric_value": -0.0, "depth": 5}
               if obj[1]>7:
                  # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": -0.0, "depth": 7}
                     if obj[5]>21:
                        # {"feature": "Alkaline_Phosphotase", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        elif obj[3]>291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=21:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]<=1:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[1]<=7:
                  # {"feature": "Alkaline_Phosphotase", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=9:
                           return 'liver'
                        elif obj[2]>9:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=25:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>25:
                           return 'liver'
                        elif obj[5]<=25:
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
         elif obj[8]<=1:
            # {"feature": "Total_Protiens", "instances": 31, "metric_value": 0.0, "depth": 4}
            if obj[6]<=81:
               # {"feature": "Alkaline_Phosphotase", "instances": 25, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 17, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=18:
                     # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=71:
                           return 'liver'
                        elif obj[5]>71:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>18:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=7:
                        return 'liver'
                     elif obj[2]>7:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=19:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=82:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>82:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>19:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[6]>81:
               # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 5}
               if obj[5]>23:
                  # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[4]>26:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=26:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[5]<=23:
                  # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        return 'normal'
                     elif obj[1]<=8:
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
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[6]>44.49473684210526:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 63, "metric_value": -0.0, "depth": 4}
            if obj[8]<=9:
               # {"feature": "Alkaline_Phosphotase", "instances": 47, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 33, "metric_value": 0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Total_Bilirubin", "instances": 32, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=12:
                        # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>12:
                        # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 8}
                        if obj[2]>23:
                           return 'liver'
                        elif obj[2]<=23:
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
                  # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 6}
                  if obj[4]>28:
                     # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=82:
                        # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>82:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=28:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>28:
                        return 'normal'
                     elif obj[1]<=28:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>9:
               # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 5}
               if obj[5]<=40:
                  # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[4]>11:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=11:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[5]>40:
                  # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>22:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=22:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
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
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[8]<=6:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=39:
                     # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[4]>26:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=26:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=13:
                           return 'liver'
                        elif obj[1]>13:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>39:
                     # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[4]>88:
                           return 'liver'
                        elif obj[4]<=88:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>6:
                  # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[1]>6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=21:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>21:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>21:
                           return 'liver'
                        elif obj[5]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=6:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=1:
                        return 'liver'
                     elif obj[2]>1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 5}
               if obj[5]<=39:
                  # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[1]>9:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[2]>3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=10:
                           return 'normal'
                        elif obj[4]>10:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=3:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=9:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[5]>39:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>9:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>4:
                           return 'liver'
                        elif obj[2]<=4:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=9:
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
   else:
      return 'liver'
