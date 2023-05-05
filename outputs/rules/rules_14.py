def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Aspartate_Aminotransferase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[5]<=63.19078947368421:
            # {"feature": "Alkaline_Phosphotase", "instances": 112, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 94, "metric_value": -0.0, "depth": 5}
               if obj[2]<=5:
                  # {"feature": "Total_Bilirubin", "instances": 83, "metric_value": -0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Total_Protiens", "instances": 48, "metric_value": 0.0, "depth": 7}
                     if obj[6]>13.23832866540564:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 41, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=11:
                           return 'liver'
                        elif obj[8]>11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=13.23832866540564:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[8]>9:
                           return 'normal'
                        elif obj[8]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[1]<=7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 35, "metric_value": 0.0, "depth": 7}
                     if obj[4]>12:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 34, "metric_value": 0.0, "depth": 8}
                        if obj[8]>7:
                           return 'liver'
                        elif obj[8]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>5:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Total_Protiens", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[6]>64:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>36:
                           return 'liver'
                        elif obj[4]<=36:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=64:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=18:
                           return 'normal'
                        elif obj[4]>18:
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
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[1]<=228:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 17, "metric_value": 0.0, "depth": 6}
                  if obj[8]>8:
                     # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        return 'liver'
                     elif obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[4]>24:
                           return 'liver'
                        elif obj[4]<=24:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=8:
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
            # {"feature": "Alkaline_Phosphotase", "instances": 40, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 5}
               if obj[2]<=13:
                  # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[4]>17:
                     # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=111:
                           return 'liver'
                        elif obj[8]>111:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=17:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[2]>13:
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
            # {"feature": "Alamine_Aminotransferase", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[4]>10:
               # {"feature": "Total_Protiens", "instances": 80, "metric_value": 0.0, "depth": 5}
               if obj[6]>47.1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 53, "metric_value": 0.0, "depth": 6}
                  if obj[5]>13:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 52, "metric_value": 0.0, "depth": 7}
                     if obj[8]>1:
                        # {"feature": "Total_Bilirubin", "instances": 49, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=190.2624559499237:
                           return 'liver'
                        elif obj[1]>190.2624559499237:
                           return 'liver'
                        else:
                           return 'liver'
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
                  elif obj[5]<=13:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[6]<=47.1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 27, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=69.37037037037037:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": 0.0, "depth": 7}
                     if obj[8]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=6:
                        # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>69.37037037037037:
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
            # {"feature": "Direct_Bilirubin", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[2]<=29.27027027027027:
               # {"feature": "Total_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[1]>5:
                  # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 20, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=6:
                        return 'liver'
                     elif obj[8]>6:
                        # {"feature": "Total_Protiens", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=45:
                           return 'liver'
                        elif obj[6]>45:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=12:
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
               # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 5}
               if obj[1]>8:
                  # {"feature": "Total_Protiens", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[6]>61:
                     return 'liver'
                  elif obj[6]<=61:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=88:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[8]>6:
                           return 'liver'
                        elif obj[8]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>88:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=8:
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
            if obj[8]>1:
               # {"feature": "Total_Bilirubin", "instances": 94, "metric_value": -0.0, "depth": 5}
               if obj[1]<=25.904255319148938:
                  # {"feature": "Total_Protiens", "instances": 75, "metric_value": 0.0, "depth": 6}
                  if obj[6]>61.22666666666667:
                     # {"feature": "Direct_Bilirubin", "instances": 56, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 51, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=92.79906514933245:
                           return 'normal'
                        elif obj[4]>92.79906514933245:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>6:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=61.22666666666667:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 19, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=41:
                        # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>41:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=54:
                           return 'liver'
                        elif obj[4]>54:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>25.904255319148938:
                  # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=37:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[5]>180:
                        return 'liver'
                     elif obj[5]<=180:
                        # {"feature": "Total_Protiens", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[6]>7:
                           return 'liver'
                        elif obj[6]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>37:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Total_Protiens", "instances": 22, "metric_value": 0.0, "depth": 5}
               if obj[6]>7:
                  # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[4]>27:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=27:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=22:
                           return 'liver'
                        elif obj[5]>22:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>8:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[5]>24:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[4]>26:
                           return 'liver'
                        elif obj[4]<=26:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=24:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[6]<=7:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
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
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[8]<=15:
               # {"feature": "Total_Bilirubin", "instances": 35, "metric_value": -0.0, "depth": 5}
               if obj[1]<=13:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[5]>51:
                     # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=70:
                           return 'liver'
                        elif obj[4]>70:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>3:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=51:
                     # {"feature": "Total_Protiens", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[6]>72:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=28:
                           return 'normal'
                        elif obj[4]>28:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=72:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[1]>13:
                  # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=95:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=390:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[5]>24:
                           return 'liver'
                        elif obj[5]<=24:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>390:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>95:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>15:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[6]>19.418485261141242:
            # {"feature": "Direct_Bilirubin", "instances": 69, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Alkaline_Phosphotase", "instances": 59, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 41, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=15:
                     # {"feature": "Alamine_Aminotransferase", "instances": 34, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=49.64705882352941:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 22, "metric_value": 0.0, "depth": 8}
                        if obj[5]>13:
                           return 'liver'
                        elif obj[5]<=13:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>49.64705882352941:
                        # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=263:
                           return 'liver'
                        elif obj[1]>263:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>15:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[5]>18:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=22:
                           return 'liver'
                        elif obj[4]>22:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=18:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[4]>48:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[5]>57:
                           return 'liver'
                        elif obj[5]<=57:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=48:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1]>21:
                           return 'liver'
                        elif obj[1]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>9:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Alkaline_Phosphotase", "instances": 10, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=41:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'normal'
                        elif obj[1]>6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=15:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>41:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[4]>91:
                        return 'liver'
                     elif obj[4]<=91:
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
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=19.418485261141242:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 26, "metric_value": 0.0, "depth": 4}
            if obj[8]<=6:
               # {"feature": "Alkaline_Phosphotase", "instances": 20, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 6}
                  if obj[4]>15:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[5]>16:
                        # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=16:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=15:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=13:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=34:
                        return 'normal'
                     elif obj[5]>34:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>13:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]>4:
                        return 'liver'
                     elif obj[2]<=4:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            elif obj[8]>6:
               # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 5}
               if obj[4]<=25:
                  # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
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
               elif obj[4]>25:
                  # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 6}
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
