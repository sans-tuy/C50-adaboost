def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Aspartate_Aminotransferase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[5]<=63.19078947368421:
            # {"feature": "Direct_Bilirubin", "instances": 112, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Alkaline_Phosphotase", "instances": 98, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 81, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=29.185185185185187:
                     # {"feature": "Total_Protiens", "instances": 47, "metric_value": 0.0, "depth": 7}
                     if obj[6]>62.234042553191486:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 33, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=11:
                           return 'liver'
                        elif obj[8]>11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=62.234042553191486:
                        # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=11:
                           return 'normal'
                        elif obj[1]>11:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>29.185185185185187:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 34, "metric_value": -0.0, "depth": 7}
                     if obj[8]>9:
                        # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=9:
                        # {"feature": "Total_Protiens", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[6]>54:
                           return 'liver'
                        elif obj[6]<=54:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 17, "metric_value": 0.0, "depth": 6}
                  if obj[1]>9:
                     return 'liver'
                  elif obj[1]<=9:
                     # {"feature": "Total_Protiens", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[6]>62:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>24:
                           return 'liver'
                        elif obj[4]<=24:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=62:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 5}
               if obj[4]>17:
                  # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=6:
                     # {"feature": "Alkaline_Phosphotase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'normal'
                        elif obj[8]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>6:
                     # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=8:
                           return 'liver'
                        elif obj[8]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[3]>291.0539499036609:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=17:
                  # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=7:
                        # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=54:
                           return 'normal'
                        elif obj[6]>54:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>7:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[5]>63.19078947368421:
            # {"feature": "Total_Protiens", "instances": 40, "metric_value": 0.0, "depth": 4}
            if obj[6]>59.575:
               # {"feature": "Alkaline_Phosphotase", "instances": 32, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=57:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 17, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=14:
                        # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[4]>33:
                           return 'liver'
                        elif obj[4]<=33:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>14:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>57:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=59.575:
               # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[4]>58:
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
               elif obj[4]<=58:
                  # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
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
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[8]<=9:
               # {"feature": "Alamine_Aminotransferase", "instances": 63, "metric_value": -0.0, "depth": 5}
               if obj[4]<=38.6031746031746:
                  # {"feature": "Total_Protiens", "instances": 39, "metric_value": 0.0, "depth": 6}
                  if obj[6]>49.05128205128205:
                     # {"feature": "Total_Bilirubin", "instances": 25, "metric_value": -0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Direct_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=9:
                           return 'liver'
                        elif obj[2]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]<=49.05128205128205:
                     # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>38.6031746031746:
                  # {"feature": "Total_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 6}
                  if obj[1]>4:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=113.6086956521739:
                        # {"feature": "Total_Protiens", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[6]>7:
                           return 'liver'
                        elif obj[6]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>113.6086956521739:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=4:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>9:
               # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[2]>2:
                  # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[4]>18:
                     # {"feature": "Total_Protiens", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[6]>58:
                        return 'liver'
                     elif obj[6]<=58:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=18:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=2:
                  # {"feature": "Total_Protiens", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[6]>7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=24:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>16:
                           return 'liver'
                        elif obj[5]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>24:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[1]>4:
                           return 'normal'
                        elif obj[1]<=4:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[6]<=7:
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
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 37, "metric_value": -0.0, "depth": 4}
            if obj[2]<=91.43074028249146:
               # {"feature": "Total_Bilirubin", "instances": 35, "metric_value": -0.0, "depth": 5}
               if obj[1]>2:
                  # {"feature": "Total_Protiens", "instances": 34, "metric_value": -0.0, "depth": 6}
                  if obj[6]>48.73529411764706:
                     # {"feature": "Alamine_Aminotransferase", "instances": 23, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=350.2353973733905:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 21, "metric_value": -0.0, "depth": 8}
                        if obj[8]>4:
                           return 'liver'
                        elif obj[8]<=4:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>350.2353973733905:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=48.73529411764706:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=2:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[2]>91.43074028249146:
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
               # {"feature": "Aspartate_Aminotransferase", "instances": 86, "metric_value": 0.0, "depth": 5}
               if obj[5]>11:
                  # {"feature": "Total_Bilirubin", "instances": 85, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=112.43072542875957:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 82, "metric_value": 0.0, "depth": 7}
                     if obj[8]>1:
                        # {"feature": "Direct_Bilirubin", "instances": 65, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=5:
                           return 'normal'
                        elif obj[2]>5:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'normal'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>112.43072542875957:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=11:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=60.3448275862069:
               # {"feature": "Total_Bilirubin", "instances": 30, "metric_value": 0.0, "depth": 5}
               if obj[1]>6:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 20, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=11:
                     # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[5]>20:
                           return 'liver'
                        elif obj[5]<=20:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>11:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        return 'liver'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]<=6:
                  # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[8]>9:
                           return 'liver'
                        elif obj[8]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        return 'normal'
                     elif obj[4]<=25:
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
            # {"feature": "Total_Protiens", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[6]<=82:
               # {"feature": "Alamine_Aminotransferase", "instances": 36, "metric_value": -0.0, "depth": 5}
               if obj[4]<=137.69444444444446:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 25, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=89.28:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[8]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]>89.28:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>137.69444444444446:
                  # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[1]>1:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=8:
                        return 'liver'
                     elif obj[8]>8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>231:
                           return 'liver'
                        elif obj[5]<=231:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]>82:
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
               # {"feature": "Alamine_Aminotransferase", "instances": 51, "metric_value": -0.0, "depth": 5}
               if obj[4]<=50.88235294117647:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 34, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=71:
                     # {"feature": "Total_Bilirubin", "instances": 30, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 19, "metric_value": -0.0, "depth": 8}
                        if obj[5]>38:
                           return 'liver'
                        elif obj[5]<=38:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]>71:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        return 'normal'
                     elif obj[1]<=6:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[4]>50.88235294117647:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 6}
                  if obj[5]>33:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 16, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=8:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=33:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[6]<=19.155279749709432:
               # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 5}
               if obj[2]<=4:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[5]>21:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[4]>26:
                           return 'liver'
                        elif obj[4]<=26:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>21:
                           return 'normal'
                        elif obj[4]<=21:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=21:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>4:
                  # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[1]>13:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]>74:
                           return 'liver'
                        elif obj[5]<=74:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=25:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=13:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 25, "metric_value": 0.0, "depth": 4}
            if obj[6]>7:
               # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 5}
               if obj[1]>9:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=76:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[2]>11:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[4]>28:
                           return 'normal'
                        elif obj[4]<=28:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=11:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>76:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=9:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[8]>1:
                     return 'liver'
                  elif obj[8]<=1:
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
               else:
                  return 'liver'
            elif obj[6]<=7:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[8]>1:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]>12:
                     return 'normal'
                  elif obj[1]<=12:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=1:
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
               return 'normal'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
