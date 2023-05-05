def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": -0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]<=81.47896483100102:
            # {"feature": "Alamine_Aminotransferase", "instances": 144, "metric_value": 0.0, "depth": 4}
            if obj[4]<=50.65972222222222:
               # {"feature": "Aspartate_Aminotransferase", "instances": 101, "metric_value": -0.0, "depth": 5}
               if obj[5]<=32.722772277227726:
                  # {"feature": "Total_Bilirubin", "instances": 64, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Direct_Bilirubin", "instances": 39, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alkaline_Phosphotase", "instances": 29, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[8]>9:
                           return 'normal'
                        elif obj[8]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>8:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 25, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=14:
                        # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>14:
                        # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[5]>32.722772277227726:
                  # {"feature": "Alkaline_Phosphotase", "instances": 37, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 28, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=15:
                        # {"feature": "Direct_Bilirubin", "instances": 26, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=4:
                           return 'liver'
                        elif obj[2]>4:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>15:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'normal'
                        elif obj[1]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=36:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>36:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[4]>50.65972222222222:
               # {"feature": "Alkaline_Phosphotase", "instances": 43, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 23, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=137.56521739130434:
                     # {"feature": "Total_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=14:
                           return 'liver'
                        elif obj[8]>14:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>137.56521739130434:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]>81.47896483100102:
            # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 4}
            if obj[4]<=32:
               # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=17:
                        # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[3]>291.0539499036609:
                           return 'liver'
                        elif obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>7:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]>18:
                           return 'normal'
                        elif obj[5]<=18:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[4]>32:
               # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=1:
                     return 'liver'
                  elif obj[8]>1:
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
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[8]<=13.838983050847459:
            # {"feature": "Alkaline_Phosphotase", "instances": 100, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Protiens", "instances": 71, "metric_value": -0.0, "depth": 5}
               if obj[6]>48.267605633802816:
                  # {"feature": "Alamine_Aminotransferase", "instances": 47, "metric_value": 0.0, "depth": 6}
                  if obj[4]>10:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 46, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=75.65217391304348:
                        # {"feature": "Direct_Bilirubin", "instances": 33, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=21:
                           return 'liver'
                        elif obj[2]>21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>75.65217391304348:
                        # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=184:
                           return 'liver'
                        elif obj[1]>184:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=10:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[6]<=48.267605633802816:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 24, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=33:
                     # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=32:
                        # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>32:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]>33:
                     # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[4]>30:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=21:
                           return 'liver'
                        elif obj[1]>21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=30:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 29, "metric_value": -0.0, "depth": 5}
               if obj[1]<=207.5827007977774:
                  # {"feature": "Total_Protiens", "instances": 28, "metric_value": -0.0, "depth": 6}
                  if obj[6]>48.42857142857143:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": -0.0, "depth": 7}
                     if obj[5]>38:
                        # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[4]>48:
                           return 'liver'
                        elif obj[4]<=48:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=38:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=48.42857142857143:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>207.5827007977774:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]>13.838983050847459:
            # {"feature": "Alkaline_Phosphotase", "instances": 18, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 5}
               if obj[4]>21:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[5]>28:
                     return 'liver'
                  elif obj[5]<=28:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[4]<=21:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[2]>5:
                     return 'liver'
                  elif obj[2]<=5:
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
               # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[4]>16:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]>3:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>25:
                           return 'liver'
                        elif obj[5]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=3:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=16:
                     return 'liver'
                  else:
                     return 'liver'
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
         # {"feature": "Total_Protiens", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[6]>63.0:
            # {"feature": "Alkaline_Phosphotase", "instances": 110, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 78, "metric_value": 0.0, "depth": 5}
               if obj[1]<=114.30517754869389:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 75, "metric_value": -0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 60, "metric_value": -0.0, "depth": 7}
                     if obj[5]>11:
                        # {"feature": "Alamine_Aminotransferase", "instances": 59, "metric_value": -0.0, "depth": 8}
                        if obj[4]>12:
                           return 'liver'
                        elif obj[4]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=11:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=1:
                     # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[4]>27:
                           return 'liver'
                        elif obj[4]<=27:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>2:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[1]>114.30517754869389:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 32, "metric_value": 0.0, "depth": 5}
               if obj[1]>8:
                  # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=7:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=16:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[5]>21:
                           return 'liver'
                        elif obj[5]<=21:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>16:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>7:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[8]>7:
                        return 'liver'
                     elif obj[8]<=7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>28:
                           return 'liver'
                        elif obj[4]<=28:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=8:
                  # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[4]>28:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=28:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]<=1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[4]>26:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[8]>1:
                           return 'normal'
                        elif obj[8]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=26:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]>29:
                           return 'liver'
                        elif obj[5]<=29:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=63.0:
            # {"feature": "Total_Bilirubin", "instances": 44, "metric_value": 0.0, "depth": 4}
            if obj[1]>2:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 39, "metric_value": -0.0, "depth": 5}
               if obj[8]<=11:
                  # {"feature": "Alkaline_Phosphotase", "instances": 28, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Direct_Bilirubin", "instances": 23, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": -0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>7:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>15:
                           return 'liver'
                        elif obj[4]<=15:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>3:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>11:
                  # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[4]>35:
                     # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=35:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
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
               else:
                  return 'liver'
            elif obj[1]<=2:
               # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=9:
                     return 'liver'
                  elif obj[2]>9:
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
            # {"feature": "Total_Protiens", "instances": 70, "metric_value": 0.0, "depth": 4}
            if obj[6]>19.155279749709432:
               # {"feature": "Direct_Bilirubin", "instances": 51, "metric_value": -0.0, "depth": 5}
               if obj[2]<=32:
                  # {"feature": "Total_Bilirubin", "instances": 42, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 28, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=11:
                        # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 8}
                        if obj[4]>12:
                           return 'liver'
                        elif obj[4]<=12:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>11:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=29:
                           return 'normal'
                        elif obj[5]>29:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>8:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[5]>18:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[8]>6:
                           return 'liver'
                        elif obj[8]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=18:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]>32:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=19.155279749709432:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": 0.0, "depth": 5}
               if obj[8]<=5:
                  # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=6:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=28:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>28:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>23:
                           return 'liver'
                        elif obj[4]<=23:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>6:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=16:
                        return 'normal'
                     elif obj[1]>16:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[8]>5:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>21:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>21:
                           return 'liver'
                        elif obj[5]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=21:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=7:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 25, "metric_value": 0.0, "depth": 4}
            if obj[2]>7:
               # {"feature": "Total_Protiens", "instances": 15, "metric_value": -0.0, "depth": 5}
               if obj[6]<=59:
                  # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[4]>28:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[1]>23:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=68:
                           return 'normal'
                        elif obj[5]>68:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=23:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=28:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]>59:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[5]>47:
                     return 'liver'
                  elif obj[5]<=47:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>21:
                        return 'normal'
                     elif obj[1]<=21:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[2]<=7:
               # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 5}
               if obj[4]<=30:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 6}
                  if obj[5]>24:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=24:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        return 'normal'
                     elif obj[1]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[4]>30:
                  # {"feature": "Total_Protiens", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[6]>6:
                     return 'liver'
                  elif obj[6]<=6:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=1:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=15:
                           return 'normal'
                        elif obj[1]>15:
                           return 'liver'
                        else:
                           return 'liver'
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
   else:
      return 'liver'
