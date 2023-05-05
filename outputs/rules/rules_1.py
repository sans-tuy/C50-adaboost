def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Albumin", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[7]>26.393063583815028:
      # {"feature": "Total_Protiens", "instances": 306, "metric_value": -0.0, "depth": 2}
      if obj[6]>61.73856209150327:
         # {"feature": "Alkaline_Phosphotase", "instances": 227, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 167, "metric_value": 0.0, "depth": 4}
            if obj[8]<=24.592814371257486:
               # {"feature": "Age", "instances": 143, "metric_value": -0.0, "depth": 5}
               if obj[0]>29.364389249503127:
                  # {"feature": "Alamine_Aminotransferase", "instances": 115, "metric_value": -0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 114, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=58.578947368421055:
                        # {"feature": "Direct_Bilirubin", "instances": 90, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>58.578947368421055:
                        # {"feature": "Total_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=12:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[0]<=29.364389249503127:
                  # {"feature": "Direct_Bilirubin", "instances": 28, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=3:
                     # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'normal'
                        elif obj[1]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=25:
                        # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'normal'
                        elif obj[1]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>3:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[4]>24:
                        return 'liver'
                     elif obj[4]<=24:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'normal'
                        elif obj[1]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            elif obj[8]>24.592814371257486:
               # {"feature": "Age", "instances": 24, "metric_value": -0.0, "depth": 5}
               if obj[0]>38:
                  # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[4]>34:
                     return 'liver'
                  elif obj[4]<=34:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>11:
                           return 'normal'
                        elif obj[1]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
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
               elif obj[0]<=38:
                  # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[1]>1:
                     # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=18:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=31:
                           return 'liver'
                        elif obj[5]>31:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>18:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=1:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Age", "instances": 60, "metric_value": 0.0, "depth": 4}
            if obj[0]>38.56666666666667:
               # {"feature": "Total_Bilirubin", "instances": 33, "metric_value": -0.0, "depth": 5}
               if obj[1]<=63.60606060606061:
                  # {"feature": "Direct_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 20, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=102:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[5]>45:
                           return 'liver'
                        elif obj[5]<=45:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>102:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>63.60606060606061:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[0]<=38.56666666666667:
               # {"feature": "Alamine_Aminotransferase", "instances": 27, "metric_value": -0.0, "depth": 5}
               if obj[4]>28:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 17, "metric_value": -0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=1:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        return 'liver'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[4]<=28:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=35:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'normal'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>35:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=1:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>5:
                           return 'liver'
                        elif obj[1]<=5:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>1:
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
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[6]<=61.73856209150327:
         # {"feature": "Alkaline_Phosphotase", "instances": 79, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 66, "metric_value": 0.0, "depth": 4}
            if obj[8]<=138.4110384267933:
               # {"feature": "Total_Bilirubin", "instances": 64, "metric_value": -0.0, "depth": 5}
               if obj[1]<=22.203125:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 52, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=65.07692307692308:
                     # {"feature": "Age", "instances": 41, "metric_value": -0.0, "depth": 7}
                     if obj[0]>45.80487804878049:
                        # {"feature": "Alamine_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 8}
                        if obj[4]>13:
                           return 'liver'
                        elif obj[4]<=13:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[0]<=45.80487804878049:
                        # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": -0.0, "depth": 8}
                        if obj[4]>14:
                           return 'liver'
                        elif obj[4]<=14:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>65.07692307692308:
                     # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[4]>17:
                        # {"feature": "Age", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[0]>18:
                           return 'liver'
                        elif obj[0]<=18:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=17:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]>22.203125:
                  # {"feature": "Age", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[0]>22:
                     return 'liver'
                  elif obj[0]<=22:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>138.4110384267933:
               return 'normal'
            else:
               return 'normal'
         elif obj[3]>291.0539499036609:
            # {"feature": "Age", "instances": 13, "metric_value": -0.0, "depth": 4}
            if obj[0]>45:
               return 'liver'
            elif obj[0]<=45:
               # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 5}
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
      # {"feature": "Alkaline_Phosphotase", "instances": 213, "metric_value": 0.0, "depth": 2}
      if obj[3]<=291.0539499036609:
         # {"feature": "Total_Protiens", "instances": 151, "metric_value": 0.0, "depth": 3}
         if obj[6]>21.50804221771271:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 115, "metric_value": 0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Age", "instances": 106, "metric_value": -0.0, "depth": 5}
               if obj[0]<=45.924528301886795:
                  # {"feature": "Alamine_Aminotransferase", "instances": 56, "metric_value": -0.0, "depth": 6}
                  if obj[4]>11:
                     # {"feature": "Direct_Bilirubin", "instances": 55, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 44, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=45.06818181818182:
                           return 'liver'
                        elif obj[1]>45.06818181818182:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[5]>41:
                           return 'liver'
                        elif obj[5]<=41:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=11:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[0]>45.924528301886795:
                  # {"feature": "Alamine_Aminotransferase", "instances": 50, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=39.06:
                     # {"feature": "Direct_Bilirubin", "instances": 34, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=5:
                        # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>5:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>39.06:
                     # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=158:
                        # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=19:
                           return 'liver'
                        elif obj[2]>19:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>158:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 5}
               if obj[2]<=11:
                  # {"feature": "Age", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[0]>26:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=14:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[4]>16:
                           return 'liver'
                        elif obj[4]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>14:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[0]<=26:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>11:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[6]<=21.50804221771271:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 36, "metric_value": -0.0, "depth": 4}
            if obj[8]<=9:
               # {"feature": "Age", "instances": 31, "metric_value": -0.0, "depth": 5}
               if obj[0]<=42.74193548387097:
                  # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=6:
                     # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=50:
                           return 'liver'
                        elif obj[4]>50:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
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
               elif obj[0]>42.74193548387097:
                  # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[4]>15:
                     # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'liver'
                        elif obj[2]>1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=15:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>9:
               # {"feature": "Age", "instances": 5, "metric_value": -0.0, "depth": 5}
               if obj[0]>48:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     return 'liver'
                  elif obj[2]<=1:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[0]<=48:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
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
      elif obj[3]>291.0539499036609:
         # {"feature": "Age", "instances": 62, "metric_value": 0.0, "depth": 3}
         if obj[0]>4:
            # {"feature": "Direct_Bilirubin", "instances": 61, "metric_value": -0.0, "depth": 4}
            if obj[2]<=30.081967213114755:
               # {"feature": "Total_Protiens", "instances": 42, "metric_value": 0.0, "depth": 5}
               if obj[6]>20.456726772054097:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 31, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=11:
                     # {"feature": "Total_Bilirubin", "instances": 26, "metric_value": -0.0, "depth": 7}
                     if obj[1]>19:
                        # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[4]>38:
                           return 'liver'
                        elif obj[4]<=38:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=19:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>11:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]>3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>16:
                           return 'normal'
                        elif obj[4]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=3:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=20.456726772054097:
                  # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=60:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=34:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>12:
                           return 'normal'
                        elif obj[1]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>34:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'normal'
                        elif obj[1]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>60:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]>30.081967213114755:
               # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 5}
               if obj[1]<=166:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[5]>102:
                           return 'liver'
                        elif obj[5]<=102:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=25:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]>7:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>166:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[0]<=4:
            return 'normal'
         else:
            return 'normal'
      else:
         return 'liver'
   else:
      return 'liver'
