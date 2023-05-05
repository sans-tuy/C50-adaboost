def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Albumin", "instances": 519, "metric_value": -0.0, "depth": 1}
   if obj[7]>26.393063583815028:
      # {"feature": "Alkaline_Phosphotase", "instances": 306, "metric_value": -0.0, "depth": 2}
      if obj[3]<=291.0539499036609:
         # {"feature": "Total_Protiens", "instances": 233, "metric_value": -0.0, "depth": 3}
         if obj[6]>16.04235045064071:
            # {"feature": "Age", "instances": 203, "metric_value": -0.0, "depth": 4}
            if obj[0]>44.039408866995075:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 104, "metric_value": -0.0, "depth": 5}
               if obj[8]<=133.1893171024874:
                  # {"feature": "Alamine_Aminotransferase", "instances": 100, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=43.37:
                     # {"feature": "Total_Bilirubin", "instances": 70, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Direct_Bilirubin", "instances": 55, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=16:
                           return 'liver'
                        elif obj[2]>16:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>43.37:
                     # {"feature": "Total_Bilirubin", "instances": 30, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=57:
                        # {"feature": "Direct_Bilirubin", "instances": 29, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=19:
                           return 'liver'
                        elif obj[2]>19:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>57:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>133.1893171024874:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[5]>24:
                     return 'liver'
                  elif obj[5]<=24:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[0]<=44.039408866995075:
               # {"feature": "Total_Bilirubin", "instances": 99, "metric_value": -0.0, "depth": 5}
               if obj[1]<=133.7792764040613:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 94, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=28.414893617021278:
                     # {"feature": "Direct_Bilirubin", "instances": 79, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=5:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 63, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=58.3968253968254:
                           return 'liver'
                        elif obj[5]>58.3968253968254:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>5:
                        # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[4]>11:
                           return 'liver'
                        elif obj[4]<=11:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[8]>28.414893617021278:
                     # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]>133.7792764040613:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=16.04235045064071:
            # {"feature": "Age", "instances": 30, "metric_value": -0.0, "depth": 4}
            if obj[0]<=42.96666666666667:
               # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 5}
               if obj[4]<=349:
                  # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[1]>1:
                     # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[5]>31:
                           return 'liver'
                        elif obj[5]<=31:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>21:
                           return 'liver'
                        elif obj[5]<=21:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>349:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[0]>42.96666666666667:
               # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 5}
               if obj[1]<=8:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=11:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>12:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>20:
                           return 'liver'
                        elif obj[5]<=20:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>11:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>17:
                           return 'liver'
                        elif obj[4]<=17:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>8:
                  # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[2]>2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>30:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>40:
                           return 'liver'
                        elif obj[5]<=40:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=30:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]>25:
                           return 'liver'
                        elif obj[5]<=25:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]<=2:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[3]>291.0539499036609:
         # {"feature": "Age", "instances": 73, "metric_value": -0.0, "depth": 3}
         if obj[0]<=40.63013698630137:
            # {"feature": "Direct_Bilirubin", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[2]<=5:
               # {"feature": "Alamine_Aminotransferase", "instances": 29, "metric_value": -0.0, "depth": 5}
               if obj[4]<=55:
                  # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": -0.0, "depth": 6}
                  if obj[1]>5:
                     # {"feature": "Total_Protiens", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[6]>59:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[5]>21:
                           return 'liver'
                        elif obj[5]<=21:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=59:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]>25:
                           return 'normal'
                        elif obj[5]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[1]<=5:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[4]>55:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[5]>108:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Total_Protiens", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[6]<=66:
                           return 'liver'
                        elif obj[6]>66:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=108:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]>72:
                           return 'liver'
                        elif obj[6]<=72:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]>62:
                           return 'liver'
                        elif obj[6]<=62:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]>5:
               # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[1]<=39:
                  # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=102:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>44:
                        return 'liver'
                     elif obj[5]<=44:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>102:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>39:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[0]>40.63013698630137:
            # {"feature": "Alamine_Aminotransferase", "instances": 36, "metric_value": -0.0, "depth": 4}
            if obj[4]<=87.69444444444444:
               # {"feature": "Aspartate_Aminotransferase", "instances": 25, "metric_value": 0.0, "depth": 5}
               if obj[5]<=56.52:
                  # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=228:
                     # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Protiens", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[6]>7:
                           return 'liver'
                        elif obj[6]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>228:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]>56.52:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[4]>87.69444444444444:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   elif obj[7]<=26.393063583815028:
      # {"feature": "Alkaline_Phosphotase", "instances": 213, "metric_value": -0.0, "depth": 2}
      if obj[3]<=291.0539499036609:
         # {"feature": "Total_Protiens", "instances": 151, "metric_value": -0.0, "depth": 3}
         if obj[6]>21.50804221771271:
            # {"feature": "Aspartate_Aminotransferase", "instances": 115, "metric_value": -0.0, "depth": 4}
            if obj[5]<=66.3391304347826:
               # {"feature": "Direct_Bilirubin", "instances": 86, "metric_value": -0.0, "depth": 5}
               if obj[2]<=5:
                  # {"feature": "Age", "instances": 61, "metric_value": -0.0, "depth": 6}
                  if obj[0]<=61.91488465421487:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 48, "metric_value": 0.0, "depth": 7}
                     if obj[8]>1:
                        # {"feature": "Total_Bilirubin", "instances": 45, "metric_value": -0.0, "depth": 8}
                        if obj[1]>1:
                           return 'normal'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]<=1:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[0]>61.91488465421487:
                     # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=26:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>26:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>5:
                  # {"feature": "Alamine_Aminotransferase", "instances": 25, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=47:
                     # {"feature": "Age", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[0]<=55:
                        return 'liver'
                     elif obj[0]>55:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=29:
                           return 'liver'
                        elif obj[1]>29:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>47:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>2:
                        # {"feature": "Age", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[0]>26:
                           return 'liver'
                        elif obj[0]<=26:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=2:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[5]>66.3391304347826:
               # {"feature": "Age", "instances": 29, "metric_value": -0.0, "depth": 5}
               if obj[0]>45.275862068965516:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=7:
                     return 'liver'
                  elif obj[8]>7:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=4:
                        return 'liver'
                     elif obj[1]>4:
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
               elif obj[0]<=45.275862068965516:
                  # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[1]>2:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[8]>1:
                        return 'liver'
                     elif obj[8]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=2:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=21.50804221771271:
            # {"feature": "Age", "instances": 36, "metric_value": 0.0, "depth": 4}
            if obj[0]<=44.19444444444444:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": 0.0, "depth": 5}
               if obj[8]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[1]>8:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]>3:
                           return 'liver'
                        elif obj[2]<=3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=8:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[5]>23:
                        return 'liver'
                     elif obj[5]<=23:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>1:
                  # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'normal'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=25:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
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
            elif obj[0]>44.19444444444444:
               # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 5}
               if obj[5]>25:
                  # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[8]>1:
                        return 'liver'
                     elif obj[8]<=1:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>8:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=25:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
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
      elif obj[3]>291.0539499036609:
         # {"feature": "Total_Protiens", "instances": 62, "metric_value": 0.0, "depth": 3}
         if obj[6]>23.726199171384:
            # {"feature": "Age", "instances": 48, "metric_value": 0.0, "depth": 4}
            if obj[0]>7:
               # {"feature": "Total_Bilirubin", "instances": 47, "metric_value": -0.0, "depth": 5}
               if obj[1]<=60.8936170212766:
                  # {"feature": "Direct_Bilirubin", "instances": 32, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=49:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 30, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=35:
                        # {"feature": "Alamine_Aminotransferase", "instances": 25, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=185.99589032832972:
                           return 'liver'
                        elif obj[4]>185.99589032832972:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>35:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[4]>20:
                           return 'liver'
                        elif obj[4]<=20:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>49:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>60.8936170212766:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=5:
                     return 'liver'
                  elif obj[8]>5:
                     # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[2]>32:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>64:
                           return 'liver'
                        elif obj[5]<=64:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=32:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'liver'
                        elif obj[4]<=25:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[0]<=7:
               return 'liver'
            else:
               return 'liver'
         elif obj[6]<=23.726199171384:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 14, "metric_value": -0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[4]>28:
                  return 'liver'
               elif obj[4]<=28:
                  # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[1]>12:
                     # {"feature": "Age", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[0]<=18:
                        return 'normal'
                     elif obj[0]>18:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=12:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Age", "instances": 5, "metric_value": 0.0, "depth": 5}
               if obj[0]<=38:
                  # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[1]>9:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=4:
                        return 'normal'
                     elif obj[2]>4:
                        return 'liver'
                     else:
                        return 'liver'
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
               elif obj[0]>38:
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
