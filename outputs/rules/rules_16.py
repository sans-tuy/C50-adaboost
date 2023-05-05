def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alamine_Aminotransferase", "instances": 152, "metric_value": -0.0, "depth": 3}
         if obj[4]<=50.125:
            # {"feature": "Total_Protiens", "instances": 108, "metric_value": 0.0, "depth": 4}
            if obj[6]>61.52777777777778:
               # {"feature": "Alkaline_Phosphotase", "instances": 79, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 67, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=17:
                     # {"feature": "Direct_Bilirubin", "instances": 63, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 40, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 8}
                        if obj[5]>31:
                           return 'liver'
                        elif obj[5]<=31:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>17:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>5:
                           return 'normal'
                        elif obj[2]<=5:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[1]>9:
                     return 'liver'
                  elif obj[1]<=9:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=36:
                        return 'liver'
                     elif obj[5]>36:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=61.52777777777778:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 29, "metric_value": 0.0, "depth": 5}
               if obj[8]<=15:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=31:
                     # {"feature": "Alkaline_Phosphotase", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'normal'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[3]>291.0539499036609:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>31:
                     # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=12:
                           return 'normal'
                        elif obj[2]>12:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>15:
                  # {"feature": "Alkaline_Phosphotase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'normal'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[4]>50.125:
            # {"feature": "Alkaline_Phosphotase", "instances": 44, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[8]<=116:
                  # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[1]>15:
                     # {"feature": "Total_Protiens", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[6]>56:
                        # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=14:
                           return 'liver'
                        elif obj[2]>14:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=56:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=15:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[5]>41:
                        # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=41:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>116:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Alamine_Aminotransferase", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[4]<=42.135802469135804:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 59, "metric_value": -0.0, "depth": 5}
               if obj[8]>5:
                  # {"feature": "Total_Protiens", "instances": 38, "metric_value": -0.0, "depth": 6}
                  if obj[6]>49.473684210526315:
                     # {"feature": "Total_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=28:
                           return 'liver'
                        elif obj[5]>28:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]<=49.473684210526315:
                     # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'normal'
                        elif obj[1]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]<=5:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[5]>12:
                     # {"feature": "Direct_Bilirubin", "instances": 20, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=8:
                        # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=12:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[4]>42.135802469135804:
               # {"feature": "Aspartate_Aminotransferase", "instances": 22, "metric_value": 0.0, "depth": 5}
               if obj[5]>25:
                  # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[1]>11:
                     # {"feature": "Total_Protiens", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[6]>54:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[2]>6:
                           return 'liver'
                        elif obj[2]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=54:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=11:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[8]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'liver'
                        elif obj[2]>1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=25:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 37, "metric_value": -0.0, "depth": 4}
            if obj[8]<=37:
               # {"feature": "Total_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 5}
               if obj[1]<=67.64516129032258:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=142:
                     # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=8:
                        # {"feature": "Total_Protiens", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[6]>52:
                           return 'liver'
                        elif obj[6]<=52:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>142:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>67.64516129032258:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[5]>77:
                     return 'liver'
                  elif obj[5]<=77:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=48:
                        return 'liver'
                     elif obj[4]>48:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>37:
               # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 5}
               if obj[5]>28:
                  # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[1]>3:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]>3:
                        return 'liver'
                     elif obj[2]<=3:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=3:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=28:
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
            # {"feature": "Total_Protiens", "instances": 116, "metric_value": -0.0, "depth": 4}
            if obj[6]>60.3448275862069:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 86, "metric_value": 0.0, "depth": 5}
               if obj[8]<=125.29206274207583:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 78, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=196.67912268723794:
                     # {"feature": "Total_Bilirubin", "instances": 73, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=69.5814596138045:
                        # {"feature": "Direct_Bilirubin", "instances": 67, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=6:
                           return 'normal'
                        elif obj[2]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>69.5814596138045:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>196.67912268723794:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>125.29206274207583:
                  # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=42:
                        return 'liver'
                     elif obj[4]>42:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>87:
                           return 'normal'
                        elif obj[5]<=87:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[2]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=60.3448275862069:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 30, "metric_value": -0.0, "depth": 5}
               if obj[8]>9:
                  # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=102:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[5]>31:
                           return 'liver'
                        elif obj[5]<=31:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>102:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>14:
                        return 'liver'
                     elif obj[4]<=14:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]<=9:
                  # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 6}
                  if obj[4]>15:
                     # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=15:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[6]<=72:
               # {"feature": "Alamine_Aminotransferase", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[4]>55:
                  # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=39:
                     # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[2]>3:
                        return 'liver'
                     elif obj[2]<=3:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[5]>82:
                           return 'liver'
                        elif obj[5]<=82:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>39:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=55:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=66:
                     # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]>66:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[6]>72:
               # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 5}
               if obj[4]<=33:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=9:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[1]>8:
                           return 'normal'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>3:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>9:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>21:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>5:
                           return 'liver'
                        elif obj[1]<=5:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=21:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>33:
                  # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[2]>2:
                     return 'liver'
                  elif obj[2]<=2:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]>42:
                           return 'liver'
                        elif obj[5]<=42:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=8:
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
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": -0.0, "depth": 3}
         if obj[6]>44.49473684210526:
            # {"feature": "Alkaline_Phosphotase", "instances": 63, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 46, "metric_value": 0.0, "depth": 5}
               if obj[5]<=69.41304347826087:
                  # {"feature": "Alamine_Aminotransferase", "instances": 33, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=64.72792721273521:
                     # {"feature": "Direct_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=4:
                        # {"feature": "Total_Bilirubin", "instances": 25, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'normal'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>4:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>64.72792721273521:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=1:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]>69.41304347826087:
                  # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 6}
                  if obj[4]>65:
                     return 'liver'
                  elif obj[4]<=65:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[1]>53:
                        return 'liver'
                     elif obj[1]<=53:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=23:
                           return 'normal'
                        elif obj[2]>23:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 5}
               if obj[2]<=14:
                  # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=48:
                     return 'liver'
                  elif obj[4]>48:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[5]>17:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'normal'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=17:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[2]>14:
                  # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[1]>28:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[4]>50:
                        return 'liver'
                     elif obj[4]<=50:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=47:
                           return 'normal'
                        elif obj[5]>47:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[1]<=28:
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
               # {"feature": "Direct_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[2]<=5:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=6:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[5]>28:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[4]>23:
                           return 'liver'
                        elif obj[4]<=23:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=28:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>6:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=28:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>28:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]>5:
                  # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[1]>13:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[8]>1:
                        return 'liver'
                     elif obj[8]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'normal'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[1]<=13:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[1]>9:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
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
                  elif obj[8]<=1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>48:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>4:
                           return 'liver'
                        elif obj[2]<=4:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=48:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=9:
                  # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=30:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=1:
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
