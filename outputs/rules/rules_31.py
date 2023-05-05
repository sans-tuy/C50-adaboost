def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alamine_Aminotransferase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[4]<=50.125:
            # {"feature": "Total_Protiens", "instances": 108, "metric_value": 0.0, "depth": 4}
            if obj[6]>21.451500197501467:
               # {"feature": "Alkaline_Phosphotase", "instances": 97, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 83, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=62.547435619650585:
                     # {"feature": "Total_Bilirubin", "instances": 78, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 47, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=7:
                           return 'liver'
                        elif obj[2]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 31, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=11:
                           return 'liver'
                        elif obj[8]>11:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>62.547435619650585:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        return 'liver'
                     elif obj[2]<=2:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=226:
                     # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=16:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=32:
                           return 'liver'
                        elif obj[5]>32:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>16:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>226:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=21.451500197501467:
               # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Alkaline_Phosphotase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]>14:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=14:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>2:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[5]>25:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=12:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>12:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=25:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[4]>50.125:
            # {"feature": "Alkaline_Phosphotase", "instances": 44, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 24, "metric_value": -0.0, "depth": 5}
               if obj[1]<=23:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=116:
                     # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=6:
                        # {"feature": "Total_Protiens", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[6]>61:
                           return 'liver'
                        elif obj[6]<=61:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>6:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=84:
                           return 'normal'
                        elif obj[5]>84:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>116:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[1]>23:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": -0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[8]<=16:
               # {"feature": "Total_Protiens", "instances": 73, "metric_value": -0.0, "depth": 5}
               if obj[6]>48.42465753424658:
                  # {"feature": "Alamine_Aminotransferase", "instances": 48, "metric_value": 0.0, "depth": 6}
                  if obj[4]>10:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 47, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=74.51063829787235:
                        # {"feature": "Total_Bilirubin", "instances": 34, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>74.51063829787235:
                        # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=184:
                           return 'liver'
                        elif obj[1]>184:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=10:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[6]<=48.42465753424658:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 25, "metric_value": 0.0, "depth": 6}
                  if obj[5]>20:
                     # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=58:
                        # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 8}
                        if obj[4]>26:
                           return 'liver'
                        elif obj[4]<=26:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>58:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=20:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>16:
               # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[5]>28:
                  # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[2]>2:
                     return 'liver'
                  elif obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>21:
                        return 'liver'
                     elif obj[4]<=21:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[5]<=28:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Aspartate_Aminotransferase", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[5]<=310.7837837837838:
               # {"feature": "Direct_Bilirubin", "instances": 28, "metric_value": -0.0, "depth": 5}
               if obj[2]>3:
                  # {"feature": "Total_Protiens", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[6]>6:
                     # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[1]>14:
                        # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=48:
                           return 'liver'
                        elif obj[4]>48:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=14:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=6:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=3:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=24:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[4]>17:
                        # {"feature": "Total_Protiens", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[6]<=52:
                           return 'liver'
                        elif obj[6]>52:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=17:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>24:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[5]>310.7837837837838:
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
         # {"feature": "Total_Protiens", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[6]>63.0:
            # {"feature": "Alkaline_Phosphotase", "instances": 110, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 78, "metric_value": 0.0, "depth": 5}
               if obj[5]>11:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 77, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=31.31168831168831:
                     # {"feature": "Total_Bilirubin", "instances": 63, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=11:
                        # {"feature": "Direct_Bilirubin", "instances": 49, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'normal'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>11:
                        # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[2]>6:
                           return 'liver'
                        elif obj[2]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>31.31168831168831:
                     # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[4]>18:
                        # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=71:
                           return 'liver'
                        elif obj[1]>71:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=18:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[5]<=11:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 32, "metric_value": 0.0, "depth": 5}
               if obj[5]<=193.15625:
                  # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=22:
                     # {"feature": "Direct_Bilirubin", "instances": 20, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 14, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=13:
                           return 'liver'
                        elif obj[8]>13:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'liver'
                        elif obj[8]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>22:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=1:
                        return 'liver'
                     elif obj[2]>1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[5]>193.15625:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=8:
                     return 'liver'
                  elif obj[8]>8:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=17:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=152:
                           return 'liver'
                        elif obj[4]>152:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>17:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=63.0:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 44, "metric_value": 0.0, "depth": 4}
            if obj[8]<=11:
               # {"feature": "Alkaline_Phosphotase", "instances": 31, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 26, "metric_value": 0.0, "depth": 6}
                  if obj[1]>6:
                     # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[4]>14:
                           return 'liver'
                        elif obj[4]<=14:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=6:
                     # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>41:
                           return 'liver'
                        elif obj[5]<=41:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
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
                  # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=9:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        return 'liver'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>9:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>11:
               # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[4]>25:
                     return 'liver'
                  elif obj[4]<=25:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>23:
                        return 'liver'
                     elif obj[5]<=23:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
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
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[6]>19.418485261141242:
            # {"feature": "Alkaline_Phosphotase", "instances": 69, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 51, "metric_value": -0.0, "depth": 5}
               if obj[4]<=98.8470650757233:
                  # {"feature": "Total_Bilirubin", "instances": 45, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Direct_Bilirubin", "instances": 26, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 20, "metric_value": 0.0, "depth": 8}
                        if obj[5]>13:
                           return 'liver'
                        elif obj[5]<=13:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]>16:
                           return 'normal'
                        elif obj[5]<=16:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>8:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=9:
                        # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>9:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[5]>30:
                           return 'normal'
                        elif obj[5]<=30:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[4]>98.8470650757233:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[5]>24:
                  # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=50:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=8:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[1]>28:
                           return 'liver'
                        elif obj[1]<=28:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>50:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[2]>12:
                           return 'liver'
                        elif obj[2]<=12:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=8:
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
            # {"feature": "Alkaline_Phosphotase", "instances": 26, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": 0.0, "depth": 5}
               if obj[8]<=7:
                  # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=4:
                     # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[4]>12:
                           return 'liver'
                        elif obj[4]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>4:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>13:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'liver'
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
               elif obj[8]>7:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 5}
               if obj[1]>9:
                  # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[2]>3:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=48:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=10:
                           return 'normal'
                        elif obj[4]>10:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>48:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=3:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=9:
                  # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=30:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 2, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=1:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": -0.0, "depth": 8}
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
