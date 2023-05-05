def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]>60.46052631578947:
            # {"feature": "Alkaline_Phosphotase", "instances": 117, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 89, "metric_value": -0.0, "depth": 5}
               if obj[8]<=112:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 85, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=57.811764705882354:
                     # {"feature": "Alamine_Aminotransferase", "instances": 62, "metric_value": 0.0, "depth": 7}
                     if obj[4]>10:
                        # {"feature": "Direct_Bilirubin", "instances": 61, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=6:
                           return 'liver'
                        elif obj[2]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=10:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]>57.811764705882354:
                     # {"feature": "Direct_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[4]>28:
                           return 'liver'
                        elif obj[4]<=28:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>8:
                        # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[1]>4:
                           return 'liver'
                        elif obj[1]<=4:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>112:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=5:
                     return 'liver'
                  elif obj[2]>5:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 28, "metric_value": 0.0, "depth": 5}
               if obj[4]<=79.07142857142857:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Direct_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        return 'liver'
                     elif obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>79.07142857142857:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=60.46052631578947:
            # {"feature": "Aspartate_Aminotransferase", "instances": 35, "metric_value": -0.0, "depth": 4}
            if obj[5]<=53.48571428571429:
               # {"feature": "Alamine_Aminotransferase", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[4]<=30:
                  # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alkaline_Phosphotase", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[8]>11:
                           return 'normal'
                        elif obj[8]<=11:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]<=1:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=1:
                        # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>1:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[4]>30:
                  # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[8]>9:
                           return 'liver'
                        elif obj[8]<=9:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=8:
                        return 'liver'
                     elif obj[8]>8:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>11:
                           return 'liver'
                        elif obj[1]<=11:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]>53.48571428571429:
               # {"feature": "Alkaline_Phosphotase", "instances": 11, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[2]>2:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>17:
                        return 'liver'
                     elif obj[1]<=17:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]<=2:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=17:
                           return 'normal'
                        elif obj[4]>17:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>6:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[3]>291.0539499036609:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Total_Bilirubin", "instances": 69, "metric_value": 0.0, "depth": 5}
               if obj[1]<=29.231884057971016:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 53, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=11:
                     # {"feature": "Total_Protiens", "instances": 44, "metric_value": -0.0, "depth": 7}
                     if obj[6]>49.0:
                        # {"feature": "Alamine_Aminotransferase", "instances": 27, "metric_value": -0.0, "depth": 8}
                        if obj[4]>24:
                           return 'liver'
                        elif obj[4]<=24:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=49.0:
                        # {"feature": "Alamine_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=41:
                           return 'liver'
                        elif obj[4]>41:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>11:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[4]>18:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[5]>27:
                           return 'liver'
                        elif obj[5]<=27:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=18:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>29.231884057971016:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 5}
               if obj[5]>33:
                  # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[4]>24:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]>4:
                        # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=5:
                           return 'liver'
                        elif obj[6]>5:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=4:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=24:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        return 'liver'
                     elif obj[1]<=6:
                        # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[6]>5:
                           return 'normal'
                        elif obj[6]<=5:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[5]<=33:
                  # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[6]>7:
                     return 'liver'
                  elif obj[6]<=7:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 33, "metric_value": 0.0, "depth": 5}
               if obj[8]<=48:
                  # {"feature": "Total_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=71.38709677419355:
                     return 'liver'
                  elif obj[1]>71.38709677419355:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=412:
                        # {"feature": "Total_Protiens", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[6]>56:
                           return 'liver'
                        elif obj[6]<=56:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>412:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>48:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]>2:
                     return 'normal'
                  elif obj[1]<=2:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
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
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Alkaline_Phosphotase", "instances": 123, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 94, "metric_value": 0.0, "depth": 5}
               if obj[5]>11:
                  # {"feature": "Total_Protiens", "instances": 93, "metric_value": 0.0, "depth": 6}
                  if obj[6]<=83.23459626624852:
                     # {"feature": "Direct_Bilirubin", "instances": 89, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 77, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[4]>22:
                           return 'liver'
                        elif obj[4]<=22:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]>83.23459626624852:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=11:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 29, "metric_value": 0.0, "depth": 5}
               if obj[5]>21:
                  # {"feature": "Direct_Bilirubin", "instances": 28, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=17:
                     # {"feature": "Alamine_Aminotransferase", "instances": 26, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=102:
                        # {"feature": "Total_Protiens", "instances": 20, "metric_value": -0.0, "depth": 8}
                        if obj[6]>69:
                           return 'liver'
                        elif obj[6]<=69:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>102:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>17:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=21:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Alkaline_Phosphotase", "instances": 31, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": 0.0, "depth": 5}
               if obj[4]<=30:
                  # {"feature": "Total_Protiens", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[6]>68:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[5]>29:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[1]>9:
                           return 'liver'
                        elif obj[1]<=9:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=29:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'normal'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[6]<=68:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>30:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[5]>24:
                     # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=7:
                           return 'liver'
                        elif obj[2]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=24:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Protiens", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[6]<=75:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 6}
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
               elif obj[6]>75:
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
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Alamine_Aminotransferase", "instances": 70, "metric_value": 0.0, "depth": 4}
            if obj[4]<=187.23066243768298:
               # {"feature": "Total_Protiens", "instances": 66, "metric_value": 0.0, "depth": 5}
               if obj[6]>44.833333333333336:
                  # {"feature": "Total_Bilirubin", "instances": 44, "metric_value": 0.0, "depth": 6}
                  if obj[1]>6:
                     # {"feature": "Direct_Bilirubin", "instances": 36, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=7:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 25, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=13:
                           return 'liver'
                        elif obj[8]>13:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>7:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=6:
                           return 'liver'
                        elif obj[8]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=6:
                     # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>16:
                           return 'normal'
                        elif obj[5]<=16:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>1:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=9:
                           return 'normal'
                        elif obj[8]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[6]<=44.833333333333336:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=76:
                     # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>76:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[4]>187.23066243768298:
               return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 25, "metric_value": 0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Total_Bilirubin", "instances": 20, "metric_value": -0.0, "depth": 5}
               if obj[1]>18:
                  # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[4]>41:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[2]>12:
                        return 'liver'
                     elif obj[2]<=12:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=57:
                           return 'normal'
                        elif obj[5]>57:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[4]<=41:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[5]>22:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>11:
                           return 'liver'
                        elif obj[2]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=22:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=18:
                  # {"feature": "Total_Protiens", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[6]>53:
                     return 'liver'
                  elif obj[6]<=53:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>10:
                        return 'liver'
                     elif obj[4]<=10:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Total_Protiens", "instances": 5, "metric_value": 0.0, "depth": 5}
               if obj[6]>6:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 6}
                  if obj[2]>2:
                     return 'liver'
                  elif obj[2]<=2:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[6]<=6:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=15:
                     return 'normal'
                  elif obj[1]>15:
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
