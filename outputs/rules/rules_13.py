def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Aspartate_Aminotransferase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[5]<=63.19078947368421:
            # {"feature": "Alkaline_Phosphotase", "instances": 112, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Protiens", "instances": 94, "metric_value": 0.0, "depth": 5}
               if obj[6]<=80.86116992413325:
                  # {"feature": "Direct_Bilirubin", "instances": 87, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 58, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=27.603448275862068:
                        # {"feature": "Total_Bilirubin", "instances": 38, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>27.603448275862068:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 20, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=87:
                           return 'liver'
                        elif obj[8]>87:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Total_Bilirubin", "instances": 29, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=11:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 17, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'liver'
                        elif obj[8]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>11:
                        # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=32:
                           return 'liver'
                        elif obj[4]>32:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]>80.86116992413325:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>18:
                        return 'liver'
                     elif obj[4]<=18:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]>1:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
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
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[1]<=228:
                  # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 6}
                  if obj[2]>2:
                     return 'liver'
                  elif obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>20:
                        # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[6]>71:
                           return 'liver'
                        elif obj[6]<=71:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=20:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>228:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[5]>63.19078947368421:
            # {"feature": "Alkaline_Phosphotase", "instances": 40, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Protiens", "instances": 23, "metric_value": 0.0, "depth": 5}
               if obj[6]<=75:
                  # {"feature": "Direct_Bilirubin", "instances": 20, "metric_value": -0.0, "depth": 6}
                  if obj[2]>9:
                     return 'liver'
                  elif obj[2]<=9:
                     # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[1]>9:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[8]>13:
                           return 'liver'
                        elif obj[8]<=13:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=9:
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
               elif obj[6]>75:
                  # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[4]>42:
                     return 'liver'
                  elif obj[4]<=42:
                     return 'normal'
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
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 81, "metric_value": -0.0, "depth": 4}
            if obj[6]>47.123456790123456:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 54, "metric_value": 0.0, "depth": 5}
               if obj[8]<=11:
                  # {"feature": "Direct_Bilirubin", "instances": 47, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=16.95744680851064:
                     # {"feature": "Alamine_Aminotransferase", "instances": 36, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=39.6972866123711:
                        # {"feature": "Total_Bilirubin", "instances": 27, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=24:
                           return 'liver'
                        elif obj[1]>24:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>39.6972866123711:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]>16.95744680851064:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>11:
                  # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=6:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>18:
                           return 'liver'
                        elif obj[4]<=18:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>6:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=47.123456790123456:
               # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[5]>30:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=41:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=45:
                           return 'liver'
                        elif obj[8]>45:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>41:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=30:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=25:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[8]>1:
                           return 'liver'
                        elif obj[8]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>25:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'liver'
                        elif obj[8]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[5]>23:
                     return 'liver'
                  elif obj[5]<=23:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 37, "metric_value": -0.0, "depth": 4}
            if obj[8]<=6:
               # {"feature": "Direct_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[2]<=36:
                  # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": -0.0, "depth": 6}
                  if obj[4]>43:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=47:
                        return 'liver'
                     elif obj[1]>47:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=64:
                           return 'normal'
                        elif obj[5]>64:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[4]<=43:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>36:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[8]>6:
               # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 5}
               if obj[1]<=58:
                  # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[2]>5:
                     return 'liver'
                  elif obj[2]<=5:
                     # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[6]<=57:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>16:
                           return 'normal'
                        elif obj[4]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>57:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=17:
                           return 'liver'
                        elif obj[4]>17:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[1]>58:
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
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 116, "metric_value": 0.0, "depth": 4}
            if obj[8]<=152.65271437127222:
               # {"feature": "Total_Protiens", "instances": 113, "metric_value": 0.0, "depth": 5}
               if obj[6]>60.07079646017699:
                  # {"feature": "Total_Bilirubin", "instances": 83, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=21.83132530120482:
                     # {"feature": "Direct_Bilirubin", "instances": 71, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=5:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 63, "metric_value": -0.0, "depth": 8}
                        if obj[5]>11:
                           return 'normal'
                        elif obj[5]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>5:
                        # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[4]>22:
                           return 'liver'
                        elif obj[4]<=22:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>21.83132530120482:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[4]>11:
                        return 'liver'
                     elif obj[4]<=11:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]<=60.07079646017699:
                  # {"feature": "Total_Bilirubin", "instances": 30, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=159:
                     # {"feature": "Alamine_Aminotransferase", "instances": 29, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=279.55172413793105:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 8}
                        if obj[5]>26:
                           return 'liver'
                        elif obj[5]<=26:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>279.55172413793105:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>159:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>152.65271437127222:
               # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 5}
               if obj[4]>36:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=1:
                     return 'normal'
                  elif obj[1]>1:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=36:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Alamine_Aminotransferase", "instances": 29, "metric_value": -0.0, "depth": 5}
               if obj[4]>55:
                  # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[1]>1:
                     # {"feature": "Total_Protiens", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=78:
                        # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>78:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=55:
                  # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Total_Protiens", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[6]>71:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'liver'
                        elif obj[2]>1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=71:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>8:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]>21:
                        # {"feature": "Total_Protiens", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[6]>69:
                           return 'liver'
                        elif obj[6]<=69:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=21:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[1]<=9:
                  # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]>62:
                           return 'normal'
                        elif obj[6]<=62:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[1]>9:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]>119:
                        return 'liver'
                     elif obj[4]<=119:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>6:
                     return 'liver'
                  else:
                     return 'liver'
               else:
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
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 51, "metric_value": 0.0, "depth": 5}
               if obj[8]>7:
                  # {"feature": "Total_Bilirubin", "instances": 32, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=11:
                     # {"feature": "Direct_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 19, "metric_value": 0.0, "depth": 8}
                        if obj[4]>11:
                           return 'liver'
                        elif obj[4]<=11:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[5]>17:
                           return 'liver'
                        elif obj[5]<=17:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>11:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[5]>22:
                        return 'liver'
                     elif obj[5]<=22:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]<=7:
                  # {"feature": "Alamine_Aminotransferase", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=65:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=56:
                        # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'normal'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>56:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[2]>23:
                           return 'liver'
                        elif obj[2]<=23:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]>65:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
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
            elif obj[6]<=19.155279749709432:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": -0.0, "depth": 5}
               if obj[8]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[1]>8:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=8:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[5]>23:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=14:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>29:
                           return 'liver'
                        elif obj[4]<=29:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>14:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=23:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 25, "metric_value": 0.0, "depth": 4}
            if obj[6]>7:
               # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 5}
               if obj[1]>23:
                  # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[4]>25:
                     # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 7}
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
                  elif obj[4]<=25:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[1]<=23:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[8]>7:
                     return 'liver'
                  elif obj[8]<=7:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>30:
                           return 'liver'
                        elif obj[4]<=30:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>2:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=7:
               # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[2]>4:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=13:
                     return 'normal'
                  elif obj[1]>13:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=4:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=12:
                     return 'liver'
                  elif obj[1]>12:
                     return 'normal'
                  else:
                     return 'normal'
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
