def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]>60.46052631578947:
            # {"feature": "Alkaline_Phosphotase", "instances": 117, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 89, "metric_value": 0.0, "depth": 5}
               if obj[8]<=116:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 86, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=57.80232558139535:
                     # {"feature": "Alamine_Aminotransferase", "instances": 63, "metric_value": 0.0, "depth": 7}
                     if obj[4]>10:
                        # {"feature": "Total_Bilirubin", "instances": 62, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=23:
                           return 'liver'
                        elif obj[1]>23:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=10:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]>57.80232558139535:
                     # {"feature": "Alamine_Aminotransferase", "instances": 23, "metric_value": 0.0, "depth": 7}
                     if obj[4]>18:
                        # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=57:
                           return 'liver'
                        elif obj[1]>57:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=18:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]>116:
                  # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[4]>12:
                     return 'liver'
                  elif obj[4]<=12:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 28, "metric_value": -0.0, "depth": 5}
               if obj[1]>6:
                  # {"feature": "Alamine_Aminotransferase", "instances": 27, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=79.18518518518519:
                     # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=8:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'liver'
                        elif obj[8]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>79.18518518518519:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=6:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=60.46052631578947:
            # {"feature": "Alamine_Aminotransferase", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[4]>12:
               # {"feature": "Alkaline_Phosphotase", "instances": 34, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": 0.0, "depth": 7}
                     if obj[5]>20:
                        # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[1]>6:
                           return 'normal'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=20:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=37:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>37:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=12:
                           return 'liver'
                        elif obj[8]>12:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
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
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[8]>6:
               # {"feature": "Total_Protiens", "instances": 46, "metric_value": -0.0, "depth": 5}
               if obj[6]>25.374021442989452:
                  # {"feature": "Alamine_Aminotransferase", "instances": 37, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=45.32432432432432:
                     # {"feature": "Total_Bilirubin", "instances": 28, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Direct_Bilirubin", "instances": 26, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=16:
                           return 'liver'
                        elif obj[2]>16:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>45.32432432432432:
                     # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[2]>6:
                        return 'liver'
                     elif obj[2]<=6:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]<=25.374021442989452:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[5]>23:
                     return 'liver'
                  elif obj[5]<=23:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]<=6:
               # {"feature": "Alamine_Aminotransferase", "instances": 35, "metric_value": 0.0, "depth": 5}
               if obj[4]>10:
                  # {"feature": "Total_Bilirubin", "instances": 34, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=81.89000794277435:
                     # {"feature": "Total_Protiens", "instances": 31, "metric_value": -0.0, "depth": 7}
                     if obj[6]>43.935483870967744:
                        # {"feature": "Direct_Bilirubin", "instances": 21, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=43.935483870967744:
                        # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=13:
                           return 'liver'
                        elif obj[2]>13:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>81.89000794277435:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=10:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[8]<=53:
               # {"feature": "Direct_Bilirubin", "instances": 35, "metric_value": -0.0, "depth": 5}
               if obj[2]<=30.82857142857143:
                  # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 6}
                  if obj[1]>8:
                     return 'liver'
                  elif obj[1]<=8:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>20:
                        return 'liver'
                     elif obj[4]<=20:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]>30.82857142857143:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 6}
                  if obj[5]>57:
                     # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[1]>141:
                        return 'liver'
                     elif obj[1]<=141:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>88:
                           return 'liver'
                        elif obj[4]<=88:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=57:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>53:
               # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 5}
               if obj[1]>22:
                  return 'normal'
               elif obj[1]<=22:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'normal'
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
               if obj[8]<=26.286956521739132:
                  # {"feature": "Total_Protiens", "instances": 97, "metric_value": -0.0, "depth": 6}
                  if obj[6]>59.18556701030928:
                     # {"feature": "Direct_Bilirubin", "instances": 68, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 39, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=35.69230769230769:
                           return 'normal'
                        elif obj[4]>35.69230769230769:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 29, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=83.96551724137932:
                           return 'liver'
                        elif obj[4]>83.96551724137932:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=59.18556701030928:
                     # {"feature": "Alamine_Aminotransferase", "instances": 29, "metric_value": 0.0, "depth": 7}
                     if obj[4]>14:
                        # {"feature": "Total_Bilirubin", "instances": 28, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=14:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]>26.286956521739132:
                  # {"feature": "Total_Protiens", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[6]>62:
                     # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=62:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'normal'
                        else:
                           return 'normal'
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
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[8]<=13:
               # {"feature": "Total_Protiens", "instances": 33, "metric_value": 0.0, "depth": 5}
               if obj[6]>67:
                  # {"feature": "Direct_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[2]>2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[4]>29:
                        return 'liver'
                     elif obj[4]<=29:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>9:
                           return 'liver'
                        elif obj[1]<=9:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]<=2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=51:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'normal'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>51:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=67:
                  # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[4]>15:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[5]>67:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=67:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]<=15:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>13:
               # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 5}
               if obj[5]>23:
                  # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     return 'liver'
                  elif obj[1]<=7:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[5]<=23:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": -0.0, "depth": 3}
         if obj[6]>19.418485261141242:
            # {"feature": "Alkaline_Phosphotase", "instances": 69, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 51, "metric_value": 0.0, "depth": 5}
               if obj[8]<=95:
                  # {"feature": "Alamine_Aminotransferase", "instances": 49, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=48.36734693877551:
                     # {"feature": "Direct_Bilirubin", "instances": 33, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=4:
                        # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>4:
                        # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=127:
                           return 'liver'
                        elif obj[1]>127:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>48.36734693877551:
                     # {"feature": "Direct_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>41:
                           return 'liver'
                        elif obj[5]<=41:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
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
               # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 5}
               if obj[1]>25:
                  # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[2]>15:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        return 'liver'
                     elif obj[4]<=25:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]<=15:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[4]>48:
                        return 'normal'
                     elif obj[4]<=48:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[1]<=25:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=19.418485261141242:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 26, "metric_value": 0.0, "depth": 4}
            if obj[8]<=1:
               # {"feature": "Alkaline_Phosphotase", "instances": 16, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[4]>20:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=28:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>28:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=20:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        return 'liver'
                     elif obj[1]>9:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=15:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>30:
                           return 'normal'
                        elif obj[4]<=30:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=2:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>15:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>1:
               # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 5}
               if obj[5]<=25:
                  # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=21:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>21:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>12:
                        return 'normal'
                     elif obj[1]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[5]>25:
                  # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        return 'normal'
                     elif obj[1]>8:
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
