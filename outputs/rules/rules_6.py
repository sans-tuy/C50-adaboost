def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Albumin", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[7]>26.393063583815028:
      # {"feature": "Alkaline_Phosphotase", "instances": 306, "metric_value": 0.0, "depth": 2}
      if obj[3]<=291.0539499036609:
         # {"feature": "Age", "instances": 233, "metric_value": 0.0, "depth": 3}
         if obj[0]<=58.69931688737856:
            # {"feature": "Aspartate_Aminotransferase", "instances": 189, "metric_value": 0.0, "depth": 4}
            if obj[5]<=95.39682539682539:
               # {"feature": "Direct_Bilirubin", "instances": 159, "metric_value": -0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Total_Bilirubin", "instances": 100, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Total_Protiens", "instances": 57, "metric_value": 0.0, "depth": 7}
                     if obj[6]>64.19298245614036:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 37, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=18:
                           return 'liver'
                        elif obj[8]>18:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=64.19298245614036:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 20, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=9:
                           return 'liver'
                        elif obj[8]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=7:
                     # {"feature": "Total_Protiens", "instances": 43, "metric_value": -0.0, "depth": 7}
                     if obj[6]>32.59081981572213:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 35, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=17:
                           return 'liver'
                        elif obj[8]>17:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=32.59081981572213:
                        # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
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
               elif obj[2]>2:
                  # {"feature": "Total_Bilirubin", "instances": 59, "metric_value": 0.0, "depth": 6}
                  if obj[1]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 46, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=42.0:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 31, "metric_value": -0.0, "depth": 8}
                        if obj[8]>8:
                           return 'liver'
                        elif obj[8]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>42.0:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=8:
                           return 'liver'
                        elif obj[8]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=1:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=13:
                        # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[4]>19:
                           return 'liver'
                        elif obj[4]<=19:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>13:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]>95.39682539682539:
               # {"feature": "Direct_Bilirubin", "instances": 30, "metric_value": -0.0, "depth": 5}
               if obj[2]>2:
                  # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[1]>31:
                     return 'liver'
                  elif obj[1]<=31:
                     # {"feature": "Total_Protiens", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[6]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[4]>48:
                           return 'liver'
                        elif obj[4]<=48:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=6:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]<=2:
                  # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[4]>97:
                     return 'liver'
                  elif obj[4]<=97:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=6:
                        return 'liver'
                     elif obj[1]>6:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[0]>58.69931688737856:
            # {"feature": "Total_Protiens", "instances": 44, "metric_value": -0.0, "depth": 4}
            if obj[6]>18.925876513124905:
               # {"feature": "Total_Bilirubin", "instances": 39, "metric_value": -0.0, "depth": 5}
               if obj[1]<=12:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 30, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=51.13333333333333:
                     # {"feature": "Alamine_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=28:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 16, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=9:
                           return 'normal'
                        elif obj[8]>9:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>28:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>51.13333333333333:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        return 'liver'
                     elif obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=42:
                           return 'normal'
                        elif obj[4]>42:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]>12:
                  # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=27:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[5]>51:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=9:
                           return 'liver'
                        elif obj[8]>9:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=51:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>12:
                           return 'liver'
                        elif obj[4]<=12:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]>27:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=18.925876513124905:
               # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 5}
               if obj[4]>17:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[2]>2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=40:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=2:
                           return 'liver'
                        elif obj[1]>2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]<=2:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[4]<=17:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'normal'
         else:
            return 'liver'
      elif obj[3]>291.0539499036609:
         # {"feature": "Age", "instances": 73, "metric_value": 0.0, "depth": 3}
         if obj[0]>4:
            # {"feature": "Direct_Bilirubin", "instances": 72, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 61, "metric_value": 0.0, "depth": 5}
               if obj[8]>6:
                  # {"feature": "Total_Protiens", "instances": 49, "metric_value": 0.0, "depth": 6}
                  if obj[6]>6:
                     # {"feature": "Total_Bilirubin", "instances": 47, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 46, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=144.7173913043478:
                           return 'liver'
                        elif obj[5]>144.7173913043478:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=6:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=6:
                  # {"feature": "Total_Protiens", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[6]>62:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[1]>17:
                        return 'liver'
                     elif obj[1]<=17:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]<=62:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": 0.0, "depth": 5}
               if obj[8]>9:
                  # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=21:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[4]>28:
                        return 'liver'
                     elif obj[4]<=28:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>29:
                           return 'liver'
                        elif obj[5]<=29:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>21:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=9:
                  # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=25:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        return 'liver'
                     elif obj[1]>8:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>25:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[0]<=4:
            return 'normal'
         else:
            return 'normal'
      else:
         return 'liver'
   elif obj[7]<=26.393063583815028:
      # {"feature": "Alkaline_Phosphotase", "instances": 213, "metric_value": 0.0, "depth": 2}
      if obj[3]<=291.0539499036609:
         # {"feature": "Total_Protiens", "instances": 151, "metric_value": 0.0, "depth": 3}
         if obj[6]>45.76158940397351:
            # {"feature": "Aspartate_Aminotransferase", "instances": 101, "metric_value": -0.0, "depth": 4}
            if obj[5]<=69.58415841584159:
               # {"feature": "Alamine_Aminotransferase", "instances": 74, "metric_value": -0.0, "depth": 5}
               if obj[4]<=31.283783783783782:
                  # {"feature": "Age", "instances": 50, "metric_value": 0.0, "depth": 6}
                  if obj[0]<=49.08:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 26, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=75:
                        # {"feature": "Total_Bilirubin", "instances": 25, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>75:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[0]>49.08:
                     # {"feature": "Total_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=39:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 22, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=6:
                           return 'liver'
                        elif obj[8]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>39:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>31.283783783783782:
                  # {"feature": "Age", "instances": 24, "metric_value": 0.0, "depth": 6}
                  if obj[0]>26:
                     # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=6:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=11:
                           return 'normal'
                        elif obj[8]>11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>6:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[0]<=26:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>7:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'normal'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]>69.58415841584159:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 27, "metric_value": 0.0, "depth": 5}
               if obj[8]<=9:
                  # {"feature": "Age", "instances": 20, "metric_value": -0.0, "depth": 6}
                  if obj[0]>35:
                     # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[2]>21:
                        # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[1]>158:
                           return 'liver'
                        elif obj[1]<=158:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=21:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[0]<=35:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>9:
                  # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Age", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[0]>33:
                        return 'normal'
                     elif obj[0]<=33:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=45.76158940397351:
            # {"feature": "Age", "instances": 50, "metric_value": -0.0, "depth": 4}
            if obj[0]>29.91548935920678:
               # {"feature": "Alamine_Aminotransferase", "instances": 41, "metric_value": 0.0, "depth": 5}
               if obj[4]<=88.62590164700478:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 37, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=75:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 36, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=41.44444444444444:
                        # {"feature": "Direct_Bilirubin", "instances": 23, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>41.44444444444444:
                        # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>75:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>88.62590164700478:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[0]<=29.91548935920678:
               # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[4]>15:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=3:
                     return 'liver'
                  elif obj[8]>3:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>5:
                           return 'liver'
                        elif obj[2]<=5:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=6:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[4]<=15:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[3]>291.0539499036609:
         # {"feature": "Age", "instances": 62, "metric_value": 0.0, "depth": 3}
         if obj[0]>14.741806709418839:
            # {"feature": "Total_Bilirubin", "instances": 59, "metric_value": 0.0, "depth": 4}
            if obj[1]<=56.728813559322035:
               # {"feature": "Total_Protiens", "instances": 40, "metric_value": 0.0, "depth": 5}
               if obj[6]>42.875:
                  # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": 0.0, "depth": 6}
                  if obj[2]>5:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 7}
                     if obj[5]>22:
                        # {"feature": "Alamine_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 8}
                        if obj[4]>12:
                           return 'liver'
                        elif obj[4]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=22:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=5:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[5]>34:
                        return 'liver'
                     elif obj[5]<=34:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>17:
                           return 'liver'
                        elif obj[4]<=17:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=42.875:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": 0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=52:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>25:
                           return 'liver'
                        elif obj[5]<=25:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>52:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=68:
                        return 'liver'
                     elif obj[5]>68:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[1]>56.728813559322035:
               # {"feature": "Aspartate_Aminotransferase", "instances": 19, "metric_value": 0.0, "depth": 5}
               if obj[5]>77:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[8]>4:
                     # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[2]>32:
                        return 'liver'
                     elif obj[2]<=32:
                        # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[6]>57:
                           return 'liver'
                        elif obj[6]<=57:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[8]<=4:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=77:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[8]>5:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]>32:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>35:
                           return 'normal'
                        elif obj[4]<=35:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=32:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]<=5:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[0]<=14.741806709418839:
            # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 4}
            if obj[6]>8:
               return 'liver'
            elif obj[6]<=8:
               return 'normal'
            else:
               return 'normal'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
