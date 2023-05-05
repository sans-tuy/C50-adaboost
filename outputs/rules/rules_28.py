def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]<=81.47896483100102:
            # {"feature": "Alamine_Aminotransferase", "instances": 144, "metric_value": -0.0, "depth": 4}
            if obj[4]<=50.65972222222222:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 101, "metric_value": -0.0, "depth": 5}
               if obj[8]<=14:
                  # {"feature": "Alkaline_Phosphotase", "instances": 86, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 72, "metric_value": 0.0, "depth": 7}
                     if obj[5]>11:
                        # {"feature": "Direct_Bilirubin", "instances": 71, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=4:
                           return 'liver'
                        elif obj[2]>4:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=11:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 7}
                     if obj[1]>13:
                        return 'liver'
                     elif obj[1]<=13:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=30:
                           return 'liver'
                        elif obj[5]>30:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>14:
                  # {"feature": "Alkaline_Phosphotase", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=14:
                        # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>14:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>8:
                           return 'normal'
                        elif obj[2]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[4]>50.65972222222222:
               # {"feature": "Alkaline_Phosphotase", "instances": 43, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=78:
                     # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 7}
                     if obj[2]>3:
                        # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=57:
                           return 'liver'
                        elif obj[1]>57:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=3:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>78:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=8:
                        return 'liver'
                     else:
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
            # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 4}
            if obj[1]<=7:
               # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=17:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]>291.0539499036609:
                        return 'liver'
                     elif obj[3]<=291.0539499036609:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]>2:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[1]>7:
               # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=32:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": -0.0, "depth": 8}
                        if obj[5]>18:
                           return 'normal'
                        elif obj[5]<=18:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[4]>32:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
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
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 118, "metric_value": -0.0, "depth": 3}
         if obj[6]>47.559322033898304:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 79, "metric_value": -0.0, "depth": 4}
            if obj[8]<=7:
               # {"feature": "Alkaline_Phosphotase", "instances": 52, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 33, "metric_value": 0.0, "depth": 6}
                  if obj[1]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 31, "metric_value": -0.0, "depth": 7}
                     if obj[4]>10:
                        # {"feature": "Direct_Bilirubin", "instances": 30, "metric_value": -0.0, "depth": 8}
                        if obj[2]>4:
                           return 'liver'
                        elif obj[2]<=4:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=10:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=1:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>22:
                           return 'liver'
                        elif obj[4]<=22:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[2]>7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[5]>64:
                        return 'liver'
                     elif obj[5]<=64:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=73:
                           return 'normal'
                        elif obj[1]>73:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=7:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>7:
               # {"feature": "Alkaline_Phosphotase", "instances": 27, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[4]>26:
                     # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[5]>42:
                           return 'liver'
                        elif obj[5]<=42:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=7:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>28:
                           return 'normal'
                        elif obj[5]<=28:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]<=26:
                     # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>16:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>25:
                           return 'normal'
                        elif obj[5]<=25:
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
            # {"feature": "Direct_Bilirubin", "instances": 39, "metric_value": -0.0, "depth": 4}
            if obj[2]>2:
               # {"feature": "Total_Bilirubin", "instances": 20, "metric_value": -0.0, "depth": 5}
               if obj[1]>18:
                  return 'liver'
               elif obj[1]<=18:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[5]>25:
                     return 'liver'
                  elif obj[5]<=25:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[2]<=2:
               # {"feature": "Alkaline_Phosphotase", "instances": 19, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=14:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": -0.0, "depth": 7}
                     if obj[5]>23:
                        # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[1]>4:
                           return 'liver'
                        elif obj[1]<=4:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=23:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>14:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=7:
                        return 'normal'
                     elif obj[1]>7:
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
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Total_Protiens", "instances": 123, "metric_value": 0.0, "depth": 4}
            if obj[6]>62.28455284552845:
               # {"feature": "Alkaline_Phosphotase", "instances": 90, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 65, "metric_value": 0.0, "depth": 6}
                  if obj[5]>11:
                     # {"feature": "Direct_Bilirubin", "instances": 64, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 50, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=36.52:
                           return 'normal'
                        elif obj[4]>36.52:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>7:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=11:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 25, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=102:
                           return 'liver'
                        elif obj[4]>102:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=103:
                           return 'liver'
                        elif obj[5]>103:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[1]>5:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>29:
                           return 'liver'
                        elif obj[5]<=29:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=5:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=62.28455284552845:
               # {"feature": "Total_Bilirubin", "instances": 33, "metric_value": -0.0, "depth": 5}
               if obj[1]<=8:
                  # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[5]>23:
                        # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[4]>29:
                           return 'liver'
                        elif obj[4]<=29:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=23:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]<=1:
                     # {"feature": "Alkaline_Phosphotase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]>31:
                           return 'liver'
                        elif obj[5]<=31:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>8:
                  # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=80:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[5]>21:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=21:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>80:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[5]>139:
                        return 'liver'
                     elif obj[5]<=139:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
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
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Direct_Bilirubin", "instances": 31, "metric_value": 0.0, "depth": 4}
            if obj[2]<=2:
               # {"feature": "Total_Protiens", "instances": 19, "metric_value": -0.0, "depth": 5}
               if obj[6]<=71:
                  # {"feature": "Alkaline_Phosphotase", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]>71:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[5]>24:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[4]>26:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=26:
                        # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=24:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
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
               else:
                  return 'normal'
            elif obj[2]>2:
               # {"feature": "Total_Protiens", "instances": 12, "metric_value": -0.0, "depth": 5}
               if obj[6]<=75:
                  # {"feature": "Alkaline_Phosphotase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>41:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=41:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]>75:
                  # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[4]>11:
                     # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[3]>291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
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
                  elif obj[4]<=11:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 95, "metric_value": -0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Alamine_Aminotransferase", "instances": 70, "metric_value": -0.0, "depth": 4}
            if obj[4]<=55.128571428571426:
               # {"feature": "Total_Protiens", "instances": 51, "metric_value": 0.0, "depth": 5}
               if obj[6]>42.05882352941177:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 32, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=12:
                     # {"feature": "Total_Bilirubin", "instances": 26, "metric_value": -0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=61:
                           return 'liver'
                        elif obj[5]>61:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=6:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'normal'
                        elif obj[2]>1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]>12:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]>10:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=10:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]<=42.05882352941177:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=76:
                     # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'liver'
                        elif obj[2]>1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[8]>76:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[4]>55.128571428571426:
               # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 5}
               if obj[2]>2:
                  # {"feature": "Total_Protiens", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[6]>8:
                     return 'liver'
                  elif obj[6]<=8:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>74:
                        return 'liver'
                     elif obj[5]<=74:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]<=2:
                  # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[5]>33:
                        # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=54:
                           return 'liver'
                        elif obj[6]>54:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=33:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[5]>40:
                        return 'liver'
                     elif obj[5]<=40:
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
            # {"feature": "Direct_Bilirubin", "instances": 25, "metric_value": 0.0, "depth": 4}
            if obj[2]<=118:
               # {"feature": "Aspartate_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 5}
               if obj[5]<=57:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[8]>6:
                     # {"feature": "Total_Protiens", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[6]<=59:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[4]>37:
                           return 'normal'
                        elif obj[4]<=37:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>59:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=6:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=13:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[4]>10:
                           return 'liver'
                        elif obj[4]<=10:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>13:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=25:
                           return 'normal'
                        elif obj[4]>25:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[5]>57:
                  # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[4]>48:
                     # {"feature": "Total_Protiens", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[6]>8:
                        return 'liver'
                     elif obj[6]<=8:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=48:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]>118:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
