def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Aspartate_Aminotransferase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[5]<=63.19078947368421:
            # {"feature": "Total_Protiens", "instances": 112, "metric_value": 0.0, "depth": 4}
            if obj[6]<=80.96417119446889:
               # {"feature": "Alamine_Aminotransferase", "instances": 104, "metric_value": 0.0, "depth": 5}
               if obj[4]<=30.048076923076923:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 65, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=12:
                     # {"feature": "Direct_Bilirubin", "instances": 47, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 37, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'liver'
                        elif obj[1]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[8]>12:
                     # {"feature": "Alkaline_Phosphotase", "instances": 18, "metric_value": -0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>30.048076923076923:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 39, "metric_value": -0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Direct_Bilirubin", "instances": 30, "metric_value": -0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[1]>12:
                           return 'liver'
                        elif obj[1]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=2:
                        # {"feature": "Alkaline_Phosphotase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]>80.96417119446889:
               # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[4]>18:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=1:
                     return 'liver'
                  elif obj[8]>1:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=18:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[5]>63.19078947368421:
            # {"feature": "Alkaline_Phosphotase", "instances": 40, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": 0.0, "depth": 5}
               if obj[1]>1:
                  # {"feature": "Total_Protiens", "instances": 22, "metric_value": 0.0, "depth": 6}
                  if obj[6]<=75:
                     # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[2]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[4]>22:
                           return 'liver'
                        elif obj[4]<=22:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[4]>17:
                           return 'liver'
                        elif obj[4]<=17:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]>75:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>42:
                        return 'liver'
                     elif obj[4]<=42:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]<=1:
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
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[6]>23.646973828484313:
               # {"feature": "Direct_Bilirubin", "instances": 64, "metric_value": -0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 57, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=39.87719298245614:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 38, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=45:
                        # {"feature": "Total_Bilirubin", "instances": 34, "metric_value": -0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>45:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>28:
                           return 'liver'
                        elif obj[5]<=28:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]>39.87719298245614:
                     # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=33:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>33:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[1]>4:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=5:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=20:
                           return 'liver'
                        elif obj[4]>20:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>5:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>20:
                           return 'normal'
                        elif obj[4]<=20:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=4:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=23.646973828484313:
               # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 5}
               if obj[5]>23:
                  # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=33:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=13:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=7:
                           return 'liver'
                        elif obj[8]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>13:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>33:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=23:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=1:
                     return 'liver'
                  elif obj[8]>1:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[2]<=29.27027027027027:
               # {"feature": "Total_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[1]>5:
                  # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=412:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 20, "metric_value": -0.0, "depth": 7}
                     if obj[5]>54:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[8]>5:
                           return 'liver'
                        elif obj[8]<=5:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=54:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>412:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=5:
                  # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[4]>20:
                     return 'liver'
                  elif obj[4]<=20:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[2]>29.27027027027027:
               # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 5}
               if obj[1]>109:
                  return 'liver'
               elif obj[1]<=109:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>48:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=64:
                           return 'normal'
                        elif obj[5]>64:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=48:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>6:
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
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Bilirubin", "instances": 116, "metric_value": 0.0, "depth": 4}
            if obj[1]>1:
               # {"feature": "Direct_Bilirubin", "instances": 107, "metric_value": -0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 92, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=26.945652173913043:
                     # {"feature": "Total_Protiens", "instances": 76, "metric_value": 0.0, "depth": 7}
                     if obj[6]>60.9078947368421:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 56, "metric_value": 0.0, "depth": 8}
                        if obj[5]>11:
                           return 'liver'
                        elif obj[5]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=60.9078947368421:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 20, "metric_value": -0.0, "depth": 8}
                        if obj[5]>25:
                           return 'liver'
                        elif obj[5]<=25:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[8]>26.945652173913043:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 7}
                     if obj[5]>23:
                        # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[4]>18:
                           return 'liver'
                        elif obj[4]<=18:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=23:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=14:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=33:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[4]>32:
                           return 'liver'
                        elif obj[4]<=32:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>33:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>18:
                           return 'normal'
                        elif obj[4]<=18:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>14:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>28:
                        return 'liver'
                     elif obj[4]<=28:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[1]<=1:
               # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[5]<=31:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=13:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'normal'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[8]>13:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        return 'normal'
                     elif obj[2]<=2:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[5]>31:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=3:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=41:
                           return 'liver'
                        elif obj[4]>41:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'normal'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 38, "metric_value": -0.0, "depth": 4}
            if obj[2]<=3:
               # {"feature": "Alamine_Aminotransferase", "instances": 26, "metric_value": -0.0, "depth": 5}
               if obj[4]<=70:
                  # {"feature": "Total_Protiens", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[6]<=75:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=58:
                        # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'normal'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>58:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]>75:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=40:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>40:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>5:
                           return 'liver'
                        elif obj[1]<=5:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[4]>70:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=141:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=1:
                        return 'liver'
                     elif obj[1]>1:
                        # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=78:
                           return 'liver'
                        elif obj[6]>78:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>141:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[8]>8:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'normal'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=8:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]>3:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 12, "metric_value": -0.0, "depth": 5}
               if obj[8]>7:
                  return 'liver'
               elif obj[8]<=7:
                  # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[4]>28:
                     return 'liver'
                  elif obj[4]<=28:
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
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[6]>44.49473684210526:
            # {"feature": "Alkaline_Phosphotase", "instances": 63, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 46, "metric_value": -0.0, "depth": 5}
               if obj[4]<=53.91304347826087:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 30, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=9:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=38:
                        # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'normal'
                        elif obj[1]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>38:
                        # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[1]>16:
                           return 'liver'
                        elif obj[1]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>9:
                     # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=6:
                           return 'normal'
                        elif obj[2]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>53.91304347826087:
                  # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[1]>2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[5]>33:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=12:
                           return 'liver'
                        elif obj[8]>12:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=33:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=2:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 5}
               if obj[5]>24:
                  # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=15:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[4]>37:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[1]>8:
                           return 'normal'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=37:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>15:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[4]>50:
                        return 'liver'
                     elif obj[4]<=50:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>25:
                           return 'normal'
                        elif obj[1]<=25:
                           return 'liver'
                        else:
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
         elif obj[6]<=44.49473684210526:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 32, "metric_value": 0.0, "depth": 4}
            if obj[8]<=5:
               # {"feature": "Direct_Bilirubin", "instances": 20, "metric_value": -0.0, "depth": 5}
               if obj[2]<=4:
                  # {"feature": "Alkaline_Phosphotase", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[4]>26:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]>28:
                           return 'liver'
                        elif obj[5]<=28:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=26:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=23:
                           return 'liver'
                        elif obj[5]>23:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>34:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>9:
                           return 'normal'
                        elif obj[1]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=34:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[2]>4:
                  # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[1]>13:
                     # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[5]>19:
                           return 'normal'
                        elif obj[5]<=19:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[3]>291.0539499036609:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=13:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>5:
               # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 5}
               if obj[4]<=25:
                  # {"feature": "Alkaline_Phosphotase", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>25:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
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
      else:
         return 'liver'
   else:
      return 'liver'
