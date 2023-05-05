def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]>60.46052631578947:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 117, "metric_value": -0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Aspartate_Aminotransferase", "instances": 91, "metric_value": -0.0, "depth": 5}
               if obj[5]<=69.98901098901099:
                  # {"feature": "Alkaline_Phosphotase", "instances": 67, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Direct_Bilirubin", "instances": 53, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Total_Bilirubin", "instances": 39, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[4]>12:
                           return 'liver'
                        elif obj[4]<=12:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=226:
                        # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=39:
                           return 'liver'
                        elif obj[2]>39:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>226:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]>69.98901098901099:
                  # {"feature": "Direct_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 6}
                  if obj[2]>6:
                     return 'liver'
                  elif obj[2]<=6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[4]>28:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=15:
                           return 'liver'
                        elif obj[1]>15:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=28:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Aspartate_Aminotransferase", "instances": 26, "metric_value": 0.0, "depth": 5}
               if obj[5]>17:
                  # {"feature": "Alamine_Aminotransferase", "instances": 25, "metric_value": 0.0, "depth": 6}
                  if obj[4]>24:
                     return 'liver'
                  elif obj[4]<=24:
                     # {"feature": "Alkaline_Phosphotase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
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
               elif obj[5]<=17:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[6]<=60.46052631578947:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Alkaline_Phosphotase", "instances": 31, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 24, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=58:
                     # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[5]>22:
                           return 'liver'
                        elif obj[5]<=22:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[5]>32:
                           return 'liver'
                        elif obj[5]<=32:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>58:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[3]>291.0539499036609:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[4]>14:
                     return 'liver'
                  elif obj[4]<=14:
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
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 118, "metric_value": -0.0, "depth": 3}
         if obj[8]<=13.838983050847459:
            # {"feature": "Alkaline_Phosphotase", "instances": 100, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 71, "metric_value": 0.0, "depth": 5}
               if obj[1]>1:
                  # {"feature": "Total_Protiens", "instances": 67, "metric_value": -0.0, "depth": 6}
                  if obj[6]>47.53731343283582:
                     # {"feature": "Alamine_Aminotransferase", "instances": 45, "metric_value": 0.0, "depth": 7}
                     if obj[4]>10:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 44, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=77.3409090909091:
                           return 'liver'
                        elif obj[5]>77.3409090909091:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=10:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]<=47.53731343283582:
                     # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=33:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[5]>25:
                           return 'liver'
                        elif obj[5]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>33:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=53:
                           return 'liver'
                        elif obj[5]>53:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=1:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=3:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[5]>13:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=22:
                           return 'normal'
                        elif obj[4]>22:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=13:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 29, "metric_value": -0.0, "depth": 5}
               if obj[2]<=31.896551724137932:
                  return 'liver'
               elif obj[2]>31.896551724137932:
                  # {"feature": "Total_Protiens", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[6]<=65:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=77:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>73:
                           return 'liver'
                        elif obj[1]<=73:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>77:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]>65:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]>13.838983050847459:
            # {"feature": "Alkaline_Phosphotase", "instances": 18, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Protiens", "instances": 10, "metric_value": 0.0, "depth": 5}
               if obj[6]>5:
                  # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=5:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[1]>4:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[5]>28:
                           return 'liver'
                        elif obj[5]<=28:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=4:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>5:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=5:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=67:
                     return 'liver'
                  elif obj[5]>67:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>2:
                        return 'normal'
                     elif obj[1]<=2:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[2]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
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
         # {"feature": "Alkaline_Phosphotase", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Aspartate_Aminotransferase", "instances": 116, "metric_value": 0.0, "depth": 4}
            if obj[5]>11:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 115, "metric_value": 0.0, "depth": 5}
               if obj[8]<=68.61194456044235:
                  # {"feature": "Total_Protiens", "instances": 98, "metric_value": -0.0, "depth": 6}
                  if obj[6]>9.390313491571312:
                     # {"feature": "Direct_Bilirubin", "instances": 82, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=6:
                        # {"feature": "Total_Bilirubin", "instances": 63, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'normal'
                        elif obj[1]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>6:
                        # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=159:
                           return 'liver'
                        elif obj[1]>159:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=9.390313491571312:
                     # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=50:
                           return 'liver'
                        elif obj[4]>50:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
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
               elif obj[8]>68.61194456044235:
                  # {"feature": "Alamine_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=42:
                     # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>9:
                        # {"feature": "Total_Protiens", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[6]>69:
                           return 'liver'
                        elif obj[6]<=69:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>42:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Protiens", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[6]<=74:
                           return 'liver'
                        elif obj[6]>74:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
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
            # {"feature": "Total_Protiens", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[6]<=79:
               # {"feature": "Alamine_Aminotransferase", "instances": 34, "metric_value": -0.0, "depth": 5}
               if obj[4]<=133.7058823529412:
                  # {"feature": "Direct_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=4:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 20, "metric_value": -0.0, "depth": 7}
                     if obj[5]>40:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'liver'
                        elif obj[8]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=40:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'normal'
                        elif obj[1]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>4:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[8]>8:
                        return 'liver'
                     elif obj[8]<=8:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": -0.0, "depth": 8}
                        if obj[1]>23:
                           return 'liver'
                        elif obj[1]<=23:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>133.7058823529412:
                  # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=39:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[5]>108:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=8:
                           return 'liver'
                        elif obj[8]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=108:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>39:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]>79:
               # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[1]<=9:
                  # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[2]>2:
                     return 'normal'
                  elif obj[2]<=2:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>9:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[6]>19.418485261141242:
            # {"feature": "Alkaline_Phosphotase", "instances": 69, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 51, "metric_value": 0.0, "depth": 5}
               if obj[8]<=95:
                  # {"feature": "Alamine_Aminotransferase", "instances": 49, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=48.36734693877551:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 33, "metric_value": 0.0, "depth": 7}
                     if obj[5]>10:
                        # {"feature": "Total_Bilirubin", "instances": 32, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=19:
                           return 'liver'
                        elif obj[1]>19:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=10:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>48.36734693877551:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=108:
                        # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>108:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>95:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]>2:
                     return 'normal'
                  elif obj[1]<=2:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[4]>48:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[5]>57:
                     return 'liver'
                  elif obj[5]<=57:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>9:
                        return 'normal'
                     elif obj[1]<=9:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[4]<=48:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[5]>22:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[1]>2:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[2]>8:
                           return 'liver'
                        elif obj[2]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=2:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=22:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=19.418485261141242:
            # {"feature": "Aspartate_Aminotransferase", "instances": 26, "metric_value": 0.0, "depth": 4}
            if obj[5]<=34:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 14, "metric_value": 0.0, "depth": 5}
               if obj[8]<=5:
                  # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[1]>8:
                     # {"feature": "Alkaline_Phosphotase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>15:
                           return 'liver'
                        elif obj[4]<=15:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[3]>291.0539499036609:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=8:
                     # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
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
               elif obj[8]>5:
                  # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]>34:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 12, "metric_value": -0.0, "depth": 5}
               if obj[8]<=1:
                  # {"feature": "Alkaline_Phosphotase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[3]>291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>9:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 8}
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
                  elif obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        return 'liver'
                     elif obj[1]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>4:
                           return 'normal'
                        elif obj[2]<=4:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]>1:
                  # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        return 'liver'
                     elif obj[1]<=8:
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
