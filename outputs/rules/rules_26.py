def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": -0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": -0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]>60.46052631578947:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 117, "metric_value": -0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Alamine_Aminotransferase", "instances": 91, "metric_value": -0.0, "depth": 5}
               if obj[4]<=53.21978021978022:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 68, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=33.455882352941174:
                     # {"feature": "Direct_Bilirubin", "instances": 42, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 30, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>2:
                        # {"feature": "Alkaline_Phosphotase", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        elif obj[3]>291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>33.455882352941174:
                     # {"feature": "Alkaline_Phosphotase", "instances": 26, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=49:
                           return 'liver'
                        elif obj[1]>49:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[3]>291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[1]>36:
                           return 'liver'
                        elif obj[1]<=36:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>53.21978021978022:
                  # {"feature": "Alkaline_Phosphotase", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[3]>291.0539499036609:
                     return 'liver'
                  elif obj[3]<=291.0539499036609:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=156:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[1]>18:
                           return 'liver'
                        elif obj[1]<=18:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>156:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Alamine_Aminotransferase", "instances": 26, "metric_value": 0.0, "depth": 5}
               if obj[4]>18:
                  # {"feature": "Alkaline_Phosphotase", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=18:
                  # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=20:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=1:
                           return 'liver'
                        elif obj[1]>1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>20:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[6]<=60.46052631578947:
            # {"feature": "Aspartate_Aminotransferase", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[5]<=53.48571428571429:
               # {"feature": "Alamine_Aminotransferase", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[4]>13:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=139:
                     # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Direct_Bilirubin", "instances": 20, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]>139:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[4]<=13:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=7:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[5]>53.48571428571429:
               # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 5}
               if obj[1]>9:
                  # {"feature": "Alkaline_Phosphotase", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[4]>55:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=15:
                           return 'normal'
                        elif obj[2]>15:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=55:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=9:
                  # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>17:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'liver'
                        elif obj[2]>1:
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
                  return 'normal'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[6]>47.559322033898304:
            # {"feature": "Alkaline_Phosphotase", "instances": 79, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 54, "metric_value": 0.0, "depth": 5}
               if obj[8]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 50, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=41.92:
                     # {"feature": "Total_Bilirubin", "instances": 35, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=44:
                        # {"feature": "Direct_Bilirubin", "instances": 34, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=15:
                           return 'liver'
                        elif obj[2]>15:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>44:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>41.92:
                     # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[2]>15:
                        return 'liver'
                     elif obj[2]<=15:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=13:
                           return 'normal'
                        elif obj[1]>13:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=9:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=16:
                           return 'liver'
                        elif obj[4]>16:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>9:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=7:
                        return 'normal'
                     elif obj[2]>7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 25, "metric_value": 0.0, "depth": 5}
               if obj[1]<=68.72:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 16, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=6:
                     return 'liver'
                  elif obj[8]>6:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=15:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=20:
                           return 'liver'
                        elif obj[4]>20:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>15:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>68.72:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=5:
                     return 'liver'
                  elif obj[8]>5:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
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
            else:
               return 'liver'
         elif obj[6]<=47.559322033898304:
            # {"feature": "Alkaline_Phosphotase", "instances": 39, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 27, "metric_value": 0.0, "depth": 5}
               if obj[8]<=14:
                  # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=58:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 7}
                     if obj[5]>29:
                        # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=59:
                           return 'liver'
                        elif obj[4]>59:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=29:
                        # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>58:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>14:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[2]>2:
                     return 'liver'
                  elif obj[2]<=2:
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
            elif obj[3]>291.0539499036609:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": -0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Total_Protiens", "instances": 123, "metric_value": -0.0, "depth": 4}
            if obj[6]>62.28455284552845:
               # {"feature": "Alkaline_Phosphotase", "instances": 90, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 65, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=348.3512773089204:
                     # {"feature": "Total_Bilirubin", "instances": 61, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=180.26451869044627:
                        # {"feature": "Direct_Bilirubin", "instances": 59, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>180.26451869044627:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>348.3512773089204:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 25, "metric_value": 0.0, "depth": 6}
                  if obj[4]>47:
                     # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=23:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=231:
                           return 'liver'
                        elif obj[5]>231:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>23:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=47:
                     # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=15:
                        # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>15:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
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
               else:
                  return 'liver'
            elif obj[6]<=62.28455284552845:
               # {"feature": "Alkaline_Phosphotase", "instances": 33, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 29, "metric_value": 0.0, "depth": 6}
                  if obj[4]>14:
                     # {"feature": "Direct_Bilirubin", "instances": 28, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=9:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 8}
                        if obj[5]>33:
                           return 'liver'
                        elif obj[5]<=33:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>9:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=71:
                           return 'liver'
                        elif obj[1]>71:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=14:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[3]>291.0539499036609:
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
         elif obj[8]<=1:
            # {"feature": "Total_Protiens", "instances": 31, "metric_value": 0.0, "depth": 4}
            if obj[6]<=76:
               # {"feature": "Alkaline_Phosphotase", "instances": 23, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=29:
                           return 'liver'
                        elif obj[4]>29:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[4]>27:
                           return 'liver'
                        elif obj[4]<=27:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[1]>6:
                     return 'liver'
                  elif obj[1]<=6:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=1:
                        return 'normal'
                     elif obj[2]>1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[6]>76:
               # {"feature": "Alkaline_Phosphotase", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[5]>23:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'normal'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=23:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        return 'normal'
                     elif obj[1]>9:
                        return 'liver'
                     else:
                        return 'liver'
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
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 70, "metric_value": 0.0, "depth": 4}
            if obj[2]<=82:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 65, "metric_value": 0.0, "depth": 5}
               if obj[8]<=8:
                  # {"feature": "Total_Protiens", "instances": 42, "metric_value": -0.0, "depth": 6}
                  if obj[6]<=53:
                     # {"feature": "Alamine_Aminotransferase", "instances": 29, "metric_value": -0.0, "depth": 7}
                     if obj[4]>12:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 28, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=104.75:
                           return 'liver'
                        elif obj[5]>104.75:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]>53:
                     # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[4]>20:
                        # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=20:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>8:
                  # {"feature": "Total_Protiens", "instances": 23, "metric_value": 0.0, "depth": 6}
                  if obj[6]>28:
                     # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": 0.0, "depth": 7}
                     if obj[4]>20:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=54:
                           return 'normal'
                        elif obj[5]>54:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=20:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'normal'
                        elif obj[1]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]<=28:
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
            elif obj[2]>82:
               return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 25, "metric_value": -0.0, "depth": 4}
            if obj[2]<=82:
               # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 5}
               if obj[4]<=50:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=47:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=7:
                        # {"feature": "Total_Protiens", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[6]>7:
                           return 'normal'
                        elif obj[6]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>7:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>47:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>50:
                  # {"feature": "Total_Protiens", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[6]>6:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[8]>7:
                           return 'normal'
                        elif obj[8]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=8:
                        return 'liver'
                     else:
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
            elif obj[2]>82:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
