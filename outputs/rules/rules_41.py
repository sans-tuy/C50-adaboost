def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]>60.46052631578947:
            # {"feature": "Aspartate_Aminotransferase", "instances": 117, "metric_value": -0.0, "depth": 4}
            if obj[5]<=66.09401709401709:
               # {"feature": "Alkaline_Phosphotase", "instances": 87, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 71, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 67, "metric_value": 0.0, "depth": 7}
                     if obj[4]>13.333767382805435:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 64, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=11:
                           return 'liver'
                        elif obj[8]>11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=13.333767382805435:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'normal'
                        elif obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>7:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=9:
                        return 'liver'
                     elif obj[8]>9:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     return 'liver'
                  elif obj[1]<=7:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>24:
                           return 'liver'
                        elif obj[4]<=24:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]>66.09401709401709:
               # {"feature": "Alkaline_Phosphotase", "instances": 30, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[2]>8:
                     return 'liver'
                  elif obj[2]<=8:
                     # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=111:
                           return 'liver'
                        elif obj[8]>111:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>28:
                           return 'normal'
                        elif obj[4]<=28:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=60.46052631578947:
            # {"feature": "Direct_Bilirubin", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[2]>2:
               # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[1]>2:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=83:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[8]>12:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>18:
                           return 'normal'
                        elif obj[4]<=18:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=12:
                        # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[3]>291.0539499036609:
                           return 'liver'
                        elif obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>83:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]>58:
                        # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        elif obj[3]>291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=58:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=2:
                  # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=19:
                        return 'normal'
                     elif obj[4]>19:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[2]<=2:
               # {"feature": "Total_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 5}
               if obj[1]>7:
                  # {"feature": "Alkaline_Phosphotase", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=24:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[8]>9:
                           return 'normal'
                        elif obj[8]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>24:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[8]>9:
                           return 'liver'
                        elif obj[8]<=9:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[1]<=7:
                  # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[8]>8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>21:
                           return 'liver'
                        elif obj[5]<=21:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]<=8:
                        # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=12:
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
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[6]>47.123456790123456:
               # {"feature": "Alamine_Aminotransferase", "instances": 54, "metric_value": -0.0, "depth": 5}
               if obj[4]>10:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 53, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=11:
                     # {"feature": "Direct_Bilirubin", "instances": 46, "metric_value": -0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Total_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=170.01767462579187:
                           return 'liver'
                        elif obj[1]>170.01767462579187:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[8]>11:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=6:
                           return 'liver'
                        elif obj[2]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=10:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[6]<=47.123456790123456:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 27, "metric_value": 0.0, "depth": 5}
               if obj[8]<=13:
                  # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[4]>15:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[5]>23:
                        # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=23:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=15:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[8]>13:
                  # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[4]>18:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>53:
                        return 'liver'
                     elif obj[5]<=53:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]<=18:
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
               # {"feature": "Total_Bilirubin", "instances": 33, "metric_value": 0.0, "depth": 5}
               if obj[1]<=68.87878787878788:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 21, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=53:
                     return 'liver'
                  elif obj[8]>53:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[1]>68.87878787878788:
                  # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[4]>48:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=562:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[8]>4:
                           return 'liver'
                        elif obj[8]<=4:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>562:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=48:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[1]>7:
                  return 'liver'
               elif obj[1]<=7:
                  # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=20:
                     return 'normal'
                  elif obj[4]>20:
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
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Alkaline_Phosphotase", "instances": 123, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 94, "metric_value": 0.0, "depth": 5}
               if obj[5]>11:
                  # {"feature": "Total_Bilirubin", "instances": 93, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=26.086021505376344:
                     # {"feature": "Total_Protiens", "instances": 74, "metric_value": -0.0, "depth": 7}
                     if obj[6]>61.148648648648646:
                        # {"feature": "Direct_Bilirubin", "instances": 55, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=61.148648648648646:
                        # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>26.086021505376344:
                     # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[2]>13:
                        return 'liver'
                     elif obj[2]<=13:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=82:
                           return 'liver'
                        elif obj[4]>82:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=11:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 29, "metric_value": 0.0, "depth": 5}
               if obj[4]>25:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=214.2173913043478:
                     # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=16:
                        # {"feature": "Total_Protiens", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[6]>71:
                           return 'liver'
                        elif obj[6]<=71:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>16:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]>69:
                           return 'liver'
                        elif obj[6]<=69:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>214.2173913043478:
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
                  else:
                     return 'liver'
               elif obj[4]<=25:
                  # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=21:
                           return 'liver'
                        elif obj[5]>21:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>1:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Alkaline_Phosphotase", "instances": 31, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": -0.0, "depth": 5}
               if obj[1]>7:
                  # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=7:
                     # {"feature": "Total_Protiens", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[6]>62:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=29:
                           return 'liver'
                        elif obj[4]>29:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=62:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>19:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=11:
                           return 'normal'
                        elif obj[4]>11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=19:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[1]<=7:
                  # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[4]>15:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[5]>30:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=30:
                        # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[6]>64:
                           return 'liver'
                        elif obj[6]<=64:
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
               # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[5]>42:
                  # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[2]>1:
                     return 'liver'
                  elif obj[2]<=1:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[5]<=42:
                  # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=9:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>15:
                           return 'normal'
                        elif obj[4]<=15:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[1]>9:
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
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 70, "metric_value": 0.0, "depth": 4}
            if obj[8]<=46:
               # {"feature": "Total_Protiens", "instances": 63, "metric_value": -0.0, "depth": 5}
               if obj[6]>17.24408702329178:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 44, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=69.22727272727273:
                     # {"feature": "Alamine_Aminotransferase", "instances": 32, "metric_value": 0.0, "depth": 7}
                     if obj[4]>12:
                        # {"feature": "Total_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=17:
                           return 'liver'
                        elif obj[1]>17:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=12:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]>69.22727272727273:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=155:
                        # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>155:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=17.24408702329178:
                  # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=26:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]>16:
                           return 'liver'
                        elif obj[5]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>26:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[1]>8:
                     # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[2]>3:
                           return 'liver'
                        elif obj[2]<=3:
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
            elif obj[8]>46:
               # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 5}
               if obj[4]<=22:
                  # {"feature": "Total_Protiens", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[6]>55:
                     return 'liver'
                  elif obj[6]<=55:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[4]>22:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[5]>28:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
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
               else:
                  return 'normal'
            else:
               return 'normal'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 25, "metric_value": 0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Direct_Bilirubin", "instances": 20, "metric_value": 0.0, "depth": 5}
               if obj[2]<=13:
                  # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=48:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=39:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[1]>12:
                           return 'liver'
                        elif obj[1]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>39:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>48:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[5]>17:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=56:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=17:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[2]>13:
                  # {"feature": "Total_Protiens", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[6]<=61:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        return 'liver'
                     elif obj[4]<=25:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]>61:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 5}
               if obj[1]>9:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[5]>48:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
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
               elif obj[1]<=9:
                  # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=30:
                     # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[6]<=8:
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
