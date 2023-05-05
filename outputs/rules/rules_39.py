def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]>60.46052631578947:
            # {"feature": "Alkaline_Phosphotase", "instances": 117, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 89, "metric_value": 0.0, "depth": 5}
               if obj[4]>10:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 88, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=57.54545454545455:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 65, "metric_value": 0.0, "depth": 7}
                     if obj[8]>8:
                        # {"feature": "Total_Bilirubin", "instances": 40, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=8:
                        # {"feature": "Total_Bilirubin", "instances": 25, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>57.54545454545455:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[8]>7:
                        # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[1]>4:
                           return 'liver'
                        elif obj[1]<=4:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=10:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 28, "metric_value": 0.0, "depth": 5}
               if obj[2]<=16:
                  # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[1]>6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 17, "metric_value": -0.0, "depth": 7}
                     if obj[4]>33:
                        return 'liver'
                     elif obj[4]<=33:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=36:
                           return 'liver'
                        elif obj[5]>36:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=6:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>16:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=60.46052631578947:
            # {"feature": "Aspartate_Aminotransferase", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[5]<=53.48571428571429:
               # {"feature": "Direct_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=15:
                     # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=20:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'normal'
                        elif obj[1]>7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>20:
                        # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>15:
                     # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
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
               elif obj[2]>2:
                  # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[4]>19:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=13:
                        # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>13:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=19:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=1:
                           return 'normal'
                        elif obj[1]>1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[5]>53.48571428571429:
               # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 5}
               if obj[4]<=58:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[1]>6:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        return 'liver'
                     elif obj[2]<=2:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=6:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
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
               elif obj[4]>58:
                  # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": -0.0, "depth": 6}
                  if obj[3]>291.0539499036609:
                     return 'liver'
                  elif obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=17:
                        return 'normal'
                     elif obj[1]>17:
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
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[6]>47.123456790123456:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 54, "metric_value": -0.0, "depth": 5}
               if obj[8]<=8:
                  # {"feature": "Alamine_Aminotransferase", "instances": 39, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=32.92307692307692:
                     # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=42:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 21, "metric_value": 0.0, "depth": 8}
                        if obj[5]>12:
                           return 'liver'
                        elif obj[5]<=12:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>42:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>32.92307692307692:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 7}
                     if obj[5]>65:
                        return 'liver'
                     elif obj[5]<=65:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1]>13:
                           return 'liver'
                        elif obj[1]<=13:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>8:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=28:
                     # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>28:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=42:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>42:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=13:
                           return 'normal'
                        elif obj[2]>13:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=47.123456790123456:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 27, "metric_value": 0.0, "depth": 5}
               if obj[8]>5:
                  # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[4]>22:
                     # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=22:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=40:
                           return 'liver'
                        elif obj[5]>40:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]<=5:
                  # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=33:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[5]>21:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'liver'
                        elif obj[1]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=21:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>33:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Aspartate_Aminotransferase", "instances": 33, "metric_value": 0.0, "depth": 5}
               if obj[5]<=340.42424242424244:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 24, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=8:
                     # {"feature": "Total_Protiens", "instances": 17, "metric_value": 0.0, "depth": 7}
                     if obj[6]<=55:
                        return 'liver'
                     elif obj[6]>55:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[1]>47:
                           return 'liver'
                        elif obj[1]<=47:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>8:
                     # {"feature": "Total_Protiens", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[6]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=64:
                           return 'liver'
                        elif obj[4]>64:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]>340.42424242424244:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 5}
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
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 116, "metric_value": -0.0, "depth": 4}
            if obj[6]<=84.16676164311447:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 109, "metric_value": -0.0, "depth": 5}
               if obj[8]<=27.40366972477064:
                  # {"feature": "Direct_Bilirubin", "instances": 91, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 78, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=562.680381229843:
                        # {"feature": "Alamine_Aminotransferase", "instances": 72, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=49.333333333333336:
                           return 'normal'
                        elif obj[4]>49.333333333333336:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>562.680381229843:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[5]>25:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'liver'
                        elif obj[1]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=25:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=32:
                           return 'normal'
                        elif obj[4]>32:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]>27.40366972477064:
                  # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[4]>34:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=34:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>2:
                     # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[1]>12:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=91:
                           return 'liver'
                        elif obj[4]>91:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=12:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>34:
                           return 'normal'
                        elif obj[4]<=34:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]>84.16676164311447:
               # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 5}
               if obj[1]<=7:
                  return 'liver'
               elif obj[1]>7:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        return 'normal'
                     elif obj[4]<=15:
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
            if obj[8]<=16:
               # {"feature": "Total_Protiens", "instances": 36, "metric_value": -0.0, "depth": 5}
               if obj[6]>69:
                  # {"feature": "Total_Bilirubin", "instances": 20, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=22:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=108:
                        # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'normal'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>108:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>22:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=69:
                  # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": -0.0, "depth": 6}
                  if obj[4]>47:
                     # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]>82:
                           return 'liver'
                        elif obj[5]<=82:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>3:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=47:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'normal'
                        elif obj[2]>3:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>16:
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
               if obj[8]<=76:
                  # {"feature": "Direct_Bilirubin", "instances": 48, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=6:
                     # {"feature": "Total_Bilirubin", "instances": 34, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Alamine_Aminotransferase", "instances": 28, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=39.642857142857146:
                           return 'normal'
                        elif obj[4]>39.642857142857146:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[5]>22:
                           return 'liver'
                        elif obj[5]<=22:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]>6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[4]>32:
                        return 'liver'
                     elif obj[4]<=32:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1]>16:
                           return 'liver'
                        elif obj[1]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>76:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[5]>29:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=2:
                        return 'liver'
                     elif obj[1]>2:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=29:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[5]>24:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=7:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=74:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'liver'
                        elif obj[4]<=25:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>74:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[4]>48:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'normal'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=48:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=24:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=19.418485261141242:
            # {"feature": "Direct_Bilirubin", "instances": 26, "metric_value": 0.0, "depth": 4}
            if obj[2]<=2:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": 0.0, "depth": 5}
               if obj[8]<=7:
                  # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Alkaline_Phosphotase", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=25:
                           return 'liver'
                        elif obj[4]>25:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>8:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        return 'liver'
                     elif obj[3]>291.0539499036609:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]>7:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[2]>2:
               # {"feature": "Alkaline_Phosphotase", "instances": 13, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[4]>20:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=16:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>62:
                           return 'liver'
                        elif obj[5]<=62:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>16:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=20:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=1:
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
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[1]>9:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>48:
                           return 'liver'
                        elif obj[5]<=48:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=10:
                           return 'normal'
                        elif obj[4]>10:
                           return 'liver'
                        else:
                           return 'liver'
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
