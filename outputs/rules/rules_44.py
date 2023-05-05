def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Alamine_Aminotransferase", "instances": 122, "metric_value": 0.0, "depth": 4}
            if obj[4]<=50.78688524590164:
               # {"feature": "Aspartate_Aminotransferase", "instances": 85, "metric_value": 0.0, "depth": 5}
               if obj[5]<=33.04705882352941:
                  # {"feature": "Direct_Bilirubin", "instances": 55, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Total_Bilirubin", "instances": 38, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Alkaline_Phosphotase", "instances": 22, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Total_Protiens", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[6]>65:
                           return 'liver'
                        elif obj[6]<=65:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Total_Protiens", "instances": 17, "metric_value": 0.0, "depth": 7}
                     if obj[6]<=62:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=11:
                           return 'normal'
                        elif obj[1]>11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>62:
                        # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[1]>9:
                           return 'liver'
                        elif obj[1]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]>33.04705882352941:
                  # {"feature": "Total_Bilirubin", "instances": 30, "metric_value": -0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Alkaline_Phosphotase", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[3]>291.0539499036609:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=7:
                     # {"feature": "Alkaline_Phosphotase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Protiens", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[6]>5:
                           return 'liver'
                        elif obj[6]<=5:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[3]>291.0539499036609:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[4]>50.78688524590164:
               # {"feature": "Alkaline_Phosphotase", "instances": 37, "metric_value": -0.0, "depth": 5}
               if obj[3]>291.0539499036609:
                  return 'liver'
               elif obj[3]<=291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[5]>57:
                     # {"feature": "Total_Protiens", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=67:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=58:
                           return 'liver'
                        elif obj[1]>58:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>67:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=57:
                     # {"feature": "Total_Protiens", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[6]>6:
                        return 'liver'
                     elif obj[6]<=6:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Total_Protiens", "instances": 30, "metric_value": 0.0, "depth": 4}
            if obj[6]>63:
               # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 5}
               if obj[1]>7:
                  return 'liver'
               elif obj[1]<=7:
                  # {"feature": "Alkaline_Phosphotase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[5]>17:
                        # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[4]>24:
                           return 'liver'
                        elif obj[4]<=24:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=17:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=63:
               # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 5}
               if obj[4]>14:
                  # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=1:
                        return 'liver'
                     elif obj[2]>1:
                        # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        elif obj[3]>291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[1]>8:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=14:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": -0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[6]>47.123456790123456:
               # {"feature": "Total_Bilirubin", "instances": 54, "metric_value": -0.0, "depth": 5}
               if obj[1]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 50, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=41.54:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 35, "metric_value": 0.0, "depth": 7}
                     if obj[5]>12:
                        # {"feature": "Direct_Bilirubin", "instances": 34, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=12:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>41.54:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[5]>39:
                           return 'liver'
                        elif obj[5]<=39:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
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
               elif obj[1]<=1:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=3:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[5]>13:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'normal'
                        elif obj[8]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=13:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[6]<=47.123456790123456:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 27, "metric_value": 0.0, "depth": 5}
               if obj[8]<=52:
                  # {"feature": "Direct_Bilirubin", "instances": 25, "metric_value": -0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=58:
                           return 'liver'
                        elif obj[1]>58:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=25:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=32:
                           return 'liver'
                        elif obj[5]>32:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]>23:
                        return 'liver'
                     elif obj[5]<=23:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]>52:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 37, "metric_value": -0.0, "depth": 4}
            if obj[8]<=6:
               # {"feature": "Alamine_Aminotransferase", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[4]<=161.58333333333334:
                  # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=13:
                     return 'liver'
                  elif obj[2]>13:
                     # {"feature": "Total_Protiens", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=61:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>11:
                           return 'liver'
                        elif obj[1]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>61:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>161.58333333333334:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[8]>6:
               # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 5}
               if obj[1]>11:
                  # {"feature": "Total_Protiens", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[6]>7:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=32:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=181:
                           return 'normal'
                        elif obj[4]>181:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>32:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=7:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=11:
                  # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 6}
                  if obj[2]>5:
                     return 'liver'
                  elif obj[2]<=5:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]>16:
                        return 'normal'
                     elif obj[4]<=16:
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
         # {"feature": "Alkaline_Phosphotase", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 116, "metric_value": 0.0, "depth": 4}
            if obj[8]<=26.155172413793103:
               # {"feature": "Total_Protiens", "instances": 98, "metric_value": -0.0, "depth": 5}
               if obj[6]>9.38418129641012:
                  # {"feature": "Total_Bilirubin", "instances": 82, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=136.50149418271735:
                     # {"feature": "Direct_Bilirubin", "instances": 78, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=25:
                        # {"feature": "Alamine_Aminotransferase", "instances": 75, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=70.37333333333333:
                           return 'liver'
                        elif obj[4]>70.37333333333333:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>25:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>136.50149418271735:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=9.38418129641012:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=34:
                     # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>15:
                           return 'liver'
                        elif obj[4]<=15:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=16:
                           return 'normal'
                        elif obj[4]>16:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[5]>34:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        return 'liver'
                     elif obj[1]<=6:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'normal'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>26.155172413793103:
               # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": -0.0, "depth": 5}
               if obj[4]>15:
                  # {"feature": "Total_Protiens", "instances": 17, "metric_value": -0.0, "depth": 6}
                  if obj[6]>68:
                     # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=19:
                        # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>19:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=68:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]>23:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=23:
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
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 38, "metric_value": -0.0, "depth": 4}
            if obj[6]<=76:
               # {"feature": "Aspartate_Aminotransferase", "instances": 28, "metric_value": -0.0, "depth": 5}
               if obj[5]<=207.64285714285714:
                  # {"feature": "Alamine_Aminotransferase", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[4]>28:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[8]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=28:
                     # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>2:
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
               elif obj[5]>207.64285714285714:
                  # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[4]>102:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        return 'liver'
                     elif obj[1]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[4]<=102:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]>76:
               # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 5}
               if obj[5]>24:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=5:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>5:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[8]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=22:
                        return 'normal'
                     elif obj[1]>22:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[5]<=24:
                  # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[1]>9:
                     return 'liver'
                  elif obj[1]<=9:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        return 'normal'
                     elif obj[2]<=2:
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
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[6]>19.418485261141242:
            # {"feature": "Alkaline_Phosphotase", "instances": 69, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 51, "metric_value": 0.0, "depth": 5}
               if obj[8]<=64:
                  # {"feature": "Direct_Bilirubin", "instances": 45, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 27, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=45.74074074074074:
                        # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>45.74074074074074:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 7}
                     if obj[1]>16:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[5]>87:
                           return 'liver'
                        elif obj[5]<=87:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=16:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>22:
                           return 'liver'
                        elif obj[5]<=22:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>64:
                  # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[5]>28:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'normal'
                        elif obj[1]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=28:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]<=12:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
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
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[2]<=82:
                  # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[4]>29:
                     # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[1]>18:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=57:
                           return 'normal'
                        elif obj[5]>57:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=18:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=29:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[8]>6:
                        return 'liver'
                     elif obj[8]<=6:
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
         elif obj[6]<=19.418485261141242:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 26, "metric_value": 0.0, "depth": 4}
            if obj[8]<=5:
               # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 5}
               if obj[2]<=4:
                  # {"feature": "Alkaline_Phosphotase", "instances": 13, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[5]>23:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=38:
                           return 'normal'
                        elif obj[4]>38:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=23:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=30:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[2]>4:
                  # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=25:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>20:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=13:
                           return 'normal'
                        elif obj[1]>13:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=20:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>25:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>48:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>16:
                           return 'liver'
                        elif obj[1]<=16:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=48:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            elif obj[8]>5:
               # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
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
               elif obj[3]>291.0539499036609:
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
